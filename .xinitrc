source "$HOME/.zprofile"
gnome-keyring-daemon --start --components=pkcs11,secrets,ssh
eval `ssh-agent -s`
xrdb -merge "$HOME/.Xresources"
compton --respect-prop-shadow -b
urxvtd -q -o -f
echo -e 'connect FC:58:FA:57:64:CE\nquit' | bluetoothctl
echo -e 'connect FC:58:FA:97:CE:78\nquit' | bluetoothctl
exec dbus-launch i3
