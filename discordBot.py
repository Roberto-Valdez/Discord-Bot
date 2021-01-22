import discord, datetime, random, requests
from discord import Embed
from discord.ext import commands
from bs4 import BeautifulSoup

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('bot is ready')

@client.command()
async def date(ctx):
    date = datetime.date.today()
    await ctx.send(date)

@client.command()
async def game(ctx):
    games = ['Overwatch', 'Counter Strike Global Offensive', 'Halo', 'Valorant', 'GTA']
    await ctx.send('You should play ' + random.choice(games))

@client.command()
async def bored(ctx):
    embed = Embed(description="https://en.wikipedia.org/wiki/Special:Random")
    await ctx.send(embed=embed)

@client.command()
async def bitcoin(ctx):
    source = requests.get('https://www.coindesk.com/price/bitcoin').text
    soup = BeautifulSoup(source, 'lxml')
    bitcoinPrice = soup.find('div', class_='price-large').text
    await ctx.send('The price of bitcoin is currently ' + bitcoinPrice)

client.run('SERVER TOKEN GOES HERE')
