#!/bin/sh

#
# diff-gentoo-desktop.sh
# author: borysn
# license: what's a license?
#
# diff dotfiles, and os specific files for desktop setup
# show results in pretty format
#
# allow auto copy files to git directory
#     - auto chown!
#

# current working directory
cwd=$(pwd)
user=$(echo $USER)
