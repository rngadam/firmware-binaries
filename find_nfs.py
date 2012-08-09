#!/usr/bin/env python
# Based on:
# http://dbus.freedesktop.org/doc/dbus-python/doc/tutorial.html
# http://avahi.org/wiki/PythonBrowseExample
#
# client:  apt-get install python-avahi python-gobject-2 python-dbus
#
# server: /etc/avahi/services/nfs.service
#
# <?xml version="1.0" standalone='no'?><!--*-nxml-*-->
# <!DOCTYPE service-group SYSTEM "avahi-service.dtd">
#
# <!-- This file is part of udisks -->
# <service-group>
#   <name replace-wildcards="yes">Lophilo OS on %h</name>
#   <service>
#     <type>_nfs._tcp</type>
#     <txt-record>path=/home/rngadam/lophilo.nfs</txt-record>
#   </service>
# </service-group>

import dbus, gobject, avahi
from dbus import DBusException
import gobject
# Looks for iTunes shares
from dbus.mainloop.glib import DBusGMainLoop

DBusGMainLoop(set_as_default=True)
loop = gobject.MainLoop()

TYPE = "_nfs._tcp"

def service_resolved(*args):
    if args[2].startswith('Lophilo OS'):
    	path_param = ''.join(['%c' % a for a in args[9][0]])
    	path = path_param.split('=')[1]
    	print '%s:%s' % (args[7], path)
    	loop.quit()

def print_error(*args):
    print 'error_handler'
    print args[0]

def myhandler(interface, protocol, name, stype, domain, flags):
    #print "Found service '%s' type '%s' domain '%s' " % (name, stype, domain)

    if flags & avahi.LOOKUP_RESULT_LOCAL:
            # local service, skip
            pass

    server.ResolveService(interface, protocol, name, stype, 
        domain, avahi.PROTO_UNSPEC, dbus.UInt32(0), 
        reply_handler=service_resolved, error_handler=print_error)


bus = dbus.SystemBus()

server = dbus.Interface( bus.get_object(avahi.DBUS_NAME, '/'),
        'org.freedesktop.Avahi.Server')

sbrowser = dbus.Interface(bus.get_object(avahi.DBUS_NAME,
        server.ServiceBrowserNew(avahi.IF_UNSPEC,
            avahi.PROTO_INET, TYPE, 'local', dbus.UInt32(0))),
        avahi.DBUS_INTERFACE_SERVICE_BROWSER)
sbrowser.connect_to_signal('ItemNew', myhandler)


loop.run()