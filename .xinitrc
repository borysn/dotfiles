source "$HOME/.zprofile"
gnome-keyring-daemon --start --components=pkcs11,secrets,ssh
eval `ssh-agent -s`
xrdb -merge "$HOME/.Xresources"
compton -cCGfF -b -i 0.75 --vsync opengl
urxvtd -q -o -f
echo -e 'connect FC:58:FA:57:64:CE\nselect 00:1A:7D:DA:71:13\nquit' | bluetoothctl
exec dbus-launch i3
