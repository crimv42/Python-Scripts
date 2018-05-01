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

def get_port_range():
    start_port = int(input("Starting port: "))
    end_port = int(input("Ending port: "))
    port_range = (start_port, (end_port + 1))
    return port_range

def port_scan(remote_server_ip):
    port_range = get_port_range()
    try:
        print ("\n {0:1s}: {1:>9}:".format('Port', 'Status'))
        for port in range(port_range[0], port_range[1]):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((remote_server_ip, port))
            if result == 0:
                print (" {0:< 5d} {1:>10}".format(port, 'Open'))
            else:
                print (" {0:< 5d} {1:>10}".format(port, 'Closed'))
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
