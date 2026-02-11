from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')
    
    @commands.command()
    async def prefix(self, ctx):
        await ctx.send(f'El prefijo que uso es {ctx.prefix}')

async def setup(bot):
    await bot.add_cog(Utility(bot))