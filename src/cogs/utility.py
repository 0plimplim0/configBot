from discord.ext import commands
import discord
from inspect import cleandoc
class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
            description='Muestra la latencia del WebSocket.'
    )
    async def ping(self, ctx):
        ms_latency = round(self.bot.latency * 1000)
        await ctx.send(f'🏓 ¡Pong! Latencia del WebSocket: {ms_latency}ms')
    
    @commands.command(
            description='Muestra el prefijo que uso.'
    )
    async def prefix(self, ctx):
        await ctx.send(f'El prefijo que uso es {ctx.prefix}')
    
    @commands.command(
            description='Muestra informacion general de un usuario.',
            usage='[@usuario]'
    )
    async def userinfo(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.author

        text = cleandoc(f'''
            # 📇 **EXPEDIENTE DE USUARIO**
            ### 🆔 **IDENTIDAD**
            > **USER** │ `{user.name}`
            > **UUID** │ `{user.id}`

            ### ⏳ **LÍNEA DE TIEMPO**
            > **REGISTRO** │ `{user.created_at.strftime('%d/%m/%Y')}` 
            > **LLEGADA**   │ `{user.joined_at.strftime('%d/%m/%Y')}`
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
            title=user.name,
            color=discord.Color.blue()
        )
        embed.set_image(url=user.avatar.url)

        await ctx.send(embed=embed)

    @commands.command(
            description='Muestra informacion general del servidor.'
    )
    async def serverinfo(self, ctx):

        text = cleandoc(f'''
            # **ESTADO DEL SERVIDOR**
            ### 👑 PROPIEDAD
            > **OWNER** | {ctx.guild.owner.mention}
            > **CREACIÓN** | {ctx.guild.created_at.strftime('%d/%m/%Y')}
            ### 👥 POBLACIÓN
            > **TOTAL** | {ctx.guild.member_count}
            > **HUMANOS** | {len([m for m in ctx.guild.members if not m.bot])}
            > **BOTS** | {len([m for m in ctx.guild.members if m.bot])}
            > **BOOSTS** | Tier {ctx.guild.premium_tier} ({ctx.guild.premium_subscription_count} mejoras)
            ### 📂 INFRAESTRUCTURA
            > **CANALES** | {len(ctx.guild.channels)} (💬 {len(ctx.guild.text_channels)} | 🔊 {len(ctx.guild.voice_channels)} | 📢 {len(ctx.guild.stage_channels)})
            > **ROLES** | {len(ctx.guild.roles) - 1}
            > **EMOJIS** | {len(ctx.guild.emojis)} / {ctx.guild.emoji_limit}
        ''')

        embed = discord.Embed(
            title=ctx.guild.name,
            description=text,
            color=discord.Color.blue()
        )

        embed.set_footer(text=f'✨ ID del servidor: {ctx.guild.id}')
        embed.set_thumbnail(url=ctx.guild.icon.url)

        await ctx.send(embed=embed)

    @commands.command(
            description='Muestra informacion de ayuda.',
            usage='[command]'
    )
    async def help(self, ctx, command: str = None):
        if command == None:
            embed = discord.Embed(
                title='Ayuda',
                description='Ayuda jeje',
                color=discord.Color.blue()
            )

            embed.set_footer(text='✨ Usa !help <comando> para ver detalles específicos.')
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))