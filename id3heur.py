import math

def entropy(inst, clas):
    #ex: for the restaurant example, clas is the string willWait
    #dictionary that will store absolute frequencies
    freq = {}
    entr = 0.0 #better work with floats since the very beggining so we won't screw up entropy calc
    
    for ins in inst:
        #if already found this answer, add 1.0
        if freq.has_key(ins[clas]):
            freq[ins[clas]] += 1.0
        else:            
            #if not, put the clas value in the dictionary with val 1.0
            freq[ins[clas]] = 1.0
    
    for f in freq.values():
        v = (f / len(inst))
        entr += (-v) * math.log(v, 2)
    
    return entr

def infoGain(inst, attry, clas):
    #if we split the data using attribute attry, this is the information gain we'll get
    freq = {}
    rest = 0.0
    
    for ins in inst:
        #if already found this answer, add 1.0
        if freq.has_key(ins[clas]):
            freq[ins[clas]] += 1.0
        else:            
            #if not, put the clas value in the dictionary with val 1.0
            freq[ins[clas]] = 1.0
    
    for f in freq.keys():
        prob = freq[f] / sum(freq.values())
        l = [ins for ins in inst if ins[attry] == val]
        rest += prob * entropy(l, clas)
    
    #gain = originalInfo - rest(attry)
    return entropy(inst, clas) - rest
