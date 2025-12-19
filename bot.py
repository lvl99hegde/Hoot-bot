import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("HootBot is online")

@bot.command()
async def hoot(ctx):
    await ctx.send("hoot")

import os
bot.run(os.getenv("TOKEN"))
