sudo apt-get update
sudo apt-get install -y xvfb x11vnc websockify novnc
Xvfb :1 -screen 0 1024x768x16 &
export DISPLAY=:1
x11vnc -display :1 -nopw -listen localhost -xkb &
websockify --web /usr/share/novnc 6080 localhost:5900 &