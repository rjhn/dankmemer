import discord
from discord.ext import commands
import json
import asyncio
import os



client = commands.Bot(command_prefix='x', description='''Dank Farmer''', self_bot=True)

client.remove_command('help')



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="Dank Memer Farming!", url="https://www.twitch.tv/smokedlel"))
    print(f'Dank memer bot is running.\nPrefix: x')

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Commands")
    embed.add_field(name="Commands", value="start\nstop")
    await ctx.reply(embed=embed)

@client.command()
async def start(ctx):
    await ctx.send('pls daily')
    await ctx.send('pls monthly')
    for i in range(100):
        await ctx.send('pls beg')
        await ctx.send('pls fish')
        await ctx.send('pls dig')
        await ctx.send('pls hunt')
        await ctx.send('pls slots 1000')
        await asyncio.sleep(50)

@client.command()
async def stop(ctx):
    embed = discord.Embed(title="stopping", description="Stopping the grind.")
    await ctx.reply(embed=embed)
    await client.close()
    os._exit    
        


client.run('TOKEN HERE', bot=False)
