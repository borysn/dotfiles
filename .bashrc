#
# ~/.bashrc
#

########
# path #
########

export PATH=$PATH:~/.local/scripts
export PATH=$PATH:~/.npm/bin
export PATH=$PATH:~/.gem/ruby/2.4.0/bin


###########
# exports #
###########

# editor
export EDITOR=nvim
# tmux
export TERM=rxvt-256color
# prompt dir trim
export PROMPT_DIRTRIM=1


#########
# alias #
#########

alias clock="tty-clock -c -C 6 -t"
alias reboot="sudo systemctl reboot"
alias poweroff="sudo systemctl poweroff"
alias halt="sudo systemctl halt"

#########
# other #
#########

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
#PS1='\[\033[38;5;13m\][\[$(tput sgr0)\]\[\033[38;5;10m\]\u\[$(tput sgr0)\]\[\033[38;5;12m\]@\[$(tput sgr0)\]\[\033[38;5;10m\]\h\[$(tput sgr0)\]\[\033[38;5;15m\] \[$(tput sgr0)\]\[\033[38;5;12m\]\W\[$(tput sgr0)\]\[\033[38;5;13m\]]\[$(tput sgr0)\]\[\033[38;5;12m\]\\$\[$(tput sgr0)\]\[\033[38;5;15m\] \[$(tput sgr0)\]'
export PS1="\w \[$(tput sgr0)\]\[\033[38;5;210m\]\\$\[$(tput sgr0)\]\[\033[38;5;15m\] \[$(tput sgr0)\]"

#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
export SDKMAN_DIR="/home/p3pt/.sdkman"
[[ -s "/home/p3pt/.sdkman/bin/sdkman-init.sh" ]] && source "/home/p3pt/.sdkman/bin/sdkman-init.sh"
