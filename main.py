import os
import sys
import json
from datetime import datetime
from urllib.parse import quote
from discord.ext import commands
import discord

sys.dont_write_bytecode = True


class Bot(commands.Bot):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(command_prefix=commands.when_mentioned_or(">>>"), intents=intents)

    async def setup_hook(self):
        for folder in os.listdir('modules'):
            for filename in os.listdir(f'modules/{folder}'):
                if filename.endswith('.py'):
                    filename = filename.replace('.py', '')
                    try:
                        await bot.load_extension(f'modules.{folder}.{filename}')
                        print(f'Loaded modules.{folder}.{filename}')
                    except Exception as error:
                        print(f'Failed to load modules.{folder}.{filename}: {error}')

        await self.tree.sync()


intents = discord.Intents.all()
intents.presences = True
intents.members = True

with open('bot_config.json') as config_file:
    config = json.load(config_file)
    token = config.get('token')

if not token:
    print("Error: Bot token not found in config.json.")
    sys.exit(1)

bot = Bot(intents=intents)
bot.remove_command("help")


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord.")
    activity = discord.Activity(type=discord.ActivityType.watching, name="Jojo's bizarre adventure")
    await bot.change_presence(status=discord.Status.dnd, activity=activity)


bot.run(token=token, log_level=40)
