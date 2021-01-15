import discord
import json

lastAction = None

def readConfig():
    """
    Load user config
    """
    with open("config.json") as json_file:
        config = json.load(json_file)
        json_file.close()
        return config

config = readConfig()

async def cardCreated(cardName, channel):
    """
    Discord embed send function using a specific embed style

    Args:
        cardName (STR): Name of a given card
        channel (OBJ): Discord channel object
    """
    global lastAction

    if (lastAction != f"Card Created {cardName}"):
        embed = discord.Embed(title="A title", colour=discord.Colour(0x12e4ff), url="https://discordapp.com", description="```A description```")
        embed.set_image(url="https://i.imgur.com/ST5Q7hj.png")
        embed.set_thumbnail(url="https://i.imgur.com/ST5Q7hj.png")
        embed.set_author(name="Bot Name", url="https://discordapp.com", icon_url="https://i.imgur.com/ST5Q7hj.png")
        embed.set_footer(text="A footer", icon_url="https://i.imgur.com/ST5Q7hj.png")
        embed.add_field(name=f"A name", value="Some value", inline = False)
        lastAction = f"Card Created {cardName}"
        await channel.send(embed=embed)

async def cardMovedUp(cardName, destination, channel, author):
    """
    Discord embed send function using a specific embed style

    Args:
        cardName (STR): Name of a given card
        destination (STR): Name of a given distentation
        channel (OBJ): Discord channel object
        author (str, optional): Name of author. Defaults to "Unknown".
    """
    global lastAction
    
    if (lastAction != f"Card MovedUP {cardName}"):
        embed = discord.Embed(title="A title", colour=discord.Colour(0x12e4ff), url="https://discordapp.com", description="```A description```")
        embed.set_image(url="https://i.imgur.com/ST5Q7hj.png")
        embed.set_thumbnail(url="https://i.imgur.com/ST5Q7hj.png")
        embed.set_author(name="Bot Name", url="https://discordapp.com", icon_url="https://i.imgur.com/ST5Q7hj.png")
        embed.set_footer(text="A footer", icon_url="https://i.imgur.com/ST5Q7hj.png")
        embed.add_field(name=f"A name", value="Some value", inline = False)
        lastAction = f"Card MovedUP {cardName}"
        await channel.send(embed=embed)


async def cardErraticMove (cardName, source, destination, channel, author):
    """
    Discord embed send function using a specific embed style

    Args:
        cardName (STR): Name of a given card
        destination (STR): Name of a given distentation
        channel (OBJ): Discord channel object
        author (str, optional): Name of author. Defaults to "Unknown".
    """
    global lastAction

    if (lastAction != f"Card ErraticMove {cardName}"):
        embed = discord.Embed(title="A title", colour=discord.Colour(0x12e4ff), url="https://discordapp.com", description="```A description```")
        embed.set_image(url="https://i.imgur.com/ST5Q7hj.png")
        embed.set_thumbnail(url="https://i.imgur.com/ST5Q7hj.png")
        embed.set_author(name="Bot Name", url="https://discordapp.com", icon_url="https://i.imgur.com/ST5Q7hj.png")
        embed.set_footer(text="A footer", icon_url="https://i.imgur.com/ST5Q7hj.png")
        embed.add_field(name=f"A name", value="Some value", inline = False)
        lastAction = f"Card ErraticMove {cardName}"
        await channel.send(embed=embed)

async def defaultCardMove(cardName, source, destination, channel, author):
    """
    Default discord embed send function using a specific embed style

    Args:
        cardName (STR): Name of a given card
        destination (STR): Name of a given distentation
        channel (OBJ): Discord channel object
        author (str, optional): Name of author. Defaults to "Unknown".
    """
    global lastAction

    if (lastAction != f"Default Move {cardName}"):
        embed = discord.Embed(title="A title", colour=discord.Colour(0x12e4ff), url="https://discordapp.com", description="```A description```")
        embed.set_image(url="https://i.imgur.com/ST5Q7hj.png")
        embed.set_thumbnail(url="https://i.imgur.com/ST5Q7hj.png")
        embed.set_author(name="Bot Name", url="https://discordapp.com", icon_url="https://i.imgur.com/ST5Q7hj.png")
        embed.set_footer(text="A footer", icon_url="https://i.imgur.com/ST5Q7hj.png")
        embed.add_field(name=f"A name", value="Some value", inline = False)
        lastAction = f"Default Move {cardName}"
        await channel.send(embed=embed)