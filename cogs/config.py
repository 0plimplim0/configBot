from discord.ext import commands
from helpers import database
class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setprefix(self, ctx, prefix: str):
        database.set_prefix(ctx.guild.id, prefix)
        await ctx.send(f'Prefijo actualizado a {prefix}')

async def setup(bot):
    await bot.add_cog(Config(bot))