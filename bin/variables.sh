# ******************************************************************************
#   COLOR VARIABLES (for Dark Terminal Backgrounds)
# ******************************************************************************

# Very Useful Article about Mac Bash Colors
# https://unix.stackexchange.com/questions/148/colorizing-your-terminal-and-shell-environment

# Foreground Colors
fgRed=$(tput setaf 9)       ; fgGreen=$(tput setaf 10)      ; fgBlue=$(tput setaf 75)
fgMagenta=$(tput setaf 13)  ; fgYellow=$(tput setaf 11)     ; fgCyan=$(tput setaf 14)
fgWhite=$(tput setaf 15)    ; fgBlack=$(tput setaf 0)       ; fgGrey=$(tput setaf 8)

# Background Colors
bgRed=$(tput setab 9)       ; bgGreen=$(tput setab 10)      ; bgBlue=$(tput setab 75)
bgMagenta=$(tput setab 13)  ; bgYellow=$(tput setab 11)     ; bgCyan=$(tput setab 14)
bgWhite=$(tput setab 15)    ; bgBlack=$(tput setab 0)       ; bgGrey=$(tput setab 8)

# Set variables for font weight and text decoration
B=$(tput bold) ; U=$(tput smul) ; C=$(tput sgr0)  ; RV=$(tput rev);
# NOTE: ${C} clears the current formatting

EM='\033[3m'
UNDERLINE='\033[4m'
ITALIC='\033[3m'
br=$'\n'
