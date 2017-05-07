#!/bin/env python3

#
# eprl.py
# author: borysn | oxenfree
# license: MIT
#
# edit portage resume list
#
# usage: eprl.py [-h] [-l] [-r ITEMNUM] [-b] [-v]

import os, sys, argparse, pickle

try:
    import portage
except ImportError:
    print('hmm, can\'t find portage python module, that\'s not good...')

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
        # get resume items
        self.target     = 'resume_backup' if backup else 'resume'
        # attempt to get resume and resume_backup from portage mtimedb
        try:
            self.resumeList = portage.mtimedb[self.target]['mergelist']
        except:
            # listing portage resume items was unsuccessful
            errorAndExit('cannot fetch portage resume list')

    #  return resume list
    def getResumeList(self): 
        return self.resumeList
    # get target 'resume' || 'resume_backup' if -b flag is set
    def getTarget(self): 
        return self.target
    # remove item from resume list by item number
    def removeItem(self, itemNum):
        try:
            # store portage mtimedb in memory
            data = portage.mtimedb
            # log
            print('{}: attempting to remove {}'.format(status.INFO, tcolor.CTXT(tcolor.PURPLE, data[self.target]['mergelist'][itemNum][2])))
            # delete specified entry
            del data[self.target]['mergelist'][itemNum]
            # attempt tow rite changes to disk
            f = open(portage.mtimedbfile, 'wb')
            pickle.dump(data, f)
            f.close()
        except:
            errorAndExit('could not save changes to portate mtimedb')

# errorAndExit
# display error msg and exit
#
# @param msg    msg to be displayed
def errorAndExit(msg):
    excInfo = sys.exc_info()
    if excInfo[0] != None:
        print(sys.exc_info())
    print('{}: {}'.format(status.ERROR, msg))
    sys.exit(2)

# cantRemoveItem
# validate if an item cant be removed from the resume point
#
# @param itemNum    portage resume item number for removal
# @return           True if item cant be removed, False otherwise
def cantRemoveItem(itemNum, db):
    # get current resume list
    resumeList = db.getResumeList();
    # check if itemNum is in range
    if resumeList != None and itemNum in range(len(resumeList)):
        return False
    return True

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

# confirmDelete
# have user confirm the removal of an item
#
# @param itemNum    item to be deleted
# @param db         portage mtimedb data store
def confirmDelete(itemNum, db):
    # init return
    confirmed = False
    msg = '{}: {}'.format(status.WARN, 'are you sure? (y/n) ')
    while True:
        answer = input(msg)
        answer = answer.upper()
        if answer == 'Y':
            confirmed = True
            break;
        elif answer == 'N':
            break;
    return confirmed

# removePortageResumeItem
# remove a portage resume item
#
# @param itemNum    valid portage resume item to be removed
def removePortageResumeItem(itemNum, db):
    # confirm delete
    if confirmDelete(itemNum, db):
        # attempt to remove resume item
        db.removeItem(itemNum)
        print('{}: item "{}" removed from portage resume list'.format(status.SUCCESS, tcolor.CTXT(tcolor.PURPLE, itemNum)))

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
        removePortageResumeItem(args.itemNum, db)

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

# argsAreValid
# validate commandline options and arguments
#
# note: argparse will handle most of the args error checking
#
# @param args    script arguments
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

# userDoesNotHaveRootPrivileges
# check if user does not have root privileges
#
# @return    true if user does not have root privileges, false otherwise
def userDoesNotHaveRootPrivileges(): return True if os.getuid() != 0 else False

# main
# root privilege check, parse & validate args, get mtimedb store, run script
def main():
    # check for correct privileges
    if userDoesNotHaveRootPrivileges():
        errorAndExit('eprl.py requires root privileges, try running with sudo')

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
