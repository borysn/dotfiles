#!/bin/sh

#
# sort-use-flags.sh
# author: borysn
# license: MIT
#
# sort use flags (USE="..."), in make.conf, alphabetically
#

# make.conf file
target=/etc/portage/make.conf.test

# get use line, strip everything except useflags
useline=$(grep 'USE=' $target | sed 's/^USE="//' | sed 's/"//')
# put all use flags on a new line
useflags=$(echo $useline | sed 's/\s/\n/g')
# sort use flags
useflags_sorted=$(echo $useflags | sort)
# create new useline, and remove trailing white space
new_useline='USE="success '$(echo $useflags_sorted | tr '\n' ' ' | sed 's/ $//')'"'

# replace new use flag line in make.conf
$(sed -i "s|^USE=.*$|$new_useline|" $target)
