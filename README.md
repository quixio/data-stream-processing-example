# data-stream-processing-example
This Data Streaming and Processing Example Code will help you build your own realtime interactive creation.

---

## Getting Setup

There are a few tasks to complete before you can get up and running.

1. Signup to Quix
2. Create a workspace and 3 topics
3. Copy the code over from GitHub
4. Update the credentials
5. Deploy
6. Play
7. Make it your own!
---

## Lets Get you signed up!
Sign up to Quix. It's free. No credit card required and we give you some free credit to get going.

[Sign up here](https://quix.ai/self-sign-up)

## Create your workspace and topics

[Create a workspace](https://quix.ai/docs/guides/how-to/manage-workspaces/create.html) for your creation!
[Create 3 topics](https://quix.ai/docs/guides/how-to/manage-topics/create.html)

These needs to be called:
- gamedata
- car-game-control
- car-game-input

**Persist the 'gamedata' topic** for help on that see [here](https://quix.ai/docs/guides/how-to/manage-topics/persist.html)

## Lets get Coding

### Create 3 projects in Quix

These dont need specific names, but ours are called:
- 'UI' - This is a Node.JS project
- 'car-game-input' - This is a Python project
- 'game-control' - This is a Python project

Use these names to start with, it'll be easier if you need a hand later.

For help creating a project check out the Docs [here](https://quix.ai/docs/guides/how-to/manage-projects/create.html)

### Copy the code

Copy the code from this GitHub repo into the relevant folders of your projects.

We suggest cloning the Quix projects to your machine then you can easily copy and paste the code. Click the clone button in each of the Quix portal project pages to clone each project.

The projects you clone from Quix will have more folders, just replace the 'source' folder with the 'source' folder from the relevant project.

If you need a hand give us a shout on [Discord](https://discord.gg/cRmJXpWqnD)

## Credentials

The code you copied contains some placeholders that need to be replaced.
- [WORKSPACE]
- [PASSWORD]
- [TOKEN_PLACEHOLDER]

[Click here](https://quix.ai/docs/guides/how-to/manage-topics/certificates.html) to find out how to get the 'Workspace' name and password. **Note Workspace is also known as the Username**
[Click here](https://quix.ai/docs/guides/how-to/manage-access-tokens/create.html) to find out how to get a PAT Token

In the **'UI'** project's 'source\js' folder there are 4 files that needs updating.
They need [WORKSPACE] and [TOKEN_PLACEHOLDER] replaced.
- result.js
- create-page.js
- phone-page.js
- landing-page.js

In the **'car-game-input'** project's 'source' folder there is 1 file that needs updating.
Replace the [WORKSPACE] and [PASSWORD] placeholders with the relevant values.
- main.py

Follow the same procedure for the **'game-control'** project.

## Save everything

Push all changes to your Quix GitLab repo. You'll now be able to reload the Quix Portal in your browser and see all the changes there.

## To the Moon! (Well the cloud at-least)

Now you can deploy all 3 projects into the Quix Serverless Cloud.

If you need to [read about deployment here](https://quix.ai/docs/guides/how-to/manage-deployments/index.html)

But the key points you need to know are:

- Deploy all 3 projects, the names you give the deployments don't matter, but keep them similar to the projects for ease of identification.
- All 3 projects should be "Service" rather than "Job". So they restart if there is an issue.
- Set the resource sliders to about half to start with, if you notice that a service is maxing out its allocation, you can increase it a bit later.
- The 'UI' project must be publicly visible, so on the network tab turn on 'public access' and enter a url prefix.

## Show your friends/colleagues

Now's the time to have a play and show off to your colleagues!

Next to the 'UI' deployment is a small globe icon. Click that sucker.

**If something has gone wrong and you want assistance please do come and chat with us on [Discord](https://discord.gg/cRmJXpWqnD). We're really nice and will bend over backwards to help you out.**

## 

Now that you've got our version of the Data Stream Processing Example up and running why not make some changes!

Here's a list of the things we wanted to add but got side tracked on other fun stuff!

- A points system
- A trace of where the car has been and maybe how fast it was traveling at the time.
- Multiplayer! - We think we could support a full F1 grid
- How about web cams! - See the other players as they play?

What else can you come up with? How about using the code to create another type of game or demo?

- Online Pong?
- Your own version of Slack/Teams/etc

