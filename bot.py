import discord
import os
from dotenv import load_dotenv

client=discord.Client()
load_dotenv()
token = os.getenv('TOKEN')
guild = os.getenv('GUILD')
@client.event
async def on_ready():
	for guild in client.guilds:
    		if (guild.name == guild):
            		break

	print(f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})')

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith('$hello'):
		await message.channel.send('Hello!')
	elif message.content.startswith('$ahem'):
		await message.channel.send('Want some Cough Syrup?')

client.run(token)
