import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from helpers import database

load_dotenv()
database.initDb()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    intents=intents,
    command_prefix=database.get_prefix,
    help_command=None
)

@bot.event
async def on_ready():
    print(f'Connected as {bot.user}')

async def main():
    async with bot:
        await bot.load_extension('cogs.utility')
        await bot.load_extension('cogs.config')
        await bot.load_extension('cogs.errorHandler')
        await bot.load_extension('cogs.moderation')
        await bot.start(os.getenv('BOT_TOKEN'))

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('\n[!] Bot apagado manualmente.')