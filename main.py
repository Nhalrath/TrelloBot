from trello import TrelloClient
from datetime import datetime, timedelta
from Util_PMP import cardCreated, cardMovedUp, config, cardErraticMove
from discord.ext import tasks
import pytz
import time
import discord
import asyncio

bot = discord.Client()
bot.executionTime = 80
bot.clientTrello = TrelloClient(api_key=config.get("API key"), api_secret=config.get("API secret"))

async def checkChange(aDict, card, channel):
    """
    Function checks if move history is forward

    Args:
        aDict (DICT): Dictionary containing card information
        card (OBJ): Card object
    """
    author =  bot.clientTrello.get_member(card.idMembers[0]).username if card.idMembers else "Unknown"

    if (aDict.get('source').get('name') == "In Progress" and aDict.get('destination').get('name') in ["Review/Editing", "Review", "Review/QA"]):
        await cardMovedUp(card.name.upper(), aDict.get('destination').get('name'), channel, author)

    elif (aDict.get('source').get('name') in ["Review/Editing", "Review", "Review/QA"] and aDict.get('destination').get('name') == "Done"):
        await cardMovedUp(card.name.upper(), aDict.get('destination').get('name'), channel, author)

    else:
        await cardErraticMove(card.name, aDict.get('source').get('name'), aDict.get('destination').get('name'), channel, author)


async def checkCardMovement(listID, targetTime):
    """
    Checks the movement history of each card

    Args:
        listID (INT): Trello Board ID
    """
    for card in listID:
        last_move = card.list_movements() 
        try:
            if (last_move[0].get('datetime').replace(tzinfo=pytz.UTC) > targetTime):
                await checkChange(last_move[0], card, bot.get_channel(config.get("Channel ID")))

        except IndexError:
            pass

        
async def checkCardCreation(listID, targetTime):
    """
    Checks the creation date of each card

    Args:
        listID (INT): Trello Board ID
    """
    for card in listID:

        if (card.created_date > targetTime):
            await cardCreated(card.name, bot.get_channel(config.get("Channel ID")))
            
        await asyncio.sleep(0.05)


async def checkTrello(targetTime):
    """
    Main check function for trello cards

    Args:
        targetTime (datetime): Main time comparison used for calculation
    """
    for boardID in config.get("Boards MVLS"):
        await checkCardMovement((bot.clientTrello.list_boards()[-1]).get_list(boardID).list_cards(), targetTime)

    for boardID in config.get("Boards CTLS"):
        await checkCardCreation((bot.clientTrello.list_boards()[-1]).get_list(boardID).list_cards(), targetTime)


@tasks.loop()
async def checkTime():
    """
    Main Loop function during time comparisons
    """
    start_time = time.time()
    await checkTrello((datetime.now(pytz.timezone(config.get("Time Zone"))) - timedelta(0,bot.executionTime)).replace(tzinfo=pytz.UTC))
    result = (time.time() - start_time)
    bot.executionTime = result


@bot.event
async def on_ready():
    """
    Function runs when bot is ready!
    """
    print("Bot is live!")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="with your feelings", description =''))
    checkTime.start()
    

bot.run(config.get("Token"))
