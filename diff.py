#!/usr/bin/env python
# diff.py
# author: borysn
# license: what's a license?
import os

# TODO args
laptop = False
fcwd = lambda x: '{}/{}'.format(os.getcwd(), x)
ignoreList = [
    '.git',
    '.gitattributes',
    'README.md',
    'diff.py',
    '__pycache__',
    'os/arch',
    'os/laptop' if not laptop else 'os/desktop'
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
    return []

# diffResults
def diffResults():
    dotfiles = getDotfiles()
    sysfiles = getSysfiles(dotfiles)
    return []

# main
def main():
    return diffResults()

# check for main and run script
if __name__ == '__main__':
    main()
