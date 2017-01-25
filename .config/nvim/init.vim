""""""""""""""""""
" general config "
""""""""""""""""""

" tabs & spaces
set tabstop=2 shiftwidth=2 expandtab

" sanely reset options when resources
"set nocompatible

" show line numbers
set number

" no wrap 
"set nowrap

" determine file type based on name
filetype indent plugin on

" keep undo history for multiple files
set hidden

" better cmd line completion
set wildmenu

" show partial commands in the last line of screen
set showcmd

" side scroll

" highlight searches
set hlsearch

" allow back spacing over autoindent
set backspace=indent,eol,start

" auto indent
set autoindent

" stop certain movements form always going to first character of line
set nostartofline

" display cursor position on last line of scren or status
set ruler

" always display status line
set laststatus=2

" raise dialog asking for save instead of failing command
set confirm

" map Y to act like D and C, yank until EOL
map Y y$

" Allow color schemes to do bright colors without forcing bold.
if &t_Co == 8 && $TERM !~# '^linux\|^Eterm'
  set t_Co=16
endif

"""""""""""""""""""""""""""""""""""""""""""""""""""
" vim-plug | https://github.com/junegunn/vim-plug "
"""""""""""""""""""""""""""""""""""""""""""""""""""
call plug#begin('~/.config/nvim/plugged')

  " nerdtree | file tree
  Plug 'scrooloose/nerdtree'
  Plug 'Xuyuanp/nerdtree-git-plugin'

  " fugitive | git wrapper
  Plug 'tpope/vim-fugitive'

  " youcompleteme | code completion
  Plug 'valloric/youcompleteme'

  " supertab | vim insert mode completions
  Plug 'ervandew/supertab'

  " syntastic | code syntax checker
  Plug 'scrooloose/syntastic'

  " vim-gitgutter | git status in gutter
  Plug 'airblade/vim-gitgutter'

  " vim-javascript
  Plug 'pangloss/vim-javascript'

  " vim-jsx
  Plug 'mxw/vim-jsx'

  " vim-markdown
  Plug 'tpope/vim-markdown'

  " html5.vim
  Plug 'othree/html5.vim'

  " JSON.vim
  Plug 'elzr/vim-json'

  " dart-vim-plugin
  Plug 'dart-lang/dart-vim-plugin'

  " typescript-vim
  Plug 'leafgarland/typescript-vim'

  " tagbar
  Plug 'majutsushi/tagbar'

  " vim-colorschemes
  Plug 'flazz/vim-colorschemes'

  " vim-airline
  Plug 'vim-airline/vim-airline'
  Plug 'vim-airline/vim-airline-themes'

call plug#end()

"""""""""""""""""
" plugin config "
"""""""""""""""""

" [vim-colorschemes]
 set t_Co=256
 syntax enable
 set background=dark
 colorscheme mojave
 "let g:solarized_termcolors=256
 "let g:badwold_darkgutter=1
 highlight Normal ctermbg=None
 highlight nonText ctermbg=None

" [nerd-tree]
 " auto open if no files specified
 autocmd StdinReadPre * let s:std_in=1
 autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
 " key shortcut toggle
 map <C-n> :NERDTreeToggle<CR>
 " close vim if nerd-tree is only window left
 autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
 " default arrows
 let g:NERDTreeDirArrowExpandable = '▸'
 let g:NERDTreeDirArrowCollapsible = '▾'

" [tagbar]
 nmap <F8> :TagbarToggle<CR>

" [airline]
 let g:airline_theme = 'bubblegum' 
