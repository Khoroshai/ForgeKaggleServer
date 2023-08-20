# Forge Minecraft Server
This method is inspired from MineColab (https://github.com/thecoder-001/MineColab)
and derived from my Colab version (https://github.com/Khoroshai/ForgeColabServer)

*It uses free ressources thanks to Kaggle, do not abuse of it.*

This method uses zipped saves files and zipped server folder stored on your gdrive.

The world files and logs are saved to gdrive every 5 minutes.

*Tested on 1.18.2 with around 80 mods*

# Requirements
- An open tab that will stay focused
- A base vanilla minecraft server
- A base Forge server
- Mods
- A Playit.gg account (free)
- RCon enabled in *server.properties*.
- Set up pydrive (Nice tutorial here : https://medium.com/analytics-vidhya/how-to-connect-google-drive-to-python-using-pydrive-9681b2a14f20) Once you have your credentials file for Kaggle, you could put it in a private dataset so the notebook can easily access it.

# How to use
1) Prepare everything on your gdrive (zipped server with mods).
2) Edit the Strings in **Config**, then run.
3) Run **Initialization**.
4) Run **Start Server**.

# Additional informations
Compared to Colab, here the server initially didn't accept input command to the server. The method to run it is thus different. 
By using subprocess, threads and RCon, you can now run other cells while the server is up. 

The logs are visible in the Console or through a cell. This cell runs continuously but can be stopped by writing "y" in the input area.

**Any error or manually stopping a cell will also hard stop the server**.

To stop the server the good way, write "stop" in **Send Commands**.
