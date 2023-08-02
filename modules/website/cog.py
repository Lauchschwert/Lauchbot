from discord.ext import commands
import discord
import datetime


class website(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='website')
    @commands.guild_only()
    async def website(self, ctx):
        try:
            await ctx.send("My Website => https://www.lauchschwert.xyz")
            await ctx.send("Anditv's Website => https://gamekiller.at")
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
    bot.add_cog(website(bot))
