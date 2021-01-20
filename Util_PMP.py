from configClass import Config
import discord
import json


def readConfig():
    """
    Load user config
    """
    with open("config.json") as json_file:
        config = json.load(json_file)
        json_file.close()
        config = Config(**config)
        return config
config = readConfig()
        
        
def calculatePoint(listName):
    """
    Point system used to determine wether a card has moved up or down

    Args:
        cardName (STR): Name of the list that the card came from

    Returns:
        [type]: [description]
    """
    if listName in ["Backlog", "To Do"]:
        return 1

    elif listName in ["In Progress"]:
        return 2

    elif listName in ["Review/QA", "Review", "Review/Editing"]:
        return 3
    
    elif listName in ["Done" , "Ready for Implementation"]:
        return 4
    
    
def counter(boardName):
    """
    Main counter function used for calculations

    Args:
        boardName (STR): Name of Parent
    """
    if boardName == "WRITE_DONE":
        config.countW += 1
        config.countW_Done += 1
        
    elif boardName == "SOUND_DONE":
        config.countS += 1
        config.countS_Done += 1
        
    elif boardName == "ART_DONE":
        config.countA += 1
        config.countA_Done += 1
    
    elif boardName == "WRITE_P":
        config.countW += 1
        config.countW_P += 1
        
    elif boardName == "SOUND_P":
        config.countS += 1
        config.countS_P += 1
        
    elif boardName == "ART_P":
        config.countA += 1
        config.countA_P += 1
        
    
    
    