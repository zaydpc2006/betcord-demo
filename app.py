import discord
from discord.ext import commands

# Enter your bot token securely (paste when you run the script)
TOKEN = "MTQzNjkwOTc3NzkyMDcyMTA1Mw.GtLcCn.ySXlhp7gTFYpeX248O4vWXME1MobuTfMtt0z0g"

# The channel ID your bot should respond in
TARGET_CHANNEL_ID = 1436908086731477155  # replace with your actual channel ID

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🤖 Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    """Replies only if command used in the allowed channel"""
    if ctx.channel.id != TARGET_CHANNEL_ID:
        return  # Ignore commands from other channels
    await ctx.send("Pong!")

@bot.event
async def on_message(message):
    # Ignore messages from other channels
    if message.channel.id != TARGET_CHANNEL_ID:
        return

    # Prevent bot from replying to itself
    if message.author == bot.user:
        return

    # You can add your custom responses here
    if message.content.lower() == "hello":
        await message.channel.send("Hey there 👋")

    # Process commands (!ping etc.)
    await bot.process_commands(message)

bot.run(TOKEN)
