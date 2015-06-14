from id3heur import *
#import collections for defaultdict, a high-performance container datatype that is usefull for representing the tree
import collections

def chooseBest(attr, inst, clas):
    inst = inst[:]
    bestGain = 0.0
    bestAttr = None
    
    for a in attr:
        #don't forget that attr has clas in it
        #print inst
        gain = infoGain(inst, a, clas)
        if gain > bestGain and a != clas:
            bestGain = gain
            bestAttr = a
    
    return bestAttr

def majVal(inst, clas):
    inst = inst[:]
    return majFreq([ins[clas] for ins in inst])

def majFreq(val):
    val = val[:]
    bestFreq = 0
    best = None
    
    for v in val:
        if(val.count(v) > bestFreq):
            best = v
            bestFreq = val.count(v)
    
    return best

def uniq(inp):
    inp = inp[:]
    outp = []
    for x in inp:
        if x not in outp:
            outp.append(x)
    return outp

def getVals(inst, best):
    inst = inst[:]
    return uniq([l[best] for l in inst])

def getInst(inst, best, val):
    inst = inst[:]
    ans = []
    if not inst:
        return ans
    else:
        l = inst.pop()
        if l[best] == val:
            ans.append(l)
            ans.extend(getInst(inst, best, val))
            return ans

        else:
            ans.extend(getInst(inst, best, val))
            return ans

def createDtree(attr, inst, clas):
    inst = inst[:]
    vals = [ins[clas] for ins in inst]
    default = majVal(inst, clas)
    
    #if inst empty or no more attr
    if(not inst or (len(attr) - 1 <= 0)):
        #don't forget that attr has clas in it
        return default

    #if all the instances have the same clas, return that
    elif vals.count(vals[0]) == len(vals):
        return vals[0]
    
    else:
        #lets create a new decision tree
        best = chooseBest(attr, inst, clas)
        tree = {best:collections.defaultdict()}
        
        #create subtree for each value in best attribute
        for val in getVals(inst, best):
            subtree = createDtree([a for a in attr if a != best], getInst(inst, best, val), clas)
            tree[best][val] = subtree
    
    return tree
