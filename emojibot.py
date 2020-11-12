import discord
import asyncio
import os
import sys
import urllib.request

# create a client
client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as \"%s\" with ID %s' % (client.user.name, client.user.id))
	for guild in client.guilds:
		guildName = str(guild.name)
		emojiNum = len(guild.emojis)
		# print out guild names and number of emojis
		print(guildName + ': ')
		print('Emoji count: ' + str(emojiNum))
		# make a folder for each folder if it actually has emojis, striping out invalid characters
		folderName = 'Emojis - ' + guildName.translate({ord(c): None for c in '/<>:"|?*'})
		if emojiNum > 0:
			if not os.path.exists(folderName):
				os.makedirs(folderName)
			# download the emojis
			print('Downloading emojis...')
			for emoji in guild.emojis:
				# create a file name
				if emoji.animated:
					fileName = folderName + '/' + emoji.name + '.gif'
				else:
					fileName = folderName + '/' + emoji.name + '.png'
				# download if we dont already have it
				if not os.path.exists(fileName):
					with open (fileName, 'wb') as outFile:
						# send a different header because otherwise we get a 403
						req = urllib.request.Request(emoji.url, headers={'User-Agent': 'Mozilla/5.0'})
						data = urllib.request.urlopen(req).read()
						outFile.write(data)

	print('All done!')
	await client.logout()


if len(sys.argv) == 2:
	try:
		client.run(sys.argv[1], bot=False)
	except discord.LoginFailure:
		print('oops!')
		client.logout()
elif len(sys.argv) == 3:
	try:
		client.run(sys.argv[1], sys.argv[2])
	except discord.LoginFailure:
		print('oops2!')
else:
	print('Invalid number of arguments. If using 2FA, your token is required. '
		  'Otherwise, provide your email and password. See https://github.com/qwertyboy/emoji-dumper'
		  ' for more details.')
	

