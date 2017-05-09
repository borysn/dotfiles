#!/bin/env python3
#
# eprl.py
# author: borysn | oxenfree
# license: MIT
#
# edit portage resume list
#
# usage: eprl.py [-h] [-l] [-r ITEMNUM] [-b] [-v]
#
import os, sys, argparse

# catch portage python module import error
# probably a result of not running as root
# continue script and attempt to error out
# at root privilege check
try:
    import portage
    from portage.util.mtimedb import MtimeDB
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
    # constructor
    def __init__(self, backup):
        # get resume items
        self.target     = 'resume_backup' if backup else 'resume'
        # attempt to get portage mtimedb
        self.db = MtimeDB(portage.mtimedbfile)
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

    # add item to resume list
    def addItems(self, items):
        try:
            for item in items:
                # log
                print('{}: attempting to add {}'.format(status.INFO, tcolor.CTXT(tcolor.PURPLE, item)))
                # create item entry
                entry = ['ebuild', '/', '{}'.format(item), 'merge']
                # add item to dict loaded in memory
                self.db[self.target]['mergelist'].append(entry)
            # write changes to disk
            self.db.commit()
        except:
            errorAndExit('could not add items to portage mtimedb')

    # remove item from resume list by item number
    def removeItems(self, itemNums):
        for item in self.db[self.target]['mergelist']:
            print('\t{}'.format(item))
        try:
            for itemNum in itemNums:
                # log
                print('{}: attempting to remove {}'.format(status.INFO, tcolor.CTXT(tcolor.PURPLE, self.db[self.target]['mergelist'][itemNum][2])))
                # delete specified entry
                del self.db[self.target]['mergelist'][itemNum]
            # write changes to disk
            self.db.commit()
        except:
            errorAndExit('could not remove item portage mtimedb')

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
    print('\n{}\n'.format(resumeList))
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
def confirmDelete(itemNums, db):
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
def removePortageResumeItems(itemNums, db):
    # confirm delete
    if confirmDelete(itemNums, db):
        # attempt to remove resume item
        db.removeItems(itemNums)
        print('{}: item "{}" removed from portage resume list'.format(status.SUCCESS, tcolor.CTXT(tcolor.PURPLE, itemNums)))

# addPortageResumeItems
# add item(s) to a portage resume list
#
# @param  items    list of possible item entries, just portage package names
# @param  db       portage mtimedb data store
def addPortageResumeItems(items, db):
    db.addItems(items)
    print('{}: item(s)\n{}\nadded to portage resume list'.format(status.SUCCESS, tcolor.CTXT(tcolor.PURPLE, items)))

# runScript
# run script as a function of args
#
# @param args       args should be validated before passed in
def runScript(args, db):
    # list all portage emerge items
    if args.list == True:
        listPortageResumeItems(db)
    # remove portage resume item(s)
    elif args.itemNums != None:
        removePortageResumeItems(args.itemNums, db)
    # add portage resume item(s)
    elif args.items != None:
        addPortageResumeItems(args.items, db)

# parse command line options and arguments
def parseArgs():
    # get argument parser
    parser = argparse.ArgumentParser()
    # list portage resume items
    parser.add_argument('-l', '--list', action='store_true', help='list portage resume items')
    # remove portage resume item(s)
    parser.add_argument('-r', '--remove', action='store', dest='itemNums', type=int, nargs="+", help='remove portage resume items') 
    # add portage resume item(s)
    parser.add_argument('-a', '--add', action='store', dest='items', type=str, nargs='+', help='add resume item(s) to a resume list')
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
    # init return
    argsAreNotValid = False
    # no options specified
    if args.list == False and args.itemNums == None and args.items == None:
        # no options specified, arparse didn't parse anything either
        # args not valid
        argsAreNotValid = True
    # itemNum specified
    elif args.itemNums != None:
        # iterate item numbers
        for itemNum in args.itemNums:
            # check if itemNum is available for removal
            if cantRemoveItem(itemNum, db):
                # error
                print('{}: invalid item number "{}", cannot remove'.format(status.ERROR, itemNum))
                # itemNum not available for removal, arg not valid
                argsAreNotValid = True
                break
    # items specified
    elif args.items != None:
        # iterate items
        for item in args.items:
            try:
                # find any matches for a given item
                matches = portage.dbapi.porttree.portdbapi().match(item)
                # no matches
                if len(matches) == 0:
                    # error
                    print('{}: invalid dependency "{}", cannot add to resume list'.format(status.ERROR, item))
                    # cannot match this item, arg not valid
                    argsAreNotValid = True
                    break
                # one or more matches
                elif len(matches) >=:

            except portage.exception.AmbiguousPackageName:
                errorAndExit('can\'t validate a package name because it\'s ambiguous, try being more specific\n\ti.e. \'dev-lisp/asdf\' vs. \'asdf\'')
            except:
                errorAndExit('something went wrong when attempting to validate your listed dependencies')
    # return result
    return argsAreNotValid

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
