# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=500
bindkey -e
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/lipastomies/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

if [ -f ~/.aliases ]; then
    . ~/.aliases
fi

autoload -U colors && colors

#PROMPT="%{$fg_bold[green]%}%D{"   >"}%{$reset_color %}"

PROMPT=%F{white}%D{"["}%f%F{cyan}%1d%f%F{white}%D{"] "}%f%F{yellow}%D{">"}%f%B%F{yellow}%D{">"}%f%b%B%F{white}%D{">"}%f%b
#RPROMPT=%B%F{yellow}%D{"<<<"}%f%b

RPROMPT=%B%F{white}%D{"<"}%f%b%B%F{yellow}%D{"<"}%f%b%F{yellow}%D{"<"}%f

  
