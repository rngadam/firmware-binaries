#!/usr/bin/env python
def get_lophilo_version():
	try:
	    return '%s' % file('/etc/lophilo_version').readline()
	except:
	    return 'nfs'

if __name__ == "__main__":
	print get_lophilo_version()