# .xinitrc
# author: borysn
# license: what's a license?

source "$HOME/.zprofile"
gnome-keyring-daemon --start --components=pkcs11,secrets,ssh
eval `ssh-agent -s`
xrdb -merge "$HOME/.Xresources"
compton -cCGfF -b -i 0.75 --vsync opengl
urxvtd -q -o -f
syndaemon -d -i 1.0 -K -R -t
exec dbus-launch i3
