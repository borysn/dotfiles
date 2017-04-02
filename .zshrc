#!/bin/zsh

# functions
#fpath=($HOME/.zsh/functions $fpath)

# load plugins
autoload -U zutil
autoload -U compinit
autoload -U promptinit
autoload -U colors

# plugin activiation
compinit
promptinit; prompt gentoo
colors

# completion
zstyle ':completion:*' use-cache on
zstyle ':completion:*' cache-path ~/.zsh/cache
zstyle ':completion:*:descriptions' format '%U%S%d%b%u'
zstyle ':completion:*:warnings' format '%Swaaahh? %d%b'
zstyle ':completion:*' _completer _complete _match _approximate
zstyle ':completion:*:match:*' original only
zstyle -e ':completion:*:approximate:*' max-errors 'reply=($((($#PREFIX+$#SUFFIX)/3))numeric)'
zstyle ':completion:*:function' ignored-patterns '_*'
zstyle ':completion:*:*:kill:*' menu yes select
zstyle ':completion:*:kill:*' force-list always
zstyle ':completion:*' squeeze-slashes true
zstyle ':completion:*:cd:*' ignore-parents parent pwd

# opts
setopt correctall
setopt hist_ignore_all_dups
setopt hist_ignore_space
setopt autocd
setopt extendedglob

# key bindings
#bindkey '\e[A' history-search-backward

# alias'
alias clock='tty-clock -c -C 6 -t'
alias reboot='sudo systemctl reboot'
alias poweroff='sudo systemctl poweroff'
alias halt='sudo systemctl halt'
alias ls='ls --color=auto --human-readable --group-directories-first --classify'
alias grep='grep --colour=auto'
alias egrep='egrep --colour=auto'
alias cp='cp -iv'
alias mv='mv -iv'
alias rmdir='rmdir -v'
alias ln='ln -v'
alias chmod='chmod -c'
alias chown='chown -c'
alias mkdir='mkdir -v'

if command -v colordiff > /dev/null 2>&1; then
  alias diff='colordiff -Nuar'
else
  alias diff='diff -Nuar'
fi

# path
export PATH=$PATH:~/.local/scripts
export PATH=$PATH:~/.npm/bin
export PATH=$PATH:~/.gem/ruby/2.4.0/bin

# exports
export EDITOR=nvim
export TERM=rxvt-256color

# Resource files
#for file in $HOME/.zsh/rc/*.rc; do
#	source $file
#done

# alert
if [ -f ~/.alert ]; then echo '>>> check ~/.alert'; fi

#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
export SDKMAN_DIR='/home/p3pt/.sdkman'
[[ -s '/home/p3pt/.sdkman/bin/sdkman-init.sh' ]] && source '/home/p3pt/.sdkman/bin/sdkman-init.sh'
