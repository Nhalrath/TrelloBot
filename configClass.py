from datetime import datetime, timedelta
from trello import TrelloClient
import pytz
           
class Config:
    
    def __init__(self, **entries):
        self.__dict__.update(entries)
        self.Trello = None
        self.executionTime = 80
        
        self.countW = 0  #Writer card counter
        self.countW_P = 0
        self.countW_TODO = 0
        self.countW_Done = 0  
        
        self.countA = 0  #Artist card counter
        self.countA_P = 0
        self.countA_TODO = 0
        self.countA_Done = 0  
        
        self.countS = 0  #Sound card counter
        self.countS_P = 0
        self.countS_TODO = 0
        self.countS_Done = 0
        
        self.reportExecute = False
        self.lastAction = None
        
        self.initTargetTime()
        
        self.targetTime = datetime(2021, 1, 20, hour=9, minute=55, second=0, microsecond=0, tzinfo=pytz.UTC)
        
    def clientTrello(self):
        """
        Initialise Trello client

        Returns:
            Trello (OBJ): Trello Client
        """
        
        return TrelloClient(api_key=self.apiK, api_secret=self.apiS)

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
        
        self.countW = 0  #Writer card counter
        self.countW_P = 0
        self.countW_TODO = 0
        self.countW_Done = 0  
        
        self.countA = 0  #Artist card counter
        self.countA_P = 0
        self.countA_TODO = 0
        self.countA_Done = 0  
        
        self.countS = 0  #Sound card counter
        self.countS_P = 0
        self.countS_TODO = 0
        self.countS_Done = 0  
    