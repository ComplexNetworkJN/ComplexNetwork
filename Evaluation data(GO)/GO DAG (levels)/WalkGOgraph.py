#!/usr/local/bin/python2.3

### USAGE:
# ./WalkGograph.py --level l <go_dag_file.txt>
#

import re, sys, os, string, math, fileinput
import sets, getopt, popen2, tempfile, copy

def getOptionsAndInput():
    usageStr = """./WalkGograph.py --level K [<go_dag_file.txt>]
    read the GO dag file and extract, for each element, it's level K
    ancestor is returned. If the node is higher than level K, then the node
    itself is returned.

    The input file's default location is
    /scratch/rsingh/work/phylo-networks/data/go-seq/go-dag.txt
    """
    
    (opts, args) = getopt.getopt(sys.argv[1:], "h", ["help",
                                                     "level="])

    infile = "go-dag.txt"
    level = 4
    for o,a in opts:
        if o in ["-h", "--help"] or len(args)> 1:
            print usageStr
            sys.exit(1)
        if o in ["--level"]:
            level = int(a.strip())
    
    if len(args) > 0:        
        infile = args[0]
        
    return (infile, level)





def readGOdagFile(fname):
    goids = sets.Set()
    fh = open(fname,'r')
    for line in fh:
        x = [a.strip() for a in line.split()]
        goids.update(x)
    fh.close()
    
    goid2children = dict([(a,sets.Set()) for a in goids])
    goid2parents = dict([(a,sets.Set()) for a in goids])

    fh = open(fname,'r')
    for line in fh:
        x = [a.strip() for a in line.split()]
        id = x[0]
        children = x[1:]
        
        goid2children[id].update(children)
        for childId in children:
            goid2parents[childId].add(id)

    return (goid2parents, goid2children, goids)




def getRoot(node, goid2parents):
    seenSet = sets.Set()
    currSet = [node]
    roots = sets.Set()
    while len(currSet) >0:
        id = currSet.pop()
        seenSet.add(id)
        parents = goid2parents[id]
        if len(parents) == 0:
            roots.add(id)
        else:
            for parentId in parents:
                if parentId not in seenSet:
                    currSet.append(parentId)
    #assert len(roots) == 1
    #x = list(roots)
    #return x[0]

    return roots


def getLevelKnodes(K, goid2parents, goid2children):
    rootNodes = sets.Set()
    for node in goid2parents:
        rootNodes.update(getRoot(node, goid2parents))

    levelKnodes = sets.Set()
    for node in rootNodes:
        seenSet = sets.Set()
        currSet = sets.Set([node])
        for i in range(K):
            thisSet = sets.Set()
            for a in currSet:
                thisSet.update(goid2children[a])
                
            currSet = thisSet - seenSet
            seenSet = currSet | seenSet
            
        levelKnodes.update(currSet)
                                
    return levelKnodes





def getAncestors(goid, goid2parents, goid2children):
    ancestors = sets.Set()
    currStack = [goid]
    while len(currStack) > 0:
        id = currStack.pop()
        ancestors.add(id)
        parents = goid2parents[id]
        for parentId in parents:
            if parentId not in ancestors:
                currStack.append(parentId)

    return ancestors
    



#################################################
if __name__ == "__main__":
    (infile, level) = getOptionsAndInput()
    (goid2parents, goid2children, goids) = readGOdagFile(infile)

    #print level
    #print goid2parents
    #print goid2children
    levelKnodes = getLevelKnodes(level, goid2parents, goid2children)
    outfile = infile + ".level" + str(level) + ".txt"
    f = open(outfile, 'w')

    for goid in goids:
        ancestors = getAncestors(goid, goid2parents, goid2children)
        x = levelKnodes & ancestors
        f.write(goid +" "+ string.join(x," ")+"\n")

