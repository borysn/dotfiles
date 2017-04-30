" init.vim
" author: borysn
" license: what's a license?

"""""""""""""""""""""""""""""""""""""""""""""""""""
" vim-plug | https://github.com/junegunn/vim-plug "
"""""""""""""""""""""""""""""""""""""""""""""""""""
call plug#begin('~/.config/nvim/plugged')
  " vim-lexical
  Plug 'reedes/vim-lexical'
  " nerdtree | file tree
  Plug 'scrooloose/nerdtree'
  Plug 'Xuyuanp/nerdtree-git-plugin'
  " fugitive | git wrapper
  Plug 'tpope/vim-fugitive'
  " supertab | vim insert mode completions
  Plug 'ervandew/supertab'
  " youcompleteme | code completion
  Plug 'valloric/youcompleteme'
  " syntastic | code syntax checker
  Plug 'scrooloose/syntastic'
  " vim-gitgutter | git status in gutter
  Plug 'airblade/vim-gitgutter'
  " polyglot language pack
  Plug 'sheerun/vim-polyglot'
  " tagbar
  Plug 'majutsushi/tagbar'
  " vim-colorschemes
  Plug 'flazz/vim-colorschemes'
  " dracula theme
  Plug 'dracula/vim'
  " vim-airline
  Plug 'vim-airline/vim-airline'
  Plug 'vim-airline/vim-airline-themes'
call plug#end()

""""""""""""""""""
" general config "
""""""""""""""""""

" tabs & spaces
set tabstop=2 shiftwidth=2 shiftround expandtab

" show line numbers
set number

" history
set history=25

" yank & cut to system clipboard instead of registers
set clipboard+=unnamedplus

" no swap or backup, but auto write before running commands
set noswapfile nobackup nowritebackup autowrite

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

" show extra white space
set list listchars=tab:>>,trail:.,extends:>

" allow back spacing over autoindent
set backspace=indent,eol,start

" incremental search
set incsearch

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

" posix compatible highlihghing
let g:is_posix=1

" map Y to act like D and C, yank until EOL
map Y y$

" colors
set t_Co=256
color dracula
syntax on
set background=dark

" highlights
set cursorline
set hlsearch
hi Search cterm=NONE ctermfg=NONE ctermbg=blue
hi IncSearch cterm=NONE ctermfg=NONE ctermbg=blue
hi Normal ctermbg=NONE
hi nonText ctermbg=NONE
hi CursorLine cterm=NONE ctermfg=NONE ctermbg=red

"""""""""""""""""
" plugin config "
"""""""""""""""""

"------------"
"[vim-lexical]"
"------------"

"augroup lexical
"  command -nargs=0 LexEnCustom call lexical#init({
"        \ 'spell': 1,
"        \ 'spelllang':  ['en', 'custom'],
"        \ 'dictionary': ['~/.config/nvim/dictionary/custom_words.txt', '/usr/share/dict/words'],
"        \ 'thesaurus':  ['~/.config/nvim/thesaurus/custom-alts.txt', '~/.config/nvim/thesaurus/www.gutenberg.org/files/3202/files/mthesaur.txt'],
"        \ 'spellfile':  ['~/.config/nvim/spell/ftp.vim.org/vim/runtime/spell/en.utf-8.add']
"        \ })
"augroup END

"-----------"
"[nerd-tree]"
"-----------"
" toggle nerd tree using ctrl+n, find current open file in tree
map <C-n> :NERDTreeFind<CR>

" open NERDTree with vim, but move cursor to open file
"autocmd VimEnter * NERDTree | wincmd p

" close nerd tree when open ing a file
let g:NERDTreeQuitOnOpen = 1

" auto open if no files specified
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif

" close vim if nerd-tree is only window left
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" default arrows
let g:NERDTreeDirArrowExpandable = '▸'
let g:NERDTreeDirArrowCollapsible = '▾'

"--------"
"[tagbar]"
"--------"

" toggle tagbar
nmap <F8> :TagbarToggle<CR>

"---------"
"[airline]"
"---------"

" set airline theme
let g:airline_theme = 'behelit'
