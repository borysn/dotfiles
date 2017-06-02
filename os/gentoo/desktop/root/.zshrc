# .zshrc
# author: borysn
# license: what's a license?

################
# basic config #
################

umask 077
ZDOTDIR=${ZDOTDIR:-${HOME}}
TERM=rxvt-unicode-256color
HISTFILE=${ZDOTDIR}/.zsh/.histfile
HISTSIZE=10000
SAVEHIST=${HISTSIZE}
export TMP=$ZDOTDIR/.tmp
export TEMP=$TMP
export TMPDIR=$TMP
export TMPPREFIX=$TMPDIR/zsh

if [ ! -d $TMP ]; then mkdir $TMP; fi

################
# load plugins #
################

autoload -Uz zutil
autoload -Uz compinit
autoload -Uz promptinit
autoload -Uz colors
autoload -Uz up-line-or-beginning-search
autoload -Uz down-line-or-beginning-search

######################
# plugin activiation #
######################

compinit
promptinit
prompt gentoo
colors
zle -N up-line-or-beginning-search
zle -N down-line-or-beginning-search

##############
# completion #
##############

zstyle ':completion:*' menu select 
zstyle ':completion:*' use-cache 1
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
zstyle ':completion:*:sudo:*' command-path /usr/local/sbin /usr/local/bin /usr/sbin /usr/bin /sbin /bin

########
# opts #
########

setopt correctall
setopt complete_aliases
setopt hist_ignore_all_dups
setopt hist_ignore_space
setopt autocd
setopt extendedglob
setopt noflowcontrol

################
# key bindings #
################

bindkey -v
typeset -g -A key
bindkey '^[[1~' beginning-of-line #home 
bindkey '^[[2~' overwrite-mode #insert
bindkey '^[[3~' delete-char #delete
bindkey '^[[4~' end-of-line #end
bindkey '^[[5~' up-line-or-history #pageup
bindkey '^[[6~' down-line-or-history #pagedown
bindkey '^[[A' up-line-or-search #up 
bindkey '^[[B' down-line-or-search #down
bindkey '^[[C' forward-char #right
bindkey '^[[D' backward-char #left

# for rxvt
bindkey '^A' beginning-of-line #ctrl-a
bindkey '^E' end-of-line #ctrl-e

[[ -n '$key[Up]'   ]] && bindkey -- '$key[Up]'   up-line-or-beginning-search
[[ -n '$key[Down]' ]] && bindkey -- '$key[Down]' down-line-or-beginning-search
