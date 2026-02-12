import discord
from discord.ext import commands
from helpers import database
class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setprefix(self, ctx, prefix: str):
        database.set_prefix(ctx.guild.id, prefix)
        await ctx.send(f'Prefijo actualizado a {prefix}')

    @commands.command
    @commands.has_permissions(administrator=True)
    async def allow(self, ctx, role: discord.Role, permission: discord.Permissions):
        pass

    @commands.command
    @commands.has_permissions(administrator=True)
    async def deny(self, ctx, role: discord.Role, permission):
        pass

async def setup(bot):
    await bot.add_cog(Config(bot))