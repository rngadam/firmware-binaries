#!/usr/bin/env python
from subprocess import check_output
import my_ip

def find_hostname():
	resolve = check_output(('avahi-resolve -a -4 %s' % my_ip.get_ip_address('eth0')).split(' ')).strip()
	return resolve.split('\t')[1]

if __name__ == "__main__":
	print find_hostname()