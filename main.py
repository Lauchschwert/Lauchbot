import os
import discord
import datetime
from discord import guild
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.utils import get
from discord.ext import commands

def main():
        activity = discord.Activity(
        type=discord.ActivityType.watching, name="Jojo's bizarre adventure")
        client = commands.Bot(
        command_prefix=commands.when_mentioned_or(">>>"),
        activity=activity,
        status=discord.Status.dnd,)

        client.remove_command("help")
        
        @client.event
        async def on_ready():
            print(f"{client.user.name} has connected to Discord.")

        @client.event
        async def on_message(message):
            if message.author == client.user:
                return


            await client.process_commands(message)

        @client.event
        async def on_command_error(ctx, error):
                embed = discord.Embed(title=":x: Command Error",
                colour=0x992D22)  # Dark Red
                embed.add_field(name="Error", value=error)
                embed.add_field(name="Guild", value=ctx.guild)
                embed.add_field(name="Channel", value=ctx.channel)
                embed.add_field(name="User", value=ctx.author)
                embed.add_field(name="Message", value=ctx.message.clean_content)
                embed.timestamp = datetime.datetime.utcnow()
                try:
                    await ctx.reply(embed=embed)
                except:
                    pass

        # load all cogs
        for folder in os.listdir("modules"):
            if os.path.exists(os.path.join("modules", folder, "cog.py")):
                client.load_extension(f"modules.{folder}.cog")      
                
        file = open('token.txt').read()
        client.run(file)


if __name__ == '__main__':
    main()
