#! /bin/bash
startit=0
export VLC_VERBOSE=-1
if [ -s /dev/shm/.processlock ]
then
	pid=$(cat /dev/shm/.processlock)
	if ps -p $pid >/dev/null
	then
		echo "Process ${pid} already running"
	else
		startit=1
	fi
else
	startit=1
fi

if [ $startit -eq 1 ]
then
	echo "starting up"
	source env/bin/activate
	flask run --host=0.0.0.0 &
	echo $! > /dev/shm/.processlock
fi
