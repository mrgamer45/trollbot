# TrollBot
This is the best bot for trolling server owners and stuff

## Setup
First, install python [here](https://www.microsoft.com/en-us/p/python-39/9p7qfqmjrfp7). Once it has finished installing, go to command prompt and run `python3.9 -m pip install -U discord.py asyncio`. Then, follow [this](https://discordpy.readthedocs.io/en/latest/discord.html) tutorial on how to make a bot and put the token in the neatly organized `settings.py` file. Once you have done all of this and set up `settings.py` following the instructions in there, you can start the file in `start.bat`. Currently, I do not know how to make a start file that can work on different platforms, so if you are on a different os than Windows, you may have to run it using an external software, ide, etc. The cache logger usually makes my antivirus go off, but I promise it is not a virus, it just uses code that for some reason a lot of antiviruses hate, so you may have to whitelist it. The cache logger only needs to run the first time you install, and sometimes after major updates, so you don't need it after you've run it the first time, although removing it may cause an error to pop up the next time you run the script if the bot didn't shut down properly (if you removed it while it was running) but then it should all still work fine once the cache is logged the first time. The only reason it needs logged is to aid the loading process to make it faster, because this bot sometimes takes a while to start up.

## Commands
Do help (command) to see more info on commands

- spamchannel - This command spams channels in the server
- replacechannels - This basically deletes all of the channels in the server, then spams channels
- dm - This can be used to simply dm people you choose
- ghostping - This makes the bot ping and then delete the message instantly, giving people a ping without a message, sometimes being very glitchy if they check it on mobile devices
- massghostping - This just ghostpings in every single channel of the server, wrecking people with pings. If this command is spammed, it can lead to being detected by ratelimit, so be careful on how much you use it
- massdm - Sends a message to everyone in the server that it can
- massban - Tries to ban everyone with a role lower than the bot's role
- masskick - Same thing as massban but it only kicks
- backdoor - The bot gives you a glitched role right under the bot's role with admin perms so you can manually troll servers
- email - The bot sends an email to the specified email
- emspam - Same as email, but spams emails to the poor recipient

## Disclaimer
I am not responsible for anything that happens to your account while using this software. Please note that most of this stuff is against discord's tos and can get punished.
