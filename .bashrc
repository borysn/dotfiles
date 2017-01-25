#
# ~/.bashrc
#

# exports
export EDITOR=nvim
export VISUAL=nvim
export TERMINAL=urxvt
export PROMPT_DIRTRIM=1

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
export PS1="\w \[$(tput sgr0)\]\[\033[38;5;210m\]\\$\[$(tput sgr0)\]\[\033[38;5;15m\] \[$(tput sgr0)\]"

PATH="/home/p3pt/.perl5/bin${PATH:+:${PATH}}"; export PATH;
PERL5LIB="/home/p3pt/.perl5/lib/perl5${PERL5LIB:+:${PERL5LIB}}"; export PERL5LIB;
PERL_LOCAL_LIB_ROOT="/home/.p3pt/perl5${PERL_LOCAL_LIB_ROOT:+:${PERL_LOCAL_LIB_ROOT}}"; export PERL_LOCAL_LIB_ROOT;
PERL_MB_OPT="--install_base \"/home/p3pt/.perl5\""; export PERL_MB_OPT;
PERL_MM_OPT="INSTALL_BASE=/home/p3pt/.perl5"; export PERL_MM_OPT;

#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
export SDKMAN_DIR="/home/p3pt/.sdkman"
[[ -s "/home/p3pt/.sdkman/bin/sdkman-init.sh" ]] && source "/home/p3pt/.sdkman/bin/sdkman-init.sh"

