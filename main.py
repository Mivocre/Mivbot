import discord
import os

botToken = os.environ.get("DISCORD_BOT_TOKEN")
linkAllowed = ["pics-links"]

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        #stops bot from replying to itself
        if message.author == self.user:
            return
        if message.content.startswith("hello"):
            await message.channel.send(f'Hi There {message.author}')
            # this line returns a list of attachments, if no attachments present the list will be empty
            # print(message.attachments)
            # this line returns a list of embedded links, if no links present the list will be empty
            # print(message.embeds)
        if message.channel.name not in linkAllowed:
            if len(message.embeds) > 0:
                await message.delete()
                await message.channel.send("stop that, no links")
            if len(message.attachments) > 0:
                await message.delete()
                await message.channel.send("stop that, no attachments")
    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send("You Reacted")

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(botToken)
