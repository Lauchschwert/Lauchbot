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
    async def miesmuschel(self, ctx, question):
        try:
            answers = [
                "Yes",
                "yep",
                "yea",
                "yup"
                "No",
                'Positive',
                'From my point of view, yes',
                'From my point of view, no',
                'Convinced.',
                'Most Likley.',
                'Chances High',
                "of course not",
                "negative",
                "never",
                "Ask me again",
                "Why do you need to ask?",
                "Go away. I do not wish to answer at this time.",
                "Time will only tell",
                "Maybe in an hour",
                "perhaps",
                "maybe",
                "possibly",
                "Maybe one day",
                "I don't think so",
                "I dont care",
                "If it makes you happpier... Yes.",
                "I dont think so.",
                "How about...... No!",
                "How about...... Yes!",
                "Dont ask me that...",
                'Not Sure',
                'Maybe',
                'I cannot predict now.',
                'Im to lazy to predict.',

            ]
            await ctx.send(random.choice(answers))
        except Exception as e:
            embed = discord.Embed(title=":x: Command Error",
            colour=0x992D22)  # Dark Red
            embed.add_field(name="Error", value=e)
            embed.add_field(name="Guild", value=ctx.guild)
            embed.add_field(name="Channel", value=ctx.channel)
            embed.add_field(name="User", value=ctx.author)
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(miesmuschel(bot))
