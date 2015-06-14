from dtree import *
import sys
import os.path

def fExists(fname):
    if os.path.isfile(fname):
        return True
    else:
        print "Error: The file %s does not exist or can not be opened." % fname
        return False

def readData(fname):
    with open(fname, 'r') as fin:
        lines = [line.rstrip() for line in fin.readlines()]
    attr = [i.strip() for i in lines[0].split(',')][1:]
    inst = []
    cls = attr[-1]
    
    for line in lines[1:]:
        inst.append(dict(zip(attr, [i.strip() for i in line.split(',')][1:])))
    
    return attr, inst, cls

def readInstClasify(line, attr):
    line = [item.strip() for item in line.split(',')]
    return [(line[i], attr[i]) for i in range(len(line))]

def readClas(fname, attr):
    inst = []
    with open(fname, 'r') as fin:
        lines = [line.rstrip() for line in fin.readlines()]

    for line in lines[1:]:
        a = readInstClasify(line, attr)
        inst.append(a)
    
    return inst

if __name__ == "__main__":
    #print "ok", len(sys.argv)
    if len(sys.argv) == 2:
        ftrain = sys.argv[1]
        if(not fExists(ftrain)):
            sys.exit(0)
        attr, inst, clas = readData(ftrain)
        #print [ins[cls] for ins in inst]
        dtree = createDtree(attr, inst, clas)

    elif len(sys.argv) == 3:
        ftrain = sys.argv[1]
        ftest = sys.argv[2]
        if((not fExists(ftrain)) or (not fExists(ftest))):
            sys.exit(0)
        attr, inst, clas = readData(ftrain)
        classif = readClas(ftest, attr)
        dtree = createDtree(attr, inst, clas)

    else:
        print "Just a little helper:\nArguments needed. If you want to both train and test, give me both files, in that order.\nOtherwise, just give me the training file."
        sys.exit(0)
