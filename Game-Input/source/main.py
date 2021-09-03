from quixstreaming import *
import threading
import signal
import time
import datetime

# Create a client. Client helps you to create input reader or output writer for specified topic.
certificatePath = "../certificates/ca.cert"
username = "[WORKSPACE]"
password = "[PASSWORD]"
broker = "kafka-k1.quix.ai:9093,kafka-k2.quix.ai:9093,kafka-k3.quix.ai:9093"

security = SecurityOptions(certificatePath, username, password)

properties = {
    "acks": "0"
}

client = StreamingClient(broker,
                         security,
                         properties)
# Change consumer group to a different constant if you want to run model locally.
print("Opening input and output topic")
input_topic = client.open_input_topic('[WORKSPACE]-gamedata', "default-consumer-group")
output_topic = client.open_output_topic('[WORKSPACE]-car-game-input')


# Callback called for each incoming stream
def read_stream(new_stream: StreamReader):
    # Create a new stream to output data
    stream_writer = output_topic.create_stream(new_stream.stream_id + "-car-game-input")

    stream_writer.properties.parents.append(new_stream.stream_id)

    stream_writer.parameters.add_definition("throttle").set_range(0.0, 1.0)
    stream_writer.parameters.add_definition("brake").set_range(0.0, 1.0)
    stream_writer.parameters.add_definition("steering").set_range(-1.0, 1.0)
    last_time = time.time_ns()

    # Callback triggered for each new data frame
    def on_parameter_data_handler(data: ParameterData):
        nonlocal last_time
        print(time.time_ns() - last_time)
        last_time = time.time_ns()
        
        for row in data.timestamps:
            y_grav = row.parameters["Y_grav"].numeric_value

            receivedThrottle = row.parameters["throttle"].numeric_value
            receivedBrake = row.parameters["brake"].numeric_value

            # We calculate steering angle from g force data.
            steering = y_grav / 4.5

            data = ParameterData()

            data.add_timestamp(datetime.datetime.utcnow()) \
                .add_tags(row.tags) \
                .add_value("throttle", receivedThrottle) \
                .add_value("oldtimestamp", str(row.timestamp)) \
                .add_value("delta2", (row.timestamp_nanoseconds / 1000000)  - int((time.time()) * 1000)) \
                .add_value("brake", receivedBrake) \
                .add_value("steering", steering)

            stream_writer.parameters.write(data)

    # React to new data received from input topic.
    new_stream.parameters.on_read += on_parameter_data_handler

    # When input stream closes, we close output stream as well.
    def on_stream_close(endType: StreamEndType):
        stream_writer.close(endType)
        print("Stream closed:" + stream_writer.stream_id)

    new_stream.on_stream_closed += on_stream_close

    # React to any metadata changes.
    def stream_properties_changed():
        if new_stream.properties.name is not None:
            stream_writer.properties.name = new_stream.properties.name + " car game input"

    new_stream.properties.on_changed += stream_properties_changed


# Hook up events before initiating read to avoid losing out on any data
input_topic.on_stream_received += read_stream
input_topic.start_reading()  # initiate read

# Hook up to termination signal (for docker image) and CTRL-C
print("Listening to streams. Press CTRL-C to exit.")

# Below code is to handle gracesfull exit of the model.
event = threading.Event()


def signal_handler(sig, frame):
    print('Exiting...')
    event.set()


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
event.wait()