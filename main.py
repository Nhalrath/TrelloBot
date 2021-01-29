from Util_Embed import performanceChart, cardCreated, cardMovedUp, cardOnHold, cardSkippedUp, cardErraticMove, timeOutError
from Util_PMP import calculatePoint, counter, config
from datetime import datetime, timedelta
from trello import TrelloClient
from discord.ext import tasks
import asyncio
import discord
import json
import pytz
import time


async def checkCardMovement(listID, targetTime, parentName):
    """
    Checks the movement history of each card

    Args:
        listID (INT): Trello Board ID
    """
    for card in listID:
        last_move = card.list_movements() 
        counter(parentName)   
        await asyncio.sleep(0.09)
        
        
async def checkCardCreation(listID, targetTime):
    """
    Checks the creation date of each card

    Args:
        listID (INT): Trello Board ID
    """
    for card in listID:
        if (card.created_date > targetTime):
            await cardCreated(card.name, config.Bot.get_channel(config.channelID))
            
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


async def checkTime():
    """
    Main Loop function used for capturing and saving time values used for comparisons
    """
    if (datetime.now(pytz.timezone("Etc/GMT+0")) > config.targetTime):
        await  performanceChart(config.Bot.get_channel(config.channelID))
        config.targetTime += timedelta(hours = 24)
        
    elif (config.countW != 0 and config.reportExecute is True):
        await  performanceChart(config.Bot.get_channel(config.channelID))
        config.reportExecute = False
        
    else:
        start_time = time.time()
        await checkTrello((datetime.now(pytz.timezone(config.timezone)) - timedelta(0,config.executionTime)).replace(tzinfo=pytz.UTC))
        result = (time.time() - start_time)
        config.executionTime = result
        print(config)
        
        
@tasks.loop()
async def mainLoop():
    """
    Main loop function
    """
    try:
        await checkTime()
    
    except:
        timeOutError()


@config.Bot.event
async def on_message(message):
    if message.content.startswith('!Report'):
        config.reportExecute = True
        await config.Bot.get_channel(config.channelID).send("Request sent. The request could take a while, please be patient.")
                 

@config.Bot.event
async def on_ready():
    """
    Function runs when bot is ready!
    """
    print("Online")
    await config.Bot.change_presence(status=discord.Status.online, activity=discord.Game(name="with your feelings", description =''))
    mainLoop.start()

config.Bot.run(config.discordToken)
