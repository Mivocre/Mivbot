import discord
from discord.ext import commands
from discord import app_commands
import os
botToken = os.environ.get("DISCORD_BOT_TOKEN")
linkAllowed = ["music", "slay-the-bot", "pics-links", "timeiscommunication", "valorant-money-maker"]
bannedWords = ["gamer", "gacha"]

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        try:
            guild = discord.Object(id=1349052725735850095)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
        except Exception as e:
            print(f'Error syncing commands: {e}')


    async def on_message(self, message):
        #stops bot from replying to itself
        if message.author == self.user:
            return
        # deletes messages containing banned words then names and shames message author for using banned word
        if any(word in message.content for word in bannedWords):
            await message.delete()
            await message.channel.send(f'bad {message.author.mention}, no banned words')

        # test to see if user is being grabbed properly
        # if message.content.startswith("hello"):
        #     await message.channel.send(f'Hi There {message.author}')
            # this line prints a list of attachments, if no attachments present the list will be empty
            # print(message.attachments)
            # this line prints a list of embedded links, if no links present the list will be empty
            # print(message.embeds)
        # deletes messages containing links or attachments from general, but not pics-links
        # if message.channel.name not in linkAllowed:
        #     if len(message.embeds) > 0:
        #         await message.delete()
        #         await message.channel.send("stop that, no links")
        #     if len(message.attachments) > 0:
        #         await message.delete()
        #         await message.channel.send("stop that, no attachments")
    # async def on_reaction_add(self, reaction, user):
    #     await reaction.message.channel.send("You Reacted")

intents = discord.Intents.default()
intents.message_content = True

client = Client(command_prefix="!", intents=intents)

GUILD_ID = discord.Object(id=1349052725735850095)

@client.tree.command(name="greeting", description="makes the bot greet you", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message(f'hello {interaction.user.mention}')

class View(discord.ui.View):
    @discord.ui.button(label="League", style=discord.ButtonStyle.red)
    async def league_button_callback(self, button, interaction):
        member = button.user
        role = discord.utils.get(member.guild.roles, name="League")
        await member.add_roles(role)
        await button.response.send_message(f'League role assigned to {member}', ephemeral=True)
    
    @discord.ui.button(label="ERBS", style=discord.ButtonStyle.green)
    async def erbs_button_callback(self, button, interaction):
        member = button.user
        role = discord.utils.get(member.guild.roles, name="ERBS")
        await member.add_roles(role)
        await button.response.send_message(f'ERBS role assigned to {member}', ephemeral=True)
        
    @discord.ui.button(label="DOTA", style=discord.ButtonStyle.blurple)
    async def dota_button_callback(self, button, interaction):
        member = button.user
        role = discord.utils.get(member.guild.roles, name="DOTA")
        await member.add_roles(role)
        await button.response.send_message(f'Dota role assigned to {member}', ephemeral=True)
        
    @discord.ui.button(label="Deadlock", style=discord.ButtonStyle.red)
    async def deadlock_button_callback(self, button, interaction):
        member = button.user
        role = discord.utils.get(member.guild.roles, name="Deadlock")
        await member.add_roles(role)
        await button.response.send_message(f'Deadlock role assigned to {member}', ephemeral=True)
        
    @discord.ui.button(label="Bapbap", style=discord.ButtonStyle.green)
    async def bapbap_button_callback(self, button, interaction):
        member = button.user
        role = discord.utils.get(member.guild.roles, name="Bapbap")
        await member.add_roles(role)
        await button.response.send_message(f'Bapbap role assigned to {member}', ephemeral=True)
        
    @discord.ui.button(label="Omega Strikers", style=discord.ButtonStyle.blurple)
    async def omegastrikers_button_callback(self, button, interaction):
        member = button.user
        role = discord.utils.get(member.guild.roles, name="Omega Strikers")
        await member.add_roles(role)
        await button.response.send_message(f'Omega Strikers role assigned to {member}', ephemeral=True)
        
    @discord.ui.button(label="Supervive", style=discord.ButtonStyle.red)
    async def supervive_button_callback(self, button, interaction):
        member = button.user
        role = discord.utils.get(member.guild.roles, name="SuperVive")
        await member.add_roles(role)
        await button.response.send_message(f'Supervive role assigned to {member}', ephemeral=True)
        
    @discord.ui.button(label="Touhou Big Big Battle", style=discord.ButtonStyle.green)
    async def touhoubbb_button_callback(self, button, interaction):
        member = button.user
        role = discord.utils.get(member.guild.roles, name="Touhou Big Big Battle")
        await member.add_roles(role)
        await button.response.send_message(f'Touhou Big Big Battle role assigned to {member}', ephemeral=True)
        
    @discord.ui.button(label="HOTS", style=discord.ButtonStyle.blurple)
    async def hots_button_callback(self, button, interaction):
        member = button.user
        role = discord.utils.get(member.guild.roles, name="HOTS")
        await member.add_roles(role)
        await button.response.send_message(f'HOTS role assigned to {member}', ephemeral=True)
    

@client.tree.command(name="mobaroles", description="display buttons to assign roles for LFG pings", guild=GUILD_ID)
async def MOBAMenu(interaction: discord.Interaction):
    await interaction.response.send_message(view=View(), ephemeral=True)


client.run(botToken)
