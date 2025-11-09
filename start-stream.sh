UDP_PORT=5000
UDP_IP=127.0.0.1

rpicam-vid -t 0 --inline --nopreview --bitrate 4000000 --framerate 10 -pkt_size 1316 -o udp://$UDP_IP:$UDP_PORT
