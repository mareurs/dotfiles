#!/bin/bash

plugin_dirs=[python-mode, ctrlp.vim, vim-markdown, jedi-vim, vim-powerline,
vim-flake8, vim-less, vim-fugitive]



rm -rf {python-mode, ctrlp.vim, vim-markdown, jedi-vim, vim-powerline}
git clone https://github.com/klen/python-mode.git
git clone https://github.com/kien/ctrlp.vim.git
git clone https://github.com/hallison/vim-markdown.git
git clone https://github.com/davidhalter/jedi-vim.git
git clone https://github.com/Lokaltog/vim-powerline.git
git clone https://github.com/nvie/vim-flake8
git clone https://github.com/groenewege/vim-less.git
git clone https://github.com/tpope/vim-fugitive.git
