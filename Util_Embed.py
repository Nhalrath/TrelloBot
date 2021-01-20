from datetime import datetime
from Util_PMP import config
import discord

async def performanceChart(channel = config.channelID_M):
    """
    Function uses discord embeds to send the daily report messages

    Args:
        channel (OBJ, optional): Discord object, for deciding channel location. Defaults to config.channelID_M.
    """
    embed = discord.Embed(title="Daily Management Report", colour=discord.Colour(0x3b91ff), url="https://discordapp.com", description=f"```asciidoc\n Date: {datetime.now().strftime('%m/%d/%Y')}\n------------------```")
    embed.set_image(url="https://media-exp1.licdn.com/dms/image/C4E1BAQFYaGosTkluEQ/company-background_10000/0/1564129197188?e=2159024400&v=beta&t=6itWEitI2AFnEOPK9kU4FgN2U2a8yUqLkiSH1NJ1xms")
    embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1334111535082446849/LdHGWkZq_400x400.jpg")
    embed.set_footer(text="We can do this! 👊", icon_url="https://pbs.twimg.com/profile_images/1334111535082446849/LdHGWkZq_400x400.jpg")
    await channel.send(embed=embed)
    
    ratio = (config.countW_Done)/(config.countW_P + config.countW_TODO + config.countW_Done)
    percent = round(ratio * 100 , 2)
    loaded = round(ratio * 20) * "#"
    unloaded = (20 - round(ratio * 20)) * "-"
    progressBar = '[' + loaded + unloaded + ']'
    string = f"```asciidoc\nBoard: Writing ({config.countW})\n----------------------\nOpen:: {config.countW_TODO}\nIn Progress:: {config.countW_P}\nDone:: {config.countW_Done}\nTotal Progress: {percent}%\n----------------------\n{progressBar}```"
    await channel.send(string)

    ratio = (config.countA_Done)/(config.countA_P + config.countA_TODO + config.countA_Done)
    percent = round(ratio * 100 , 2)
    loaded = round(ratio * 20) * "#"
    unloaded = (20 - round(ratio * 20)) * "-"
    progressBar = '[' + loaded + unloaded + ']'
    string = f"```asciidoc\nBoard: Art ({config.countA})\n----------------------\nOpen:: {config.countA_TODO}\nIn Progress:: {config.countA_P}\nDone:: {config.countA_Done}\nTotal Progress: {percent}%\n----------------------\n{progressBar}```"
    await channel.send(string)
    
    ratio = (config.countS_Done)/(config.countS_P + config.countS_TODO + config.countS_Done)
    percent = round(ratio * 100 , 2)
    loaded = round(ratio * 20) * "#"
    unloaded = (20 - round(ratio * 20)) * "-"
    progressBar = '[' + loaded + unloaded + ']'
    string = f"```asciidoc\nBoard: Sound ({config.countS})\n----------------------\nOpen:: {config.countS_TODO}\nIn Progress:: {config.countS_P}\nDone:: {config.countS_Done}\nTotal Progress: {percent}%\n----------------------\n{progressBar}```"
    await channel.send(string)
    

async def cardCreated(cardName, channel):
    """
    Discord embed send function using a specific embed style

    Args:
        cardName (STR): Name of a given card
        channel (OBJ): Discord channel object
    """
    if (config.lastAction != f"Card Created {cardName}"):
        embed = discord.Embed(title="🚨 WEE WOO WEE WOO 🚨", colour=discord.Colour(0x12e4ff), url="https://discordapp.com", description="```asciidoc\n[A NEW TODO HAS BEEN CREATED!]```")
        embed.set_image(url="https://thewhisp.mommyish.com/wp-content/uploads/2018/12/Spongebob-Mailbox.jpg")
        embed.set_thumbnail(url="https://simpleskincarescience.com/wp-content/uploads/2019/11/smiling-spongebob-fish-e1574132873854.jpg")
        embed.set_author(name="Postman Phat", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/app-icons/795966880779206656/8b6d6c8e089b7cd499435333dd3c0bf3.png?size=64")
        embed.set_footer(text="Do people even read this?", icon_url="https://pbs.twimg.com/profile_images/1334111535082446849/LdHGWkZq_400x400.jpg")
        embed.add_field(name=f"New ToDo - {cardName}", value="Visit trello for more information!", inline = False)
        config.lastAction = f"Card Created {cardName}"
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
    if (config.lastAction != f"Card MovedUP {cardName}"):
        embed = discord.Embed(title="🚨 WEE WOO WEE WOO 🚨", colour=discord.Colour(0x12e4ff), url="https://discordapp.com", description="```css\nWe need more people like you!\nYou're a star!💪🌟```")
        embed.set_image(url="https://i.ytimg.com/vi/oZw26clV1UI/maxresdefault.jpg")
        embed.set_thumbnail(url="https://fhr.fra1.cdn.digitaloceanspaces.com/NHLGamer/ECL/ECL_8/team_logos/Pro/ECL8%20Pro%20-%20Poggers.png")
        embed.set_author(name="Postman Phat", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/app-icons/795966880779206656/8b6d6c8e089b7cd499435333dd3c0bf3.png?size=64")
        embed.set_footer(text="Do people even read this?", icon_url="https://pbs.twimg.com/profile_images/1334111535082446849/LdHGWkZq_400x400.jpg")
        embed.add_field(name=f"{cardName} has advanced to {destination}!!!", value=f"Made by: {author}", inline = False)
        config.lastAction = f"Card MovedUP {cardName}"
        await channel.send(embed=embed)
        
    
async def cardOnHold(cardName, channel, author):
    """
    Discord embed send function using a specific embed style

    Args:
        cardName (STR): Name of card
        destination (STR): Name of a given distentation
        channel (OBJ): Discord channel object
        author (str, optional): Name of author. Defaults to "Unknown".
    """
    if (config.lastAction != f"Card OnHold {cardName}"):
        embed = discord.Embed(title="🚨 WEE WOO WEE WOO 🚨", colour=discord.Colour(0x12e4ff), url="https://discordapp.com", description="```css\n😥😥😥😥😥```")
        embed.set_image(url="https://i.imgflip.com/1o12mo.jpg")
        embed.set_thumbnail(url="https://img2.wikia.nocookie.net/__cb20130524235901/fakemon/es/images/3/39/Crying_Meme.png")
        embed.set_author(name="Postman Phat", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/app-icons/795966880779206656/8b6d6c8e089b7cd499435333dd3c0bf3.png?size=64")
        embed.set_footer(text="Do people even read this?", icon_url="https://pbs.twimg.com/profile_images/1334111535082446849/LdHGWkZq_400x400.jpg")
        embed.add_field(name=f"{cardName} has been put on hold!", value=f"Made by: {author}", inline = False)
        config.lastAction = f"Card OnHold {cardName}"
        await channel.send(embed=embed)
        
        
async def cardSkippedUp(cardName, source, destination, channel, author):
    """
    Discord embed send function using a specific embed style

    Args:
        cardName (STR): Name of card
        destination (STR): Name of a given distentation
        channel (OBJ): Discord channel object
        author (str, optional): Name of author. Defaults to "Unknown".
    """ 
    if (config.lastAction != f"Card SkippedUP {cardName}"):
        embed = discord.Embed(title="🚨 WEE WOO WEE WOO 🚨", colour=discord.Colour(0x12e4ff), url="https://discordapp.com", description="```css\nIt skipped a few steps.....\nWe need more people like you!\nYou're a star!💪🌟```")
        embed.set_image(url="https://i.ytimg.com/vi/oZw26clV1UI/maxresdefault.jpg")
        embed.set_thumbnail(url="https://fhr.fra1.cdn.digitaloceanspaces.com/NHLGamer/ECL/ECL_8/team_logos/Pro/ECL8%20Pro%20-%20Poggers.png")
        embed.set_author(name="Postman Phat", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/app-icons/795966880779206656/8b6d6c8e089b7cd499435333dd3c0bf3.png?size=64")
        embed.set_footer(text="Do people even read this?", icon_url="https://pbs.twimg.com/profile_images/1334111535082446849/LdHGWkZq_400x400.jpg")
        embed.add_field(name=f"{cardName} has advanced to {destination}!!!", value=f"Made by: {author}", inline = False)
        config.lastAction = f"Card SkippedUP {cardName}"
        await channel.send(embed=embed)


async def cardErraticMove(cardName, source, destination, channel, author):
    """
    Discord embed send function using a specific embed style

    Args:
        cardName (STR): Name of a given card
        destination (STR): Name of a given distentation
        channel (OBJ): Discord channel object
        author (str, optional): Name of author. Defaults to "Unknown".
    """
    if (config.lastAction != f"Card ErraticMove {cardName}"):
        embed = discord.Embed(title="🚨 Card Moved Erratically..EHH?! 🚨", colour=discord.Colour(0x12e4ff), url="https://discordapp.com", description="```asciidoc\n[That wasn't suppose to happen...]```")
        embed.set_image(url="https://www.centralfloridapost.com/wp-content/uploads/2020/06/flat1000x1000075f.u1.jpg")
        embed.set_thumbnail(url="https://external-preview.redd.it/u08WRG2L8S9j8BDgmn9kHTQy4bqN1v_dj3KlUiYDJKU.jpg?auto=webp&s=860bd654a0b30fa4582ea84cc5087ed7d3286928")
        embed.set_author(name="Postman Phat", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/app-icons/795966880779206656/8b6d6c8e089b7cd499435333dd3c0bf3.png?size=64")
        embed.set_footer(text="Do people even read this?", icon_url="https://pbs.twimg.com/profile_images/1334111535082446849/LdHGWkZq_400x400.jpg")
        embed.add_field(name=f"Card moved from '{source}' to '{destination}'", value=f"{cardName} - {author}", inline = False)
        config.lastAction = f"Card ErraticMove {cardName}"
        await channel.send(embed=embed)
