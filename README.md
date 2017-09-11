## 💩 emoji-dumper 💩
This is a very simple Discord self-bot for saving the emojis of the servers you are on.

The only required library is [discord.py].

To run the bot execute the following in your terminal of choice:
```bash
python emojibot.py [token]
    - or -
python emojibot.py [email] [password]
```

If using 2FA on your account (like you should), use the first option. To get
your token, press CTRL+SHIFT+I in Discord. Navigate to the 'Application' tab.
Click the drop down for 'Local Storage' and select the item that opens up. At
the bottom of the column labeled 'Key' there is a field that says token. Your
token is in the right column. Obviously you should never share this with anyone.
See the image below for clarification.

![Token Location](https://github.com/qwertyboy/emoji-dumper/raw/master/images/token.png)

If not using 2FA, use the second option. You can probably figure out what to put
in each field.

The bot will log in as you and go through each server you are in that has emotes
and download each one. They are stored in the directory you ran the bot from
under `Emojis\Server Name`.


[discord.py]: https://github.com/Rapptz/discord.py
