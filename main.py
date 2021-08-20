import discord
import os
import time
import random
from fuzzywuzzy import fuzz

# Bot Settings
client = discord.Client()

# Printing Booyaka means that the bot connected to Discord successfully 
@client.event
async def on_ready():
	print(f'Booyaka! {client.user} has connected to Discord!')

# This ignores its own messages, otherwise checks and responds if needed
@client.event
async def on_message(message):
	if message.author == client.user:
		return

	wen_list = ['wen', 'when', 'When', 'Wen']

	soon = ['Soon!', 'Soon, I guess..', 'I guess very soon!', 'Very soon!', 'Hmm..']

	if message.content in wen_list:
		time.sleep(0.2)
		await message.channel.send(random.choice(soon))

	if fuzz.ratio(message.content, 'When token') > 80:
		time.sleep(0.2)
		await message.channel.send(random.choice(soon))

	howsoon = [
	    'Very soon!',
	    'That I can\'t tell',
	    'Soon, maybe?',
	    'Honestly, IDK',
	    'Sooner than you get a girlfriend or boyfriend',
	    'Go get busy']

	if fuzz.ratio(message.content, 'How soon') > 80:
		time.sleep(0.2)
		await message.channel.send(random.choice(tuple(howsoon)))

	if fuzz.ratio(message.content, 'When exactly?') > 87:
		time.sleep(0.2)
		await message.channel.send('Go ask your mom')

	if fuzz.ratio(message.content, 'Fuck you') > 73:
		time.sleep(0.2)
		await message.channel.send('Fuck you too!')

# Run the client using the token stored in .env file
client.run(os.getenv('TOKEN'))