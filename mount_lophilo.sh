#!/bin/sh
# assuming that the lophilo source directory
# is at the same location than the Lophilo OS
export NAME=`/media/BOOT/find_nfs.py`
export MOUNT=/home/lophilo/lophilo
echo "Resolved as $NAME"
mkdir -p ${MOUNT}
sudo mount -t nfs -o cto ${NAME%.nfs} ${MOUNT}
if [ "$USER" != "lophilo" ]; then
	su - lophilo
fi
