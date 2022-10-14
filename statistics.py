import math

class mailNotification:
    def __init__(self, mailSent=True):
        self.mailSent = mailSent



   def notification():
        self.mailSent = True




class ledNotification:
    def __init__(self, ledGlows=True):
        self.ledGlows = ledGlows



   def notification():
        self.ledGlows = True



class statsNotification:
    def __init__(self, v1, v2):
        self.maxThreshold = v1
        self.list = v2



   def validateAndNotify(self, v):
        val = max(v)
        if val > self.maxThreshold:
            self.list[0].emailSent = True
            self.list[1].ledGlows = True
            
            
def calculateStats(numbers):
  computedStats = {}
  if len(numbers) == 0:
    computedStats["avg"] = math.nan
    computedStats["max"] = math.nan
    computedStats["min"] = math.nan
  else:
    computedStats["avg"] = sum(numbers)/len(numbers)
    computedStats["max"] = max(numbers)
    computedStats["min"] = min(numbers)
  return computedStats
