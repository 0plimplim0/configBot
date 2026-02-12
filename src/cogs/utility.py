from discord.ext import commands
import discord
from inspect import cleandoc
class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')
    
    @commands.command()
    async def prefix(self, ctx):
        await ctx.send(f'El prefijo que uso es {ctx.prefix}')
    
    @commands.command()
    async def userinfo(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.author

        text = cleandoc(f'''
            # 📇 **EXPEDIENTE DE USUARIO**
            ### 🆔 **IDENTIDAD**
            > **USER** │ `{user.name}`
            > **UUID** │ `{user.id}`

            ### ⏳ **LÍNEA DE TIEMPO**
            > 📅 **REGISTRO** │ `{user.created_at.strftime('%d/%m/%Y')}` 
            > 📥 **LLEGADA**   │ `{user.joined_at.strftime('%d/%m/%Y')}`
        ''')

        embed = discord.Embed(
            title=user.name,
            description=text,
            color=discord.Color.blue(),
        )
        
        embed.set_footer(text='✨ Consulta generada por !userinfo')

        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.author

        embed = discord.Embed(
            title=user.name
        )
        embed.set_image(url=user.avatar.url)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))