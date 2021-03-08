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
# @bot.command(name='hi')
# async def hel(ctx):
# 	response = 'Hello '
# 	await ctx.send(response)

#if you call the name of the function(if you don;t have an alias for it), it still executes the code 
#so if i have 3 aliases for a single command, if i name the function after a command(from the 3), 
# and give aliases to the only the other 2, it would still work as 3 aliases

@bot.command(pass_context=True, help='Greets back the user')
async def hello(ctx):			
    await ctx.send("Hello {}!".format(ctx.message.author))
bot.command(name="hi", pass_context=True)(hello.callback)
bot.command(name="yo", pass_context=True)(hello.callback)

@bot.command(name='ahem')
async def cough(ctx):
	response = 'Want some Cough Syrup?'
	await ctx.send(response)

@bot.command(name='jojo', help='Responds with a random quote from JJBA')
async def nine_nine(ctx):
    quotes = ['NIGERUNDAYOO!!', 'Sunright Yero Ovadrivu!', "Hoo, you're approaching me?", 'OH MAI GOT!', 
	'ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA!', 'How many bread have you eaten in a lifetime?', 'I, Giorno Giovanna, have a dream.', 'Arrivederci',
	'STANDO PAWAH', 'Gureto desu yo..', 'MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDAAA!']
    response = random.choice(quotes)
    await ctx.send(response)

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, num: int, sides: int):
	dice=[str(random.choice(range(1, sides + 1))) for _ in range(num)]
	await ctx.send(', '.join(dice))

@bot.command(pass_context=True) 		#doesn't work for multiple commands for a single function
async def fuck(ctx):			
	await ctx.send('lil bitch')

bot.run(token)
#client.run(token)
#live score
