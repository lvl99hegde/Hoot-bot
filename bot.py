import discord
from discord.ext import commands
import os  # Move import to top

# Enable intents
intents = discord.Intents.default()
intents.message_content = True

# Create bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print("HootBot is online")

# Command: !hoot
@bot.command()
async def hoot(ctx):
    await ctx.send("hoot")

# Run the bot using the token from environment variable
bot.run(os.getenv("TOKEN"))
