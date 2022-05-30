from discord.ext import commands
import discord
import discord_slash
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext.tasks import loop
from discord_slash import cog_ext
import datetime
import random

class miesmuschel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(name='miesmuschel')
    @commands.guild_only()
    async def miesmuschel(self, ctx: discord.Member):
        answers = [
            "Yes",
            "No",
            "Ask me again",
            "Why do you need to ask?",
            "Go away. I do not wish to answer at this time.",
            "Time will only tell",
                ]
        await ctx.send(random.choice(answers))




def setup(bot):
    bot.add_cog(miesmuschel(bot))


         