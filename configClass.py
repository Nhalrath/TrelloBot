from trello import TrelloClient
from datetime import datetime, timedelta
import pytz
           
class Config:
    
    def __init__(self, **entries):
        self.__dict__.update(entries)
        
        self.Trello = None
        self.executionTime = 80
        self.dailyExecution = False
        
        self.countW = 0  #Writer card counter
        self.countW_TODO = 0
        self.countW_P = 0
        self.countW_Done = 0  
        
        self.countA = 0  #Artist card counter
        self.countA_TODO = 0
        self.countA_P = 0
        self.countA_Done = 0  
        
        self.countS = 0  #Sound card counter
        self.countS_TODO = 0
        self.countS_P = 0
        self.countS_Done = 0  
        
        #self.targetTime = datetime(2021, 1, 18, hour=9, minute=55, second=0, microsecond=0, tzinfo=pytz.UTC)
        self.targetTime = targetTime = datetime.now(pytz.timezone("Etc/GMT+0")) + timedelta(0,10)
        
    def clientTrello(self):
        return TrelloClient(api_key=self.apiK, api_secret=self.apiS)
    
    def __repr__(self):
        print("Config Object")
    
    def __str__(self):
        print(self)
        