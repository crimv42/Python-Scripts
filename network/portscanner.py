#!/usr/bin/env python3
import socket
import subprocess
import sys
from datetime import datetime
from time import sleep

# Clear the screen
subprocess.call('clear', shell=True)

# Ask for input
def get_host():
    remote_server = input("Enter a remote host to scan: ")
    print (remote_server)
    try:
        remote_server_ip = socket.gethostbyname(remote_server)
        return remote_server_ip
    except socket.gaierror:
        print ("Could not resolve host!")
        sys.exit()

# Print a nice banner with information on which host we are about to scan
def banner(remote_server_ip):
    message = ("-" * 60 + "\nPlease wait, scanning remote host: %s\n" % remote_server_ip + "-" * 60)
    #print ("-" * 60)
    #print ("Please wait, scanning remote host", remote_server_ip)
    #print ("-" * 60)
    return message

def time_spent(x, time=datetime.now()):
    x.lower()
    if x == 'start':
         return time
    elif x == 'stop':
        time_2 = datetime.now()
        total = time_2 - time
        return total


def port_scan(remote_server_ip):
    try:
        for port in range(1,25):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remote_server_ip, port))
            if result == 0:
                print ("Port {}:    Open".format(port))
            sock.close()
        return ("\nScan Completed!\n")
    except KeyboardInterrupt:
        print ("\nYou pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print ("Hostname could not be resolved. Exiting!")
        sys.exit()

    except socket.error:
        print ("Couldn't connect to server!")
        sys.exit()



remote_server_ip = get_host()
print (banner(remote_server_ip))

time_1 = time_spent('start')
print (port_scan(remote_server_ip))

print ("Time spent: ", time_spent('stop', time_1))
