import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} خدام دابا فـ ROBALA RP 👑")

@bot.command()
async def hello(ctx):
    await ctx.send("مرحبا بيك فـ ROBALA RP 💚")

bot.run(TOKEN)
