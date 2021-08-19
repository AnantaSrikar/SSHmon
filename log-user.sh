if [ $# -ne 2 ]
	then
		echo "No arguments supplied. Logging will NOT happen"
		exit
fi

UNAME=$1
UPID=$2

if [ ! -d "$LOG_PATH/$UNAME" ]; then
	mkdir $LOG_PATH/$UNAME
fi
filename="$(date +%Y-%m-%d_%H-%M-%S)-temp"
strace -s 16384 -p $UPID -e read 2>&1 | stdbuf -oL grep -oP '"\K[^"\047]+(?=["\047])' >> $LOG_PATH/$UNAME/$filename.log
python3 clean.py --file $filename.log --user $UNAME