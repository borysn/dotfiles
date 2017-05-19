#!/usr/bin/env python
#
# diff.py
# author: borysn
# license: what's a license?
#
# diff system files and dotfiles and display any discrepancies
#
import os, sys, subprocess, argparse

# tcolor
class tcolor:
    PURPLE  = '\033[95m'
    BLUE    = '\033[94m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[93m'
    RED     = '\033[91m'
    ENDC    = '\033[0m'
    CTXT    = lambda c, m: '{}{}{}'.format(c, m, tcolor.ENDC)

# diffobj
class DiffObj:
    # constructor
    def __init__(self, dotfile, sysfile):
        self.dotfile = dotfile
        self.sysfile = sysfile
    # sysfileExists
    def sysfileExists(self): return os.path.exists(self.sysfile)
    # getFileBasename
    def getFileBasename(self): return os.path.basename(self.sysfile)
    # diff files
    def diff(self): return subprocess.getoutput('diff {} {}'.format(self.sysfile, self.dotfile))
    # getSysfile
    def getSysfile(self): return self.sysfile
    # getDotfile
    def getDotfile(self): return self.dotfile

# properties
class properties:
    currOS = 'os/gentoo'
    laptop = '{}/{}'.format(currOS, 'laptop')
    desktop = '{}/{}'.format(currOS, 'desktop')
    target = ''
    ignoreList = []
    # constructor
    def __init__(self, args):
        self.target = self.laptop if args.laptop else self.desktop
        self.ignoreList.extend([
            '.git',
            '.gitattributes',
            'README.md',
            'diff.py',
            'extra',
            '__pycache__',
            'os/arch',
            'sudoers',
            self.desktop if args.laptop else self.laptop
        ])

# isIgnoredFileOrDir
def isIgnoredFileOrDir(props, string):
    # init return
    result = False
    # traverse ignore list
    for ignore in props.ignoreList:
        if ignore in string:
            result = True
            break
    # not ignored
    return result

# filterIgnored
def filterIgnored(props, root, filenames):
    # init return
    files = []
    # check if root is ignored
    if not isIgnoredFileOrDir(props, root):
        # traverse filenames
        for file in filenames:
            # check if file is ignored
            if not isIgnoredFileOrDir(props, file):
                # add file
                files.append(os.path.join(os.getcwd(), root[2:], file))
    return files

# getAllFiles
def getDotfiles(props):
    # init return
    files = []
    # recursively walk dotfiles dir
    for root, dirnames, filenames in os.walk('.'):
        files.extend(filterIgnored(props, root, filenames))
    # return results
    return files

# getSysfiles
def getSysfiles(props, dotfiles):
    # init return
    sysfiles = []
    # traverse dotfiles
    for f in dotfiles:
        # check for file outside of user space
        if props.target in f:
            # truncate everything (upto and including) the target string
            file = f[len(os.getcwd()) + len(props.target) + 1:]
            sysfiles.append(file)
        else:
            # user space file
            file = os.path.join(os.environ['HOME'], f[len(os.getcwd())+1:])
            sysfiles.append(file)

    # return result
    return sysfiles

# prepareDiffObjects
def prepareDiffObjects(sysfiles, dotfiles):
    # init diff
    results = {}
    # iterate files
    for i in range(len(sysfiles)):
        try:
            # create adn store diff obj
            results[os.path.basename(sysfiles[i])] = DiffObj(sysfiles[i], dotfiles[i])
        except Exception as err:
            print(err)
            sys.exit(2)
            pass
    # return diff
    return results

# getDiffObjects
def getDiffObjects(props):
    # get dotfiles (repo)
    dotfiles = getDotfiles(props)
    # get files on system (1 to 1 relationship with dotfiles list)
    sysfiles = getSysfiles(props, dotfiles)
    # return diff results
    return prepareDiffObjects(sysfiles, dotfiles)

# printDiffResults
def printDiffResults(diffObjects):
    # iterate diff results
    for file, obj in diffObjects.items():
        # get diff
        diff = obj.diff()
        # check for not empty diff
        if not diff == '':
            c1 = tcolor.RED
            c2 = tcolor.YELLOW
            print('{}'.format(tcolor.CTXT(c1, file)))
            print('\t{}'.format(tcolor.CTXT(c2, obj.getSysfile())))
            print('\t{}'.format(tcolor.CTXT(c2, obj.getDotfile())))

# parseArgs
def parseArgs():
    # get argument parser
    parser = argparse.ArgumentParser()
    # laptop flag
    parser.add_argument('-l', '--laptop', action='store_true', help='flag to target laptop os files')
    # verbose output TODO
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose output')
    return parser.parse_args()

# main
def main():
    # parse args
    args = parseArgs()
    # get diff results
    printDiffResults(getDiffObjects(properties(args)))
    # script completed successfully
    sys.exit(0)

# check for main and run script
if __name__ == '__main__':
    main()
