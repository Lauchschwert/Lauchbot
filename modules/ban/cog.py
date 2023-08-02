import discord
from discord import app_commands
from discord.ext import commands

class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ban", description="Ban someone")
    @discord.app_commands.describe(member="The member you want to ban")
    @discord.app_commands.describe(reason="Why do you want to ban this member?")
    async def ban(self, interaction: discord.Interaction, user: discord.Member, *, reason: str = None):
            if not interaction.guild.me.guild_permissions.ban_members:
                embed = discord.Embed(
                    title="Permission Denied",
                    color=0xff0000
                ).add_field(
                    name="Error",
                    value="I do not have permission to ban members.",
                    inline=True
                )
                return await interaction.response.send_message(embed=embed, ephemeral=True)

            # Check if the user has the permission to ban members
            if not interaction.user.guild_permissions.ban_members:
                embed = discord.Embed(
                    title="Permission Denied",
                    color=0xff0000
                ).add_field(
                    name="Error",
                    value="You do not have permission to use this command.",
                    inline=True
                )
                return await interaction.response.send_message(embed=embed, ephemeral=True)

            if reason == None:
                reason = "none"
            await user.ban(reason=reason)
            embed = discord.Embed(
            title="💥 User has been banned!", color=0x00d9ff)
            embed.set_author(name=interaction.author, icon_url=interaction.author.avatar_url)
            embed.add_field(name="User:", value=user.mention, inline=True)
            embed.add_field(name="Banned by: ",
            value=interaction.author.mention, inline=True)
            embed.add_field(name="Reason: ", value=reason, inline=True)
            await interaction.send(embed=embed)
            try:
                await user.send(f"You have been banned from {interaction.guild.name} Reason: " + reason)
            except Exception as e:
                print(e)

def setup(bot):
    bot.add_cog(ban(bot))
