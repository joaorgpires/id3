from id3heur import *

def chooseAttr(attr, inst, clas, infoGain):
    bestGain = 0.0
    bestAttr = None
    
    for a in attr:
        #don't forget that attr has clas in it
        gain = infoGain(inst, a, clas)
        if gain > bestGain and a != clas:
            bestGain = gain
            bestAttr = a
    
    return bestAttr

def createDtree(attr, inst, clas):
    
