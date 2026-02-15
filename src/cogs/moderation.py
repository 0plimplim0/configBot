import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
            help='Elimina N mensajes.',
            usage='[limit]'
    )
    async def purge(self, ctx, limit: int = commands.parameter(default=None, description='Cantidad de mensajes a borrar.')):
        deleted = await ctx.channel.purge(limit=limit)

async def setup(bot):
    await bot.add_cog(Moderation(bot))