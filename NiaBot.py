import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix = "%")

offline = discord.Status.offline
online = discord.Status.online

@bot.event
async def on_ready(): 
    await bot.change_presence(status=online, activity=discord.Game(name="with your mind"))
    print("Bot Booted and is Ready!")

@bot.command(pass_context=True)
async def embed(ctx, title:str="", desc:str=""):
    embed = discord.Embed(title=title, description=desc, color=0xff823f)
    await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    f = open("LOGS.txt","a")
    if message.author.name == "𝒶𝑒𝓇𝓈𝑜𝓃𝒶𝓁":
        name = "aersonal"
    else:
        name = message.author.name
    KEK = f'[[{message.guild.name}]]-[{message.channel.name}]: |{name}| "{message.content}"'
    print(KEK)
    f.write(f"{KEK}\n")

@bot.event
async def status_task():
    while True:
        await bot.change_presence(status=online, activity=discord.Game(name="with your mind"))
        asyncio.sleep(15)
        await bot.change_presence(status=online, activity=discord.Game(name="with my girlfriend"))
        asyncio.sleep(15)
        await bot.change_presence(status=online, activity=discord.Spotify(name="to your chats"))
        asyncio.sleep(15)
        await bot.change_presence(status=online, activity=discord.Game(name="4D chess"))
        asyncio.sleep(15)
        await bot.change_presence(status=online, activity=discord.Spotify(name="livvie sleep"))
        asyncio.sleep(5)


bot.run(token)