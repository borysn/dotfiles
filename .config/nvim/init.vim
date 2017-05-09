" init.vim
" author: borysn
" license: what's a license?

"""""""""""""""""""""""""""""""""""""""""""""""""""
" vim-plug | https://github.com/junegunn/vim-plug "
"""""""""""""""""""""""""""""""""""""""""""""""""""
call plug#begin('~/.config/nvim/plugged')
  Plug 'reedes/vim-lexical'
  Plug 'scrooloose/nerdtree'
  Plug 'Xuyuanp/nerdtree-git-plugin'
  Plug 'tpope/vim-fugitive'
  Plug 'ervandew/supertab'
  Plug 'shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins'}
  Plug 'tweekmonster/deoplete-clang2',
  Plug 'zchee/deoplete-go',
  Plug 'shougo/neco-vim',
  Plug 'OmniSharp/omnisharp-vim',
  Plug 'dimixar/deoplete-omnisharp',
  Plug 'shougo/unite.vim',
  Plug 'tpope/vim-dispatch',
  Plug 'fishbullet/deoplete-ruby',
  Plug 'ternjs/tern_for_vim', {'do': 'npm install -g tern' }
  Plug 'carlitux/deoplete-ternjs'
  Plug 'clojure-vim/async-clj-omni',
  Plug 'davidhalter/jedi',
  Plug 'zchee/deoplete-jedi',
  Plug 'artur-shaik/vim-javacomplete2',
  Plug 'mhartington/nvim-typescript'
  Plug 'scrooloose/syntastic'
  Plug 'airblade/vim-gitgutter'
  Plug 'sheerun/vim-polyglot'
  Plug 'majutsushi/tagbar'
  Plug 'flazz/vim-colorschemes'
  Plug 'dracula/vim'
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

"""""""""
" unite "
"""""""""

let g:unite_source_menu_menus = get(g:,'unite_source_menu_menus',{})
let g:unite_source_menu_menus.git = {
    \ 'description' : '            gestionar repositorios git
        \                            ⌘ [espacio]g',
    \}
let g:unite_source_menu_menus.git.command_candidates = [
    \['▷ tig                                                        ⌘ ,gt',
        \'normal ,gt'],
    \['▷ git status       (Fugitive)                                ⌘ ,gs',
        \'Gstatus'],
    \['▷ git diff         (Fugitive)                                ⌘ ,gd',
        \'Gdiff'],
    \['▷ git commit       (Fugitive)                                ⌘ ,gc',
        \'Gcommit'],
    \['▷ git log          (Fugitive)                                ⌘ ,gl',
        \'exe "silent Glog | Unite quickfix"'],
    \['▷ git blame        (Fugitive)                                ⌘ ,gb',
        \'Gblame'],
    \['▷ git stage        (Fugitive)                                ⌘ ,gw',
        \'Gwrite'],
    \['▷ git checkout     (Fugitive)                                ⌘ ,go',
        \'Gread'],
    \['▷ git rm           (Fugitive)                                ⌘ ,gr',
        \'Gremove'],
    \['▷ git mv           (Fugitive)                                ⌘ ,gm',
        \'exe "Gmove " input("destino: ")'],
    \['▷ git push         (Fugitive, salida por buffer)             ⌘ ,gp',
        \'Git! push'],
    \['▷ git pull         (Fugitive, salida por buffer)             ⌘ ,gP',
        \'Git! pull'],
    \['▷ git prompt       (Fugitive, salida por buffer)             ⌘ ,gi',
        \'exe "Git! " input("comando git: ")'],
    \['▷ git cd           (Fugitive)',
        \'Gcd'],
    \]
nnoremap <silent>[menu]g :Unite -silent -start-insert menu:git<CR>

"""""""""""""
" omnisharp "
"""""""""""""

let g:OmniSharp_selector_ui = 'unite'

"""""""""""""""""""""
" vim-javacomplete2 "
"""""""""""""""""""""

" enable
autocmd FileType java setlocal omnifunc=javacomplete2#Complete
" to enable smart (trying to guess import option) inserting class imports with F4, add:
nmap <F4> <Plug>(JavaComplete-Imports-AddSmart)
imap <F4> <Plug>(JavaComplete-Imports-AddSmart)
" to enable usual (will ask for import option) inserting class imports with F5, add:
nmap <F5> <Plug>(JavaComplete-Imports-Add)
imap <F5> <Plug>(JavaComplete-Imports-Add)
" to add all missing imports with F6:
nmap <F6> <Plug>(JavaComplete-Imports-AddMissing)
imap <F6> <Plug>(JavaComplete-Imports-AddMissing)
" to remove all unused imports with F7:
nmap <F7> <Plug>(JavaComplete-Imports-RemoveUnused)
imap <F7> <Plug>(JavaComplete-Imports-RemoveUnused)

"----------"
" deoplete "
"----------"

let g:deoplete#enable_at_startup = 1
"let g:deoplete#enable_debug = 1
"let g:deoplete#enable_profile = 1
"call deoplete#enable_logging('DEBUG', 'tmp/deoplete.log')

" deoplete clang
let g:deoplete#sources#clang#libclang_path = '/usr/lib64/libclang.so'
let g:deoplete#sources#clang#clang_header = '/usr/lib64/clang'
"let g:deoplete#sources#clang#std = {'c': 'c11', 'cpp': 'c++1z', 'objc':
"'c11', 'objcpp': 'c++1z'}
"let g:deoplete#sources#clang#flags = ['-x', 'c']

" deoplete-clojure
let g:deoplete#keyword_patterns = {}
let g:deoplete#keyword_patterns.clojure = '[\w!$%&*+/:<=>?@\^_~\-\.#]*'

" deoplete-ternjs
let g:tern_request_timeout = 1
let g:tern_show_signature_in_pum = '0'  " This do disable full signature type on autocomplete
let g:tern#filetypes = ['jsx', 'javascript.jsx', 'vue']
let g:tern#command = ['tern']
let g:tern#arguments = ["--persistent"]

"-------------"
" vim-lexical "
"-------------"

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
" nerd-tree "
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
" tagbar "
"--------"

" toggle tagbar
nmap <F8> :TagbarToggle<CR>

"---------"
" airline "
"---------"

" set airline theme
let g:airline_theme = 'behelit'
