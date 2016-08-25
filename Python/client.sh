#cvlc http://172.20.10.5:8090 --sout file/ts:/home/kbaroni/test.h264 &

#vlc http://172.20.10.5:8090/video.h264

#vlc rtsp://172.20.10.5:8090/test.sdp
vlc &
python3 client.py
