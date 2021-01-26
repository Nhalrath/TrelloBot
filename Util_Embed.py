from datetime import datetime
from Util_PMP import config
import discord


async def timeOutError(date, channel):
    """
    Function uses discord embeds to send the an error report

    Args:
        date (STR): Name of card
        channel (OBJ): Discord channel object
        
    Example:
    
          Statistics
    ----------------------
    Runtime(Ave):: 53.5s
    Iterations:: 2047
    Raised Errors:: 1

    API Usage: 22.2%
    ----------------------
    [####----------------]
    """
                 
    embed = discord.Embed(title="🚨 Timeout Error 🚨", colour=discord.Colour(0x12e4ff), url="https://discordapp.com")
    embed.set_image(url="")
    embed.set_thumbnail(url="")
    embed.set_author(name="Name", url="", icon_url="")
    embed.set_footer(text="", icon_url="")
    embed.add_field(name=f"", value=f"", inline = False)
    await channel.send(embed=embed)
    

    ratio = (config.totalCallCount)/(config.executionTime * 30)
    progressBar = '[' + (round(ratio * 20) * "#") + ((20 - round(ratio * 20)) * "-") + ']'
    string = f"```asciidoc\n      Statistics\n----------------------\nRuntime(Ave):: {config.executionTime:.1f}s\nItererations:: {config.iterationCounter}\nRaised Errors:: {config.nErrors}\n   API Usage: {percent}%\n----------------------\n{progressBar}```"
    await channel.send(string)
    
    
async def performanceChart(channel = config.channelID_M):
    """
    Function uses discord embeds to send the daily report messages

    Args:
        channel (OBJ, optional): Discord object, for deciding channel location. Defaults to config.channelID_M.
        
        
    Example:
    
     Board: Writing (184)
    ----------------------
    Open:: 136
    In Progress:: 28
    Done:: 20
    Total Progress: 10.87%
    ----------------------
    [##------------------]
    """
    embed = discord.Embed(title="Daily Management Report", colour=discord.Colour(0x3b91ff), url="https://discordapp.com", description=f"```asciidoc\n Date: {datetime.now().strftime('%m/%d/%Y')}\n------------------```")
    embed.set_image(url="")
    embed.set_thumbnail(url="")
    embed.set_footer(text="We can do this! 👊", icon_url="")
    await channel.send(embed=embed)
    
    ratio = (config.countW_Done)/(config.countW_P + config.countW_TODO + config.countW_Done)
    progressBar = '[' + (round(ratio * 20) * "#") + ((20 - round(ratio * 20)) * "-") + ']'
    string = f"```asciidoc\nBoard: Writing ({config.countW})\n----------------------\nOpen:: {config.countW_TODO}\nIn Progress:: {config.countW_P}\nDone:: {config.countW_Done}\nTotal Progress: {percent}%\n----------------------\n{progressBar}```"
    await channel.send(string)

    ratio = (config.countA_Done)/(config.countA_P + config.countA_TODO + config.countA_Done)
    percent = round(ratio * 100 , 2)
    progressBar = '[' + (round(ratio * 20) * "#") + ((20 - round(ratio * 20)) * "-") + ']'
    string = f"```asciidoc\nBoard: Art ({config.countA})\n----------------------\nOpen:: {config.countA_TODO}\nIn Progress:: {config.countA_P}\nDone:: {config.countA_Done}\nTotal Progress: {percent}%\n----------------------\n{progressBar}```"
    await channel.send(string)
    
    ratio = (config.countS_Done)/(config.countS_P + config.countS_TODO + config.countS_Done)
    progressBar = '[' + (round(ratio * 20) * "#") + ((20 - round(ratio * 20)) * "-") + ']'
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
        embed.set_image(url="")
        embed.set_thumbnail(url="")
        embed.set_author(name="", url="")
        embed.set_footer(text="", icon_url="")
        embed.add_field(name=f"", value="", inline = False)
        config.lastAction = f""
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
        embed.set_image(url="")
        embed.set_thumbnail(url="")
        embed.set_author(name="", url="", icon_url="")
        embed.set_footer(text="", icon_url="")
        embed.add_field(name=f"", value=f"", inline = False)
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
        embed.set_image(url="")
        embed.set_thumbnail(url="")
        embed.set_author(name="", url="", icon_url="")
        embed.set_footer(text="", icon_url="")
        embed.add_field(name=f"", value=f"", inline = False)
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
        embed.set_image(url="")
        embed.set_thumbnail(url="")
        embed.set_author(name="", url="", icon_url="")
        embed.set_footer(text="", icon_url="")
        embed.add_field(name=f"", value=f"", inline = False)
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
        embed.set_image(url="")
        embed.set_thumbnail(url="")
        embed.set_author(name="", url="", icon_url="")
        embed.set_footer(text="", icon_url="")
        embed.add_field(name=f"", inline = False)
        config.lastAction = f""
        await channel.send(embed=embed)
