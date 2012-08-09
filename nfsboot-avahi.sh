DIR="$( cd "$( dirname "$0" )" && pwd )"
NFSROOT=`$DIR/find_nfs.py`
kexec -l $DIR/zImage --append="mem=128M ip=dhcp noinitrd init=/sbin/init root=/dev/nfs nfsroot=$NFSROOT rw nfsrootdebug rootwait rootfstype=nfs"
echo -n "current timestamp: " 
date
echo $NFSROOT
kexec -e
