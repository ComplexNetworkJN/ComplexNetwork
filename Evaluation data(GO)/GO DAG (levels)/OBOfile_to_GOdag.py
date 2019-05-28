#!/usr/bin/env python

### USAGE:
# ./OBOfile_to_GOdag.py <obo-file>

import re, sys, os, string, math, fileinput
import sets, getopt, popen2, tempfile, copy

def getOptionsAndInput():
    usageStr = "./OBOfile_to_GOdag <obo-file>"
    (opts, args) = getopt.getopt(sys.argv[1:], "h", ["help"])

    oboFile = ""
    for o,a in opts:
        if o in ["-h", "--help"] or len(args) != 1:
            print usageStr
            sys.exit(1)
            
    oboFile = args[0]
    return oboFile



def processCurrBlock(lines, goid2children):
    if len(lines)==0 or lines[0].strip() != "[Term]":
        return
    idline = [a.strip() for a in lines[1].split()]
    assert idline[0] == "id:"
    id = idline[1]
    
    seenIS_A = False
    for line in lines[2:]:
        x = [a.strip() for a in line.split()]
        if len(x) > 1 and x[0]=="is_a:":
            seenIS_A = True
            parentId = x[1]
            if parentId not in goid2children:
                goid2children[parentId] = sets.Set()
            goid2children[parentId].add(id)

    if not seenIS_A:
        
        isObsolete = False
        for line in lines[2:]:
            x = [a.strip() for a in line.split()]
            if x == ["is_obsolete:", "true"]:
                isObsolete = True
        if not isObsolete:
            print 'Flag: %s' % (id)
            
        for line in lines[2:]:
            x = [a.strip() for a in line.split()]
            pass
    return goid2children




def readOboFile(obofile):
    fh = open(obofile,'r')
    currBlock = []
    goid2children = {}
    for line in fh:
        if line.strip() == "[Term]":
            processCurrBlock(currBlock, goid2children)
            currBlock = [line.strip()]
        else:
            currBlock.append(line)

    processCurrBlock(currBlock, goid2children)
    return goid2children


##############################################
if __name__ == "__main__":
    oboFile = getOptionsAndInput()
    goid2children = readOboFile(oboFile)
    outfile = oboFile + ".dag.txt"
    f = open(outfile, 'w')
    for goid, children in goid2children.iteritems():
        f.write(goid+" "+string.join(children," ")+"\n")

