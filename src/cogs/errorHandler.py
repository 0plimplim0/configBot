from discord.ext import commands

class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return
        
        error = getattr(error, 'original', error)

        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f'No tienes permisos suficientes para ejecutar {ctx.command}.', delete_after=3)
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'Calma... Intenta de nuevo en {error.retry_after:.2f}s', delete_after=3)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Missing argument: `{error.param.name}`.', delete_after=3)
        else:
            print(f'Error no manejado en {ctx.command}: {error}')

async def setup(bot):
    await bot.add_cog(ErrorHandler(bot))