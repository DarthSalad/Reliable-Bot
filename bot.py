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

bot.run(token)
#client.run(token)
#live score
