# ******************************************************************************
#   CURSOR AND WINDOW MANIPULATION
# ******************************************************************************

desktopsize () {
    dimensions=$(osascript -e 'tell application "Finder" to get bounds of window of desktop')
    screen_width=$(echo "${dimensions}" | cut -d ',' -f 3 | sed 's/^ *//;s/ *$//');
    screen_height=$(echo "${dimensions}" | cut -d ',' -f 4 | sed 's/^ *//;s/ *$//');
}

windowposition () {
    xy=$(osascript -e 'tell application "System Events" to set frontApp to name of first application process whose frontmost is true
    tell application frontApp to get the bounds of the front window');
    x=$(echo "${xy}" | cut -d ',' -f 1 | sed 's/^ *//;s/ *$//');
    y=$(echo "${xy}" | cut -d ',' -f 2 | sed 's/^ *//;s/ *$//');
}

mouseposition () {
    mouse_xy=(echo $(MouseTools -location))
    mouse_x=${mouse_xy[1]}
    mouse_y=${mouse_xy[2]}
}


# ******************************************************************************
#   SNAP FUNCTION FOR TERMINAL
# ******************************************************************************

snap () {
    osascript "$SRC/bin/snap-$1.scpt"
    MouseTools -releaseMouse
}


# ******************************************************************************
#   ALERTS AND FORMATTING
# ******************************************************************************

# Simple Yellow Alert
alert () { echo; tput bold; print -yellow "$1"; tput sgr0; }

# SECTION HEADER with Alignment Options
# Usage: header (-a -c) "Simple Section Header" "Insert a descriptive subheader"

header () {
    # Capture Alignment and Color Arguments ------------------------------------
    while getopts a:c: flag; do
        case "${flag}" in
            a|--align)
                local alignment=${OPTARG}
            ;;

            c|--color)
                local color=${OPTARG}

                case "$color" in
                    black)      local colorID=0;    local lineColor=${fgBlack};;
                    red)        local colorID=9;    local lineColor=${fgRed};;
                    green)      local colorID=10;   local lineColor=${fgGreen};;
                    yellow)     local colorID=11;   local lineColor=${fgYellow};;
                    blue)       local colorID=75;   local lineColor=${fgBlue};;
                    cyan)       local colorID=14;   local lineColor=${fgCyan};;
                    white|*)    local colorID=15;   local lineColor=${C};;
                esac
            ;;
        esac
    done

    # Capture Text -------------------------------------------------------------
    # There's likely a more efficient way to do this, but I'm not sure what it is yet.

    local title="$1"
    local subtitle="$2"

    if [[ $alignment || $color ]]; then
        local title="$3"
        local subtitle="$4"
    fi

    if [[ $alignment && $color ]]; then
        local title="$5"
        local subtitle="$6"
    fi

    test ! $color && local colorID=10;

    # Print Stuff --------------------------------------------------------------

    echo -e "\n$(tput setaf $colorID)$(hr \*)${C}"

    case "$alignment" in
        center)
            # Print Colored Title
            tput bold; tput setaf $colorID;
            center "$title"
            tput sgr0;

            # Print Grey Subtitle
            tput setaf 8;
            center "$subtitle";
            tput sgr0;
        ;;

        right)
            # Print Colored Title
            tput bold; tput setaf $colorID;
            # right "$(echo -e "$title\t")";
            echo -e "$(right "$title\t")\t"
            tput sgr0;

            # Print Grey Subtitle
            tput setaf 8;
            # right "$(echo -e "$subtitle\t")";
            echo -e "$(right "$subtitle\t")\t"
            tput sgr0;
        ;;

        left|*)
            # Print Colored Title
            tput bold; tput setaf $colorID;
            echo -e "\t$title"
            tput sgr0;

            # Print Grey Subtitle
            tput setaf 8;
            echo -e "\t$subtitle";
            tput sgr0;
        ;;
    esac

    echo -e "$(tput setaf $colorID)$(hr \*)${C}\n"

    OPTIND=1
}
