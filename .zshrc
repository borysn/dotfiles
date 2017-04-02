#!/bin/zsh

# functions
#fpath=($HOME/.zsh/functions $fpath)

# colors
#eval `dircolors $HOME/.zsh/colors`

# load plugins
autoload -U zutil
autoload -U compinit
autoload -U promptinit

# plugin activiation
compinit
promptinit; prompt gentoo

# zstyles
zstyle ':completion::complete:*' use-cache 1
zstyle ':completion:*:descriptions' format '%U%S%d%b%u'
zstyle ':completion:*:warnings' format '%Swtf r u doing? %d%b'

# opts
setopt correctall
setopt hist_ignore_all_dups
setopt hist_ignore_space
setopt autocd

# key bindings
#bindkey '\e[A' history-search-backward

# Resource files
#for file in $HOME/.zsh/rc/*.rc; do
#	source $file
#done
