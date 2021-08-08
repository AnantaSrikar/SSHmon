if [ $# -ne 2 ]
	then
		echo "No arguments supplied. Logging will NOT happen"
		exit
fi

UNAME=$1
UPID=$2

if [ ! -d "/tmp/$UNAME" ]; then
	mkdir /tmp/$UNAME
fi
filename=$(date +%Y-%m-%d_%H-%M-%S)
strace -s 16384 -p $UPID -e read 2>&1 | stdbuf -oL grep -oP '"\K[^"\047]+(?=["\047])' >> /tmp/$UNAME/$filename.log
python3 clean.py --file $filename.log --user $UNAME
cp $filename.log-f.log /tmp/$UNAME/
