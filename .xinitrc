xrdb -load "$HOME/.Xresources"
compton -cCGfF -b -i 0.75 --vsync opengl
exec dbus-launch i3
