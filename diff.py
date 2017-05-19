#!/usr/bin/env python
# diff.py
# author: borysn
# license: what's a license?
#
# diff system files and dotfiles and display any discrepancies
#
import os, sys, subprocess

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

# TODO args
currOS = 'os/gentoo'
laptop = '{}/{}'.format(currOS, 'laptop')
desktop = '{}/{}'.format(currOS, 'desktop')
laptopDiff = False
fcwd = lambda x: '{}/{}'.format(os.getcwd(), x)
target = desktop if not laptopDiff else laptop
ignoreList = [
    '.git',
    '.gitattributes',
    'README.md',
    'diff.py',
    'extra',
    '__pycache__',
    'os/arch',
    'sudoers',
    laptop if not laptopDiff else desktop
]

# isIgnoredFileOrDir
def isIgnoredFileOrDir(i):
    # init return
    result = False
    # traverse ignore list
    for ignore in ignoreList:
        if ignore in i:
            result = True
            break
    # not ignored
    return result

# filterIgnored
def filterIgnored(root, filenames):
    # init return
    files = []
    # check if root is ignored
    if not isIgnoredFileOrDir(root):
        # traverse filenames
        for file in filenames:
            # check if file is ignored
            if not isIgnoredFileOrDir(file):
                # add file
                files.append(fcwd(os.path.join(root[2:], file)))
    return files

# getAllFiles
def getDotfiles():
    # init return
    files = []
    # recursively walk dotfiles dir
    for root, dirnames, filenames in os.walk('.'):
        files.extend(filterIgnored(root, filenames))
    # return results
    return files

# getSysfiles
def getSysfiles(dotfiles):
    # init return
    sysfiles = []
    # traverse dotfiles
    for f in dotfiles:
        # check for file outside of user space
        if target in f:
            # truncate everything (upto and including) the target string
            file = f[len(os.getcwd()) + len(target) + 1:]
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
def getDiffObjects():
    # get dotfiles (repo)
    dotfiles = getDotfiles()
    # get files on system (1 to 1 relationship with dotfiles list)
    sysfiles = getSysfiles(dotfiles)
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

# main
def main():
    # get diff results
    printDiffResults(getDiffObjects())
    # script completed successfully
    sys.exit(0)

# check for main and run script
if __name__ == '__main__':
    main()
