import discord
import os
from dotenv import load_dotenv
import random
from discord import opus
from discord.ext import commands
from googlesearch import search
import youtube_dl
import requests
import json

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

@bot.command(pass_context=True, help='Greets back the user', aliases=['yo', 'hi', 'hey'])
async def hello(ctx):			
    await ctx.send("Hello {}!".format(ctx.author.mention))	#mentions the user instead of writing their user names(not nicknames)
#bot.command(name="yo", pass_context=True)(hello.callback)		#aliases worls instead of this shit
#bot.command(name="hi", pass_context=True)(hello.callback)

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

# class JoinDistance:						#to get the join and creation date of an user's acc
#     def __init__(self, joined, created):
#         self.joined = joined
#         self.created = created

#     @property
#     def delta(self):
#         return self.joined - self.created

# class JoinDistanceConverter(commands.MemberConverter):
#     async def convert(self, ctx, argument):
#         member = await super().convert(ctx, argument)
#         return JoinDistance(member.joined_at, member.created_at)

#working join date code
# @bot.command(name="acc", help="Shows the account creation date and joining date of the user")
# async def delta(ctx):
# 	date = "\n".join(str(ctx.message.author.joined_at).split(' '))
# 	await ctx.send("{} joined Discord on {}" .format(ctx.message.author.mention, date[:10]))

#need to @ a member but working
@bot.command(help="Shows the account creation date and joining date of the user")
async def acc(ctx, *, member: discord.Member = None):
	if not member:
    		member = ctx.author
	date1 = "\n".join(str(member.joined_at).split(' '))
	date2 = '\n'.join(str(member.created_at).split(' '))
	await ctx.send('{} joined this server on {} and created their account on {}'.format(member.mention, date1[:10], date2[:10]))

#try at web scraping
@bot.command(help="Lists the first 10 results from the web")
async def gsearch(ctx):
	await ctx.send("Type the search query")
	def check(msg):
    		return msg.author == ctx.author and msg.channel == ctx.channel
	msg = await bot.wait_for("message", check=check)
	return_value=search(str(msg.content), tld='co.in', num=10, stop=10, pause=2)
	for j in return_value:
			await ctx.send(j)

@bot.command(name='gg', helps='gg')
async def gg(ctx):
	await ctx.send('https://i0.wp.com/ytimg.googleusercontent.com/vi/tN6VMf3wTUo/maxresdefault.jpg?resize=650,400')

players = {}

@bot.command(pass_context=True)
async def bruh(ctx):
    # await ctx.author.voice.channel.connect()
    # player = await ctx.author.voice.channel.create_ytdl_player(r'https://youtu.be/2ZIpFytCSVc')
	# # players[ctx.message.server.id] = player
	# player.start()
	vc = await ctx.author.voice.channel.connect()
	player = await vc.create_ytdl_player(r'https://youtu.be/2ZIpFytCSVc')
	player.start()

@bot.command()
async def leave(ctx):
    await ctx.voice.channel.disconnect()

@bot.command()
async def drake(ctx, arg1, arg2):
	def jprint(obj):
		text = json.dumps(obj, sort_keys=True, indent=4)
		print(text)

	parameters = {
		"template_id": 181913649,
		"username": 'darthsalad',
		"password": 'Beyblade@321',
		'text0': str(arg1),
		'text1': str(arg2),
	}

	response = requests.post(r'https://api.imgflip.com/caption_image', params= parameters)
	await ctx.send(response.json()['data']['url'])

bot.run(token)
#client.run(token)

#torrent link search
#done google search, started working on fetching links from a particular site with keywords
