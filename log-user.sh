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

strace -s 16384 -p $UPID -e read 2>&1 | stdbuf -oL grep -oP '"\K[^"\047]+(?=["\047])' >> /tmp/$UNAME/$(date +"%Y%m%d-%T").log
