#! /bin/bash
export PYTHONPATH=$PYTHONPATH:/home/pi/Documents/SEAL/Python/joystick
export PYTHONPATH=$PYTHONPATH:/home/pi/Documents/SEAL/Python

#function killstuff {
#	jobs -p | xargs kill
#}

trap killstuff SIGINT

python3 joy_client.py

wait
