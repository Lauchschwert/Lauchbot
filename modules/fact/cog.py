from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext.tasks import loop
from discord_slash import cog_ext
import requests



class fact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(name='fact')
    async def fact(self, ctx):
        url = "https://uselessfacts.jsph.pl/random.json?language=en"
        response = requests.get(url)
        value = response.json()["text"]
        await ctx.send("Here is a random and useless fact: " + value)

        
def setup(bot):
    bot.add_cog(fact(bot))
