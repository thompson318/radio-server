#! /bin/bash
startit=0
export VLC_VERBOSE=-1
if [ -s /dev/shm/radio.lock ]
then
	pid=$(cat /dev/shm/radio.lock)
	if ps -p $pid >/dev/null
	then
		echo "Radio running on process ${pid}."
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
	echo $! > /dev/shm/radio.lock
fi
