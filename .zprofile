#!/bin/sh

#
# .zprofile
# author: borysn
# license: what's a license?
#

###########
# exports #
###########

export PYTHONSTARTUP=~/.pythonrc

#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
export SDKMAN_DIR="/home/p3pt/.sdkman"
[[ -s "/home/p3pt/.sdkman/bin/sdkman-init.sh" ]] && source "/home/p3pt/.sdkman/bin/sdkman-init.sh"
