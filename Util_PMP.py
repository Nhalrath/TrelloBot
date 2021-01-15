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

    if (lastAction != 1):
        embed = discord.Embed(title="🚨 WEE WOO WEE WOO 🚨", colour=discord.Colour(0x12e4ff), url="https://discordapp.com", description="```asciidoc\n[A NEW TODO HAS BEEN CREATED!]```")
        embed.set_image(url="https://thewhisp.mommyish.com/wp-content/uploads/2018/12/Spongebob-Mailbox.jpg")
        embed.set_thumbnail(url="https://simpleskincarescience.com/wp-content/uploads/2019/11/smiling-spongebob-fish-e1574132873854.jpg")
        embed.set_author(name="Postman Phat", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/app-icons/795966880779206656/8b6d6c8e089b7cd499435333dd3c0bf3.png?size=64")
        embed.set_footer(text="Do people even read this?", icon_url="https://pbs.twimg.com/profile_images/1334111535082446849/LdHGWkZq_400x400.jpg")
        embed.add_field(name=f"New ToDo - {cardName}", value="Visit trello for more information!", inline = False)
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
    
    if (lastAction != 2):
        embed = discord.Embed(title="🚨 WEE WOO WEE WOO 🚨", colour=discord.Colour(0x12e4ff), url="https://discordapp.com", description="```css\nWe need more people like you!\nYou're a star!💪🌟```")
        embed.set_image(url="https://i.ytimg.com/vi/oZw26clV1UI/maxresdefault.jpg")
        embed.set_thumbnail(url="https://fhr.fra1.cdn.digitaloceanspaces.com/NHLGamer/ECL/ECL_8/team_logos/Pro/ECL8%20Pro%20-%20Poggers.png")
        embed.set_author(name="Postman Phat", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/app-icons/795966880779206656/8b6d6c8e089b7cd499435333dd3c0bf3.png?size=64")
        embed.set_footer(text="Do people even read this?", icon_url="https://pbs.twimg.com/profile_images/1334111535082446849/LdHGWkZq_400x400.jpg")
        embed.add_field(name=f"{cardName} has advanced to {destination}!!!", value=f"Made by: {author}", inline = False)
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
    if (lastAction != 3):
        embed = discord.Embed(title="🚨 Card Moved Erratically..EHH?! 🚨", colour=discord.Colour(0x12e4ff), url="https://discordapp.com", description="```asciidoc\n[That wasn't suppose to happen...]```")
        embed.set_image(url="https://www.centralfloridapost.com/wp-content/uploads/2020/06/flat1000x1000075f.u1.jpg")
        embed.set_thumbnail(url="https://external-preview.redd.it/u08WRG2L8S9j8BDgmn9kHTQy4bqN1v_dj3KlUiYDJKU.jpg?auto=webp&s=860bd654a0b30fa4582ea84cc5087ed7d3286928")
        embed.set_author(name="Postman Phat", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/app-icons/795966880779206656/8b6d6c8e089b7cd499435333dd3c0bf3.png?size=64")
        embed.set_footer(text="Do people even read this?", icon_url="https://pbs.twimg.com/profile_images/1334111535082446849/LdHGWkZq_400x400.jpg")
        embed.add_field(name=f"Card moved from '{source}' to '{destination}'", value=f"{cardName} - {author}", inline = False)
        lastAction = f"Card ErraticMove {cardName}"
        await channel.send(embed=embed)