source "$HOME/.zprofile"
xrdb -merge "$HOME/.Xresources"
compton -cCGfF -b -i 0.75 --vsync opengl
urxvtd -q -o -f
exec dbus-launch i3
