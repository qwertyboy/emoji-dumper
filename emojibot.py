import discord
import asyncio
import os
import sys
import urllib.request

# get character encoding for printing to the terminal
encoding = sys.stdout.encoding

# create a client
client = discord.Client()

# create a folder for storing the emojis
if not os.path.exists('Emojis'):
    os.makedirs('Emojis')

@client.event
async def on_ready():
    print('Logged in as \"%s\" with ID %s' % (client.user.name, client.user.id))
    print('Connected servers:')
    for server in client.servers:
        # print out server names and number of emojis
        print('\t%s (%s)' % (server.name.encode(encoding, 'replace').decode(encoding), server.id))
        emojiNum = len(server.emojis)
        print('\t\tEmoji Count: %s' % emojiNum)

        # make a folder for each folder if it actually has emojis, striping out invalid characters
        folderName = 'Emojis\\' + server.name.translate({ord(c): None for c in '/<>:"\\|?*'})
        if emojiNum > 0:
            if not os.path.exists(folderName):
                os.makedirs(folderName)

            # download the emojis
            print('\t\tDownloading emojis...')
            for emoji in server.emojis:
                # create a file name
                fileName = folderName + '\\' + emoji.name + '.png'
                # download if we dont already have it
                if not os.path.exists(fileName):
                    with open (fileName, 'wb') as outFile:
                        # send a different header because otherwise we get a 403
                        req = urllib.request.Request(emoji.url, headers={'User-Agent': 'Mozilla/5.0'})
                        data = urllib.request.urlopen(req).read()
                        outFile.write(data)

    print('All done!')
    await client.logout()

# if using 2FA on your account (like you should), use this client.run. to get
# your token, press CTRL+SHIFT+I in discord. Navigate to the 'Application' tab.
# Click the drop down for 'Local Storage' and select the item that opens up. At
# the bottom of the column labeled 'Key' there is a field that says token. your
# token is in the right column. obviously you should never share this with anyone
client.run('token', bot=False)

# if not using 2FA, use this version of client.run by commenting out the
# previous one with # and uncommenting this one by deleting the #. i hope you
# can figure out what to put in each field
#client.run('email', 'password')
