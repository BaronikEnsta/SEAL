<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> origin/master
#raspivid -t 0 -n --width 720 -h 576 -o - | cvlc stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264 &

#raspivid -ih -w 640 -h 480 -b 6000000 -t 0 -o - | cvlc stream:///dev/stdin --sout '#rtp{dst=172.20.10.6,port=8090,sdp=rtsp://172.20.10.5:8090/test.sdp}'

#raspivid -ih -w 640 -h 480 -b 6000000 -t 0 -o - | cvlc stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/video.h264}' --sout-keep

#vlc -vvv /dev/video0 --sout '#rtp{dst=172.20.10.5,port=1234,sdp=rtsp://172.20.10.5:8090/test.sdp}'

#raspivid -ih -w 640 -h 480 -b 6000000 -t 0 -o - | cvlc --demux h264 --sout '#standard{access=http,mux=ts,dst=:8090/video.h264}' stream:///dev/stdin 

#raspivid -ih -md 6 -b 8000000 -fps 15 -t 0 -o - | cvlc --demux h264 --sout '#standard{access=http,mux=ts,dst=:8090/video.h264}' stream:///dev/stdin
vlc &
python3 serveur.py 
<<<<<<< HEAD
=======
=======
raspivid -t 0 -n --width 720 -h 576 -o - | cvlc stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264 &

#python3 serveur.py 
>>>>>>> origin/master
>>>>>>> origin/master
