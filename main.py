import os
import asyncio
import discord
import datetime
from discord.ext import commands
import requests
import json
import sys

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

def main():
    bot = commands.Bot(
        command_prefix=commands.when_mentioned_or(">>>"),
        intents=intents
    )
    bot.remove_command("help")

    @bot.event
    async def on_ready():
        print(f"{bot.user.name} has connected to Discord.")
        activity = discord.Activity(type=discord.ActivityType.watching, name="Jojo's bizarre adventure")
        await bot.change_presence(status=discord.Status.dnd, activity=activity)

    @bot.event
    async def on_message(message):
        if message.author.bot:
            return False
        await bot.process_commands(message)

    @bot.event
    async def on_command_error(ctx, error):
        embed = discord.Embed(title=":x: Command Error", colour=0x992D22)  # Dark Red
        embed.add_field(name="Error", value=str(error))
        embed.add_field(name="Guild", value=ctx.guild.name)
        embed.add_field(name="Channel", value=ctx.channel.name)
        embed.add_field(name="User", value=ctx.author.name)
        embed.add_field(name="Message", value=ctx.message.clean_content)
        embed.timestamp = datetime.datetime.utcnow()
        try:
            await ctx.reply(embed=embed)
        except discord.Forbidden:
            await ctx.send("An error occurred, but I couldn't send the error message. Please check my permissions.")
        except:
            pass

    # load all modules
    class Bot(commands.Bot):
        def __init__(self, *, intents: discord.Intents):

            super().__init__(command_prefix=commands.when_mentioned_or("$$"), intents=intents)

        async def setup_hook(self):
            for filepath in os.listdir('modules'):
                for filename in os.listdir(f'modules/{filepath}'):
                    if filename.endswith('.py'):
                        filename = filename.replace('.py', '')
                        allmodules += 1
                        try:
                            await bot.load_extension(f'modules.{filepath}.{filename}')
                            print(f'Loaded modules.{filepath}.{filename}')
                            loaded += 1
                        except Exception as error:
                            print(f'Failed to load modules.{filepath}.{filename}: {error}')

            await self.tree.sync()

    with open("config.json", "r", encoding="UTF-8") as configfile:
        config = json.load(configfile)
        token = config.get("token")
        if not token:
            print("[ERROR] Value for key 'token' is missing in config.json. Please check the configuration file and try again.")
            sys.exit()
    
    bot.run(token)

if __name__ == '__main__':
    main()
