#!/usr/bin/env python

import urllib
import socket
import time

username = ""
password = ""
hostname = ""  # your domain name hosted on no-ip.com

while True:
    # Gets the current public IP of the host machine using curl.
    myip = urllib.urlopen('http://api.ipify.org').read().strip()

    # Gets the existing DNS IP pointing to the hostname.
    old_ip = socket.gethostbyname(hostname)

    # No-IP API - Dynamic DNS update using curl.
    # https://www.noip.com/integrate/request.
    def update_dns(config):
        urllib.urlopen('http://%s:%s@dynupdate.no-ip.com/nic/update?hostname=%s&myip=%s' % config)

    # Print current IP and old IP for reference.
    print "Current IP: %s" % myip
    print "Old IP: %s" % old_ip

    # Update only when IP is different.
    if myip != old_ip:
        update_dns((username, password, hostname, myip))

    # Sleep for 3 minutes before checking again.
    time.sleep(180)

