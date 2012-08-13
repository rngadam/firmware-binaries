#!/bin/sh
# assuming that the lophilo source directory
# is at the same location than the Lophilo OS
export NAME=`/media/BOOT/find_nfs.py`
echo "Resolved as $NAME"
mkdir -p ${HOME}/lophilo
mount -t nfs -o cto ${NAME%.nfs} ${HOME}/lophilo
