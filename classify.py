def getClas(ins, tree):
    if(type(tree) == str):
        return tree
    
    else:
        attr = tree.keys()[0]
        t = tree[attr][ins[attr]]
        return getClas(ins, t)

def classify(inst, tree):
    clas = []
    
    for ins in inst:
        clas.append(getClas(ins, tree))
        
    return clas
