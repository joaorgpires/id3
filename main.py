from dtree import *
from classify import *
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

def readClas(fname, attr):
    with open(fname, 'r') as fin:
        lines = [line.rstrip() for line in fin.readlines()]
    
    testInst = []
    
    for line in lines:
        testInst.append(dict(zip(attr, [i.strip() for i in line.split(',')])))

    return testInst

def printTree(tree, str):
    if type(tree) == dict:
        print "%s<%s>" % (str, tree.keys()[0])
        for node in tree.values()[0].keys():
            print "%s\t%s:" % (str, node)
            printTree(tree.values()[0][node], str + "\t\t")
    else:
        print "%sClass: %s" % (str, tree)

if __name__ == "__main__":
    #print "ok", len(sys.argv)
    if len(sys.argv) == 2:
        ftrain = sys.argv[1]
        if(not fExists(ftrain)):
            sys.exit(0)
        attr, inst, clas = readData(ftrain)
        #print [ins[cls] for ins in inst]
        dtree = createDtree(attr, inst, clas)
        printTree(dtree, "")
        #print attr, inst, clas
        #print dtree

    elif len(sys.argv) == 3:
        ftrain = sys.argv[1]
        ftest = sys.argv[2]
        if((not fExists(ftrain)) or (not fExists(ftest))):
            sys.exit(0)
        attr, inst, clas = readData(ftrain)
        classif = readClas(ftest, attr)
        dtree = createDtree(attr, inst, clas)
        printTree(dtree, "")
        testRes = classify(classif, dtree)
        for i in range(len(testRes)):
            print "Test case %d: %s" % (i + 1, testRes[i])

    else:
        print "Just a little helper:\n\t- Arguments needed. If you want to both train and test, give me both files, in that order.\n\t- Otherwise, just give me the training file."
        sys.exit(0)
