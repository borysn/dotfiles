#!/usr/bin/env python
# diff.py
# author: borysn
# license: what's a license?
#
# diff system files and dotfiles and display any discrepancies
import os, sys, difflib

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
                files.append(fcwd('{}/{}'.format(root[2:], file)))
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
            file = '{}{}'.format(os.environ['HOME'], f[len(os.getcwd())+1:])
            sysfiles.append(file)

    # return result
    return sysfiles

# diff
def diff(sysfiles, dotfiles):
    # init diff
    results = {}
    # iterate files
    for i in range(len(sysfiles)):
        print('{}:{}'.format(sysfiles[i], dotfiles[i]))
        try:
            # TODO check file r ok
            # open files for reading
            f1 = open(sysfiles[i], 'r', errors='replace')
            f2 = open(dotfiles[i], 'r', errors='replace')
            # diff files
            diff = difflib.ndiff(f1.readlines(), f2.readlines())
            # store results
            results[os.path.basename(f1.name)] = [f1, f2, diff]
            # close files
            f1.close()
            f2.close()
        except Exception as err:
            print(err)
            sys.exit(2)
            pass
    # return diff
    return results

# getDiffResults
def getDiffResults():
    # get dotfiles (repo)
    dotfiles = getDotfiles()
    # get files on system (1 to 1 relationship with dotfiles list)
    sysfiles = getSysfiles(dotfiles)
    # return diff results
    return diff(sysfiles, dotfiles)

# main
def main():
    # get diff results
    diffResults = getDiffResults()
    # script completed successfully
    sys.exit(0)

# check for main and run script
if __name__ == '__main__':
    main()
