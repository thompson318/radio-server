#! /bin/bash
startit=0
if [ -s .processlock ]
then
	pid=$(cat .processlock)
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
	echo $! > .processlock
fi
