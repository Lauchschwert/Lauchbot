import os
import asyncio
import discord
import datetime
from discord.ext import commands
import requests
import json
import sys

"""
CLIENT_ID = 't6b4d5a942qvmgpw0t0cb3a3r8jc6g'
AUTH_TOKEN = ''

STREAMER_NAME = 'Lauchschwert'

CHANNEL_ID = '863582397944692756'

client = discord.Client()

async def send_discord_message(message):
    channel = client.get_channel(int(863582397944692756))
    await channel.send(message)

def check_stream_status():
    url = f'https://api.twitch.tv/helix/streams?user_login=lauchschwert'
    headers = {'Client-ID': f'Bearer ', 'Authorization': f'Bearer '}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    if data['data']:
        return True
    else:
        return False

async def send_live_notification():
    message = f'Lauchschwert just went live on Twitch! Watch the stream here: https://www.twitch.tv/lauchschwert'
    await send_discord_message(message)


async def on_ready():
    while True:
        if check_stream_status():
            await send_live_notification()
        await asyncio.sleep(60)
"""


def main():
    client = commands.Bot(
        command_prefix=commands.when_mentioned_or(">>>"),
    )
    client.remove_command("help")

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to Discord.")
        await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="Jojo's bizarre adventure"))

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

    with open("config.json", "r", encoding="UTF-8") as configfile:
        config = json.load(configfile)
        token = config.get("token")
        if not token:
            print(f"[ERROR] Value for key 'token' is missing in config.json. Please check the configuration file and try again.")
            sys.exit()
    configfile.close()
    client.run(token)


if __name__ == '__main__':
    main()
