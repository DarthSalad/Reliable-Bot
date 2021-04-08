import discord
import os
import random
from dotenv import load_dotenv
from discord import opus
from discord.ext import commands

load_dotenv()
token = os.getenv('TOKEN')
bot = commands.Bot(command_prefix='$')

for file in os.listdir('./cogs'):
    	if file.endswith('.py'):
    			bot.load_extension(f'cogs.{file[:-3]}')

@bot.event
async def on_ready():
	await bot.change_presence(status=discord.Status.idle, activity=discord.Game('$help'))
	for guild in bot.guilds:
    		if (guild.name == guild):
            		break

	print(f'{bot.user} is online')


@bot.command(pass_context=True, help='Greets back the user', aliases=['yo', 'hi', 'hey'])
async def hello(ctx):			
    await ctx.send("Hello {}!".format(ctx.author.mention))

@bot.command()
async def ahem(ctx):
	response = 'Want some Cough Syrup?'
	await ctx.send(response)

@bot.command(help='Responds with a random quote from JJBA')
async def jojo(ctx):
    quotes = ['NIGERUNDAYOO!!', 'Sunright Yero Ovadrivu!', "Hoo, you're approaching me?", 'OH MAI GOD!', 
	'ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA!', 'How many bread have you eaten in a lifetime?', 'I, Giorno Giovanna, have a dream.', 'Arrivederci',
	'STANDO PAWAH', 'Gureto desu yo..', 'MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDAAA!']
    response = random.choice(quotes)
    await ctx.send(response)

@bot.command(help='Simulates rolling dice.')
async def roll(ctx, num: int, sides: int):
	dice=[str(random.choice(range(1, sides + 1))) for _ in range(num)]
	await ctx.send(', '.join(dice))

@bot.command(help="Shows the account creation date and joining date of the user")
async def acc(ctx, *, member: discord.Member = None):
	if not member:
    		member = ctx.author
	date1 = "\n".join(str(member.joined_at).split(' '))
	date2 = '\n'.join(str(member.created_at).split(' '))
	await ctx.send('{} joined this server on {} and created their account on {}'.format(member.mention, date1[:10], date2[:10]))

@bot.command(name='gg', helps='gg')
async def gg(ctx):
	await ctx.send('https://i0.wp.com/ytimg.googleusercontent.com/vi/tN6VMf3wTUo/maxresdefault.jpg?resize=650,400')

bot.run(token)

#torrent link search
