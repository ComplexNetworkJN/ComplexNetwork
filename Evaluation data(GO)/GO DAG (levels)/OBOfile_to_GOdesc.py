#!/usr/bin/env python

### USAGE:
# ./OBOfile_to_GOdesc.py <obo-file>

import re, sys, os, string, math, fileinput
import sets, getopt, popen2, tempfile, copy

def getOptionsAndInput():
    usageStr = "./OBOfile_to_GOdesc <obo-file>"
    (opts, args) = getopt.getopt(sys.argv[1:], "h", ["help"])

    oboFile = ""
    for o,a in opts:
        if o in ["-h", "--help"] or len(args) != 1:
            print usageStr
            sys.exit(1)
            
    oboFile = args[0]
    return oboFile



def processCurrBlock(lines, goid2desc):
    if len(lines)==0 or lines[0].strip() != "[Term]":
        return
    idline = [a.strip() for a in lines[1].split()]
    assert idline[0] == "id:"
    id = idline[1]
    nameline = [a.strip() for a in lines[2].split()]
    assert nameline[0] == "name:"
    name = string.join(nameline[1:], " ")

    goid2desc[id.upper()] = name
    return





def readOboFile(obofile):
    fh = open(obofile,'r')
    currBlock = []
    goid2desc = {}
    for line in fh:
        if line.strip() == "[Term]":
            processCurrBlock(currBlock, goid2desc)
            currBlock = [line.strip()]
        else:
            currBlock.append(line)

    processCurrBlock(currBlock, goid2desc)
    return goid2desc



##############################################
if __name__ == "__main__":
    oboFile = getOptionsAndInput()
    goid2desc = readOboFile(oboFile)

    for goid, desc in goid2desc.iteritems():
        print '%s %s' % (goid, desc)

