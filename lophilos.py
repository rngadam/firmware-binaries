#!/usr/bin/env python
from subprocess import check_output
import my_ip

class LophiloException(Exception):
	pass

def find_hostname(name):
	resolve = check_output(('avahi-resolve -a -n -4 %s' % name).split(' ')).strip()
	if not resolve:
		raise LophiloException('no resolution for %s' % name)
	return resolve.split('\t')[1]

def resolve(name):
	print '%s = %s' % (name, find_hostname(name))

if __name__ == "__main__":
	try:
		resolve("lophilo1.local")
		i = 1
		while True:
			i = i + 1
			name = "lophilo1-%d.local" % i
			resolve(name)
	except LophiloException, e:
		print "no more local hosts"
