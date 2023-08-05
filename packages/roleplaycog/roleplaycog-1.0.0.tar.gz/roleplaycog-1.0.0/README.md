# Roleplay Cog
This package is a cog edition of [my roleplay bot repository](https://github.com/mariohero24/Roleplay-Bot) that has been heavily modified
## Installation
```cs
pip install roleplaycog
```
## Setup
```py
import discord
bot = discord.Bot()

# Loading via the setup function
bot.load_extension("roleplaycog")

# Loading directly (why would you do this)
from roleplaycog import Roleplay
bot.add_cog(Roleplay(bot))

bot.run("Token")
```