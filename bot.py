import discord
import os
from dotenv import load_dotenv
import random
from discord.ext import commands

# client=discord.Client() 	#ok, so client is basically useless
							#client doesn't work if bot is invoked (bot importance > client(renders null))
load_dotenv()
token = os.getenv('TOKEN')
guild = os.getenv('GUILD')
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
	for guild in bot.guilds:
    		if (guild.name == guild):
            		break

	print(f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})')

# @client.event
# async def on_message(message):
# 	if message.author == client.user:
# 		return
# 	if message.content.startswith('$hello'):
# 		await message.channel.send('Hello!')
# 	elif message.content.startswith('$ahem'):
# 		await message.channel.send('Want some Cough Syrup?')
@bot.command(name='hi')
async def cough(ctx):
	response = 'Hello There'
	await ctx.send(response)
	
@bot.command(name='ahem')
async def cough(ctx):
	response = 'Want some Cough Syrup?'
	await ctx.send(response)

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    quotes = ['Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ), 'Noice.', 'Name of your sex tape!', ''
    ]

    response = random.choice(quotes)
    await ctx.send(response)

bot.run(token)
# client.run(token)
