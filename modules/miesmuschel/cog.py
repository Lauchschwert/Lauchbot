from discord.ext import commands
import discord
from discord.ext.tasks import loop
import datetime
import random


class miesmuschel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='miesmuschel')
    async def miesmuschel(self, interaction: discord.Interaction):
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
        await interaction.response.send_message(random.choice(answers))

async def setup(bot):
    await bot.add_cog(miesmuschel(bot))
