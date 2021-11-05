# Discord Rich Presence Tool

Discord Rich Presence Tool is a tool to show off a customized rich presence on your Discord profile.

![An image of the banner of this awesome project](https://sentinelx.xyz/images/DRPCToolBanner.gif)

## Audience
Since some stuff you have to do in order to make use of this little script is found on a "developer application page", I'd say it can be confusing for people with limited to no technical background / education.

conclusion: **targeted audience;** somewhat experienced around webpanels and commandline utilities

## dependencies
[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

- Latest Python version. Click [here](https://python/org) to download & install Python.

- [`psutil`]()(Python external library / module)
- [`pypresence`](https://github.com/qwertyquerty/pypresence) (Python external library / module)
- any Terminal that **supports ANSI Escape codes**\
\
You are more than welcome to use any Terminal without ANSI Escape code support, of course. But it will be very unreadable. I **highly** suggest Powershell for Windows 8.1, 10, 11 users

## Installation
*instructions are made for Windows users*\
*for Linux users, you know your ways 🙃.*

1.) Install the [Latest Python version](https://python/org), if you haven't already

2.) Press **Windows logo key** + **X**
- Click "Windows Terminal" or "Windows Powershell".\
\
*We call this a* **terminal** *or* **command prompt** *. In this documentation, we use this word to refer to that.*

- keep the **terminal** open.

3.) Now go to your **terminal** and Install the following:
- **[`pypresence`](https://github.com/qwertyquerty/pypresence)**, if not installed.
    ```powershell
    python -m pip install pypresence --user
    ```
- **[`psutil`](https://github.com/giampaolo/psutil)**, if not installed.
    ```powershell
    python -m pip install psutil --user
    ```

4.) Now go to your **terminal**. In  your **terminal**, **clone** this repository by **copying** the below text and **pasting** it in your **terminal**, then finally, hit enter.
```
git clone https://github.com/Dr-Insanity/DiscordWebHookTool.git
```
*what is a* **clone**?\
*This is literally a clone, it makes a complete copy of the repository*

5.) You're **done**! Please proceed to the **Usage** section below.

## Usage
*I am assuming you still haven't closed your* **terminal** *yet*.

Go to the **terminal** and **copy** the below text and **paste** it in your **terminal**, then finally, hit enter.
```
cd DiscordRichPresenceTool
```
Now, In  your **terminal**, and **paste** the below text in your **terminal**, then finally, hit enter.
```
python RPC_Launcher.py
```
You have now opened the tool and it's initializing\
It looks like this:

![An image of the beginning screen](https://sentinelx.xyz/images/DRPCToolSplashScreen.jpg)

*But it isn't loading anything...*\
 Yes, It's for you to read this screen, I set a timer so it doesn't instantly skip to the main functions

Now, simply follow the steps / questions shown in your **terminal**

## Questions?
join the discord server: [The Sentinel Project](https://discord.com/invite/X2NeNS3Qkg)

## Features
- Change previously-configured Rich Presence
- Buttons on your Rich Presence
- **[Coming soon]** Save multiple Rich Presences
- **[Coming soon]** Logo's / Images on your Rich Presence
- Undoubtedly, enhancement

## Contributing
This project is not open for contribution, as per my preference.

## License
MIT