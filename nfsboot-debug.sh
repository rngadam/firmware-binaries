DIR="$( cd "$( dirname "$0" )" && pwd )"
NFSROOT=`cat nfsroot.txt`
kexec -l $DIR/zImage-debug --append="mem=128M ip=dhcp noinitrd init=/sbin/init root=/dev/nfs nfsroot=$NFSROOT rw nfsrootdebug rootwait rootfstype=nfs"
kexec -e
