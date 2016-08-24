raspivid -t 0 -n --width 720 -h 576 -o - | cvlc stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264 &

#python3 serveur.py 
