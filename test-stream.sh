UDP_PORT=5000
UDP_IP=127.0.0.1

ffplay -probesize 32 -analyzeduration 0 udp://$UDP_IP:$UDP_PORT
