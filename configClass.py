from datetime import datetime, timedelta
from trello import TrelloClient
import discord
import pytz
           
class Config:
    """
    [summary]
    """
    
    def __init__(self, **entries):
        """
        [summary]
        """
        self.__dict__.update(entries)
        self.Trello = TrelloClient(api_key=self.apiK, api_secret=self.apiS)
        self.Bot = discord.Client()
        
        self.countW_P = 0
        self.countW_TODO = 0
        self.countW_Done = 0  
        
        self.countA_P = 0
        self.countA_TODO = 0
        self.countA_Done = 0  
        
        self.countS_P = 0
        self.countS_TODO = 0
        self.countS_Done = 0
        
        self.reportExecute = False
        self.executionTime = 80
        self.lastAction = None
        self.targetTime = None        
        self.initTargetTime()


    def initTargetTime(self):
        """
        Function sets the targetTime for GMT+0 8:00 AM
        """
        nowGMT0 = datetime.now(pytz.timezone("Etc/GMT+0"))
        if (nowGMT0.hour >= 8):
            self.targetTime = nowGMT0 + timedelta(hours = (24 - nowGMT0.hour) + 8)
            print("Report set for:", self.targetTime)
        else:
            self.targetTime = nowGMT0 + timedelta(hours = (8 - nowGMT0.hour))
            print("Report set for:", self.targetTime)    
    

    def resetCounter(self):
        """
        Resets all counters
        """       
        self.countW_P = 0
        self.countW_TODO = 0
        self.countW_Done = 0  
        
        self.countA_P = 0
        self.countA_TODO = 0
        self.countA_Done = 0  
        
        self.countS_P = 0
        self.countS_TODO = 0
        self.countS_Done = 0  
        
    def __str__(self):
        print(f"#########->{executionTime:.2f} seconds <-#########")
