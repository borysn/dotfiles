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

    def disable(self):
        self.HEADER  = ''
        self.OKBLUE  = ''
        self.OKGREEN = ''
        self.WARN    = ''
        self.ERROR   = ''
        self.ENDC    = ''

# status
# status log msg prefixes (with colors)
class status:
    ERROR   = '{}ERROR{}'.format(bcolors.ERROR, bcolors.ENDC)
    WARN    = '{}WARNING{}'.format(bcolors.WARN, bcolors.ENDC)
    INFO    = '{}INFO{}'.format(bcolors.OKBLUE, bcolors.ENDC)
    SUCCESS = '{}SUCCESS{}'.format(bcolors.OKGREEN, bcolors.ENDC)

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
    parser.add_argument('-r', '--remove', action='store', dest='itemNum', type=int, help='remove portage resume item') 
    # version
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')

    # parse arguments and return
    return parser.parse_args()

# canRemoveItem
# validate if an item can be removed from the resume point
#
# @param itemNum    valid portage resume item for removal
# @return           True if item can be removed, False otherwise
def canRemoveItem(itemNum):
    return True

# argsAreValid
# validate commandline options and arguments
#
# note: argparse will handle most of the args error checking
#
# @param args      
# @return        True if args are valid, False otherwise
def argsAreValid(args): 
    # no options specified
    if args.list == False and args.itemNum == None:
        # no options specified, arparse didn't parse anything either
        print('{}: what to do, what to do... try -h'.format(status.ERROR))
        # args not valid
        return False
    # itemNum specified
    elif args.itemNum != None:
        # check if itemNum is available for removal
        if canRemoveItem(args.itemNum) != True:
            # error
            print('{}: invalid item number "{}", cannot remove'.format(status.ERROR, args.itemNum))
            # itemNum not available for removal, arg not valid
            return False
    # all args valid, return True
    return True

# printResumeItems
# output resume item list to console
#
# @params items    dictionary containing 'resume' & 'resume_backup' matrices
def printResumeItems(allItems):
    # print all items
    for name,items in allItems.items():
        # print collection name
        print('[' + name + ']')
        # check list size
        if items == None or len(items) <= 0:
            print('\t{}: list is empty'.format(status.WARN))
        else:
            for i in range(len(items)):
                print('\t#{}: {}'.format(i, items[i][2]))

# listPortageResumeItems
# list all ebuilds scheduled in resume & resume_backup
def listPortageResumeItems():
    # attempt to get resume and resume_backup from portage mtimedb
    try:
        # get resume items
        resume       = portage.mtimedb.get('resume', {}).get("mergelist")
        resumeBackup = portage.mtimedb.get('resume_backup', {}).get("mergelist")
        items = {'resume': resume, 'resume_backup': resumeBackup}
        # print resume items
        printResumeItems(items)
        # listing portage resume items was successful
        print('\n{}: fetch portage resume/resume_backup lists'.format(status.SUCCESS))
    #except TypeError as err:
    #    print(err)
    except:
        # listing portage resume items was unsuccessful
        errorAndExit('cannot fetch portage resume list')


# removePortageResumeItem
# remove a portage resume item
#
# @param itemNum    valid portage resume item to be removed
def removePortageResumeItem(itemNum):
    print('{}: item "{}" removed from portage resume list'.format(status.SUCCESS))

# runScript
# run script as a function of args
#
# @param args       args should be validated before passed in
def runScript(args):
    # list all portage emerge items
    if args.list == True:
        listPortageResumeItems()
    # remove portage resume item(s)
    if args.itemNum != None:
        removePortageResumeItem(args.itemNum)

# main
# parse & validate args, run script
def main():
    # get args
    args = parseArgs()

    # validate args, exit if invalid
    if argsAreValid(args) == False:
        sys.exit(2)
        
    # execute script
    runScript(args)

    # exit succes
    sys.exit(0)

# exec main
if __name__ == '__main__':
    main()
