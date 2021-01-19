from Util_Embed import performanceChart, cardCreated, cardMovedUp, cardOnHold, cardSkippedUp, cardErraticMove
from Util_PMP import calculatePoint, counter, config
from datetime import datetime, timedelta
from trello import TrelloClient
from discord.ext import tasks
import discord
import asyncio
import json
import pytz
import time

bot = discord.Client()

async def checkChange(aDict, card, channel):
    """
    Function determines the type of move a card has taken

    Args:
        aDict (DICT): Dictionary containing card information
        card (OBJ): Card object
    """
    author =  config.Trello.get_member(card.idMembers[0]).username if card.idMembers else "Unknown"

    if  aDict.get("destination").get("name") == "On Hold":
        await cardOnHold(card.name.upper(), channel, author)
    
    elif ((calculatePoint(aDict.get("destination").get("name")) - calculatePoint(aDict.get("source").get("name"))) == 1):
        await cardMovedUp(card.name.upper(), aDict.get('destination').get('name'), channel, author)
        
    elif ((calculatePoint(aDict.get("destination").get("name")) - calculatePoint(aDict.get("source").get("name"))) > 1):
        await cardSkippedUp(card.name.upper(), aDict.get('destination').get('name'), aDict.get("destination").get("name"), channel, author)
        
    else:
        await cardErraticMove(card.name.upper(), aDict.get("source").get("name"), aDict.get("destination").get("name"), channel, author)
    

async def checkCardMovement(listID, targetTime, parentName):
    """
    Checks the movement history of each card

    Args:
        listID (INT): Trello Board ID
    """
    for card in listID:
        last_move = card.list_movements() 
        counter(parentName)
        try:
            if (last_move[0].get('datetime').replace(tzinfo=pytz.UTC) > targetTime):
                await checkChange(last_move[0], card, bot.get_channel(config.channelID))

        except IndexError:
            None
        await asyncio.sleep(0.09)
        
        
async def checkCardCreation(listID, targetTime):
    """
    Checks the creation date of each card

    Args:
        listID (INT): Trello Board ID
    """
    for card in listID:
        if (card.created_date > targetTime):
            await cardCreated(card.name, bot.get_channel(config.channelID))
            
        await asyncio.sleep(0.09)
        

async def checkTrello(targetTime):
    """
    Main check function for trello cards

    Args:
        targetTime (datetime): Main time comparison used for calculation
    """
    config.resetCounter()
    for boardID, parentName in config.board_MVLS.items():
        await checkCardMovement((config.Trello.list_boards()[-1]).get_list(boardID).list_cards(), targetTime, parentName)

    for boardID in config.board_CTLS:
        await checkCardCreation((config.Trello.list_boards()[-1]).get_list(boardID).list_cards(), targetTime)


@tasks.loop()
async def checkTime():
    """
    Main Loop function used for capturing and saving time values used for comparisons
    """
    if (datetime.now(pytz.timezone("Etc/GMT+0")) > config.targetTime):
        await  performanceChart(bot.get_channel(config.channelID))
        config.targetTime += timedelta(hours = 24)
        
    elif (config.countW != 0 and config.reportExecute is True):
        await  performanceChart(bot.get_channel(config.channelID))
        config.reportExecute = False
        
    else:
        start_time = time.time()
        await checkTrello((datetime.now(pytz.timezone(config.timezone)) - timedelta(0,config.executionTime)).replace(tzinfo=pytz.UTC))
        result = (time.time() - start_time)
        config.executionTime = result
        print(f"#########->{result:.2f} seconds <-#########")
        
        
@bot.event
async def on_message(message):
    if message.content.startswith('!Report'):
        config.reportExecute = True
        await bot.get_channel(config.channelID).send("Request sent. The request could take a while, please be patient.")
                 

@bot.event
async def on_ready():
    """
    Function runs when bot is ready!
    """
    print("I`m Alive")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="with your feelings", description =''))
    checkTime.start()
    

bot.run(config.discordToken)
