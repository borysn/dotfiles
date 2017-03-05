# source profile
source "$HOME/.profile"

# urxvt daemon
urxvtd --quiet --opendisplay --fork

# load .Xresources
xrdb -load "$HOME/.Xresources"

# start compton
compton -cCGfF -b -i 0.75 --vsync opengl

# start i3
exec dbus-launch i3

