#!/bin/env python3

#
# eprl.py
# author: borysn | oxenfree
# license: MIT
#
# edit portage resume list
#

import portage, sys, argparse

# ANSI color codes
# thank you, lliam-mcinroy
# https://stackoverflow.com/a/22886382/2276284
class bcolors:
    HEADER  = '\033[95m'
    OKBLUE  = '\033[94m'
    OKGREEN = '\033[92m'
    WARN    = '\033[93m'
    ERROR   = '\033[91m'
    ENDC    = '\033[0m'

# tcolor
# colorify some text
class tcolor:
    PURPLE  = bcolors.HEADER
    BLUE    = bcolors.OKBLUE
    GREEN   = bcolors.OKGREEN
    YELLOW  = bcolors.WARN
    RED     = bcolors.ERROR
    
    CTXT    = lambda c, m: '{}{}{}'.format(c, m, bcolors.ENDC)
    

# status
# status log msg prefixes (with colors)
class status:
    ERROR   = '{}ERROR{}'.format(bcolors.ERROR, bcolors.ENDC)
    WARN    = '{}WARNING{}'.format(bcolors.WARN, bcolors.ENDC)
    INFO    = '{}INFO{}'.format(bcolors.OKBLUE, bcolors.ENDC)
    SUCCESS = '{}SUCCESS{}'.format(bcolors.OKGREEN, bcolors.ENDC)

# dbstore
# portage mtimedb data store
class dbstore:
    def __init__(self, backup):
        # attempt to get resume and resume_backup from portage mtimedb
        try:
            # get resume items
            self.target     = 'resume_backup' if backup else 'resume'
            self.resumeList = portage.mtimedb.get(self.target, {}).get('mergelist')
        except:
            # listing portage resume items was unsuccessful
            errorAndExit('cannot fetch portage resume list')

    def getResumeList(self): 
        return self.resumeList
    def getTarget(self): 
        return self.target

# errorAndExit
# display error msg and exit
#
# @param msg    msg to be displayed
def errorAndExit(msg):
    print(sys.exc_info())
    print('{}: {}'.format(status.ERROR, msg))
    sys.exit(2)

# parse command line options and arguments
def parseArgs():
    # get argument parser
    parser = argparse.ArgumentParser()
    # list portage resume items
    parser.add_argument('-l', '--list', action='store_true', help='list portage resume items')
    # remove portage resume item(s)
    parser.add_argument('-r', '--remove', action='store', dest='itemNum', type=int, help='remove portage resume items') 
    # which list to remove from
    parser.add_argument('-b', '--backup', action='store_true', help='specify list or removal from backup list')
    # version
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')

    # parse arguments and return
    return parser.parse_args()

# cantRemoveItem
# validate if an item cant be removed from the resume point
#
# @param itemNum    portage resume item number for removal
# @return           True if item cant be removed, False otherwise
def cantRemoveItem(itemNum, db):
    # get current resume list
    resumeList = db.getResumeList();
    # check if itemNum is in range
    if itemNum in range(len(resumeList)):
        return False
    return True

# argsAreValid
# validate commandline options and arguments
#
# note: argparse will handle most of the args error checking
#
# @param args      
# @return        True if args are valid, False otherwise
def argsAreNotValid(args, db): 
    # no options specified
    if args.list == False and args.itemNum == None:
        # no options specified, arparse didn't parse anything either
        # args not valid
        return True
    # itemNum specified
    elif args.itemNum != None:
        # check if itemNum is available for removal
        if cantRemoveItem(args.itemNum, db):
            # error
            print('{}: invalid item number "{}", cannot remove'.format(status.ERROR, args.itemNum))
            # itemNum not available for removal, arg not valid
            return True
    # all args valid, return False
    return False

# printResumeItems
# output resume item list to console
#
# @params items    dictionary containing 'resume' & 'resume_backup' matrices
def printResumeList(resumeList, target):
     # print collection name
     print('[{} list]'.format(tcolor.CTXT(tcolor.PURPLE, target)))
     # check list size
     if resumeList == None or len(resumeList) <= 0:
         print('\t{}: list is empty'.format(status.WARN))
     else:
         for i in range(len(resumeList)):
             print('\t{}: {}'.format(tcolor.CTXT(tcolor.BLUE, i), resumeList[i][2]))

# listPortageResumeItems
# list all ebuilds scheduled in resume & resume_backup
#
# @param db    mtimedb data store
def listPortageResumeItems(db):
        # print resume items
        printResumeList(db.getResumeList(), db.getTarget())
        # listing portage resume items was successful
        print('\n{}: fetch portage resume/resume_backup lists'.format(status.SUCCESS))

# removePortageResumeItem
# remove a portage resume item
#
# @param itemNum    valid portage resume item to be removed
def removePortageResumeItem(itemNum, db):
    print('{}: item "{}" removed from portage resume list'.format(status.SUCCESS))

# runScript
# run script as a function of args
#
# @param args       args should be validated before passed in
def runScript(args, db):
    # list all portage emerge items
    if args.list == True:
        listPortageResumeItems(db)
    # remove portage resume item(s)
    elif args.itemNum != None:
        removePortageResumeItem(db)

# main
# parse & validate args, run script
def main():
    # get args
    args = parseArgs()

    # init db store for portage mtimedb
    db = dbstore(args.backup)
    
    # validate args, exit if invalid
    if argsAreNotValid(args, db):
        errorAndExit('what to do, what to do...try {}'.format(tcolor.CTXT(tcolor.BLUE, '-h')))
        
    # execute script
    runScript(args, db)

    # exit succes
    sys.exit(0)

# exec main
if __name__ == '__main__':
    main()
