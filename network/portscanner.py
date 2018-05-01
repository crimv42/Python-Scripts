#!/usr/bin/env python3
import socket
import subprocess
import sys
import argparse
from datetime import datetime
from time import sleep

# Ask for input
def get_host():
    remote_server = input("Enter a remote hostname to scan: ")
    try:
        remote_server_ip = socket.gethostbyname(remote_server)
        return remote_server_ip
    except socket.gaierror:
        print ("Could not resolve host!")
        sys.exit()

# Print a nice banner with information on which host we are about to scan
def banner(remote_server_ip):
    message = ("-" * 60 + "\nPlease wait, scanning remote host: %s\n" 
                % remote_server_ip + "-" * 60)
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

def port_scan(remote_server_ip, full_scan=False):
    port_range = get_port_range()
    print (banner(remote_server_ip))
    
    try:
        print ("\n {0:1s}: {1:>9}:".format('Port', 'Status'))
        for port in range(port_range[0], port_range[1]):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((remote_server_ip, port))
            if full_scan == True:
                if result == 0:
                    print (" {0:< 5d} {1:>10}".format(port, 'Open'))
                else:
                    print (" {0:< 5d} {1:>10}".format(port, 'Closed'))
                sock.close()
            else:
                if result == 0:
                    print (" {0:< 5d} {1:>10}".format(port, 'Open'))
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

## Parse any arguments
parser = argparse.ArgumentParser(description="Set optional flags for PortScanner")
parser.add_argument('-a', '--all', action='store_true', help="Display all ports. Closed, and Open")
parser.add_argument('-i', '--ip', help="Provide direct IP of Host")
args = parser.parse_args()

# Clear the screen
subprocess.call('clear', shell=True)

# Start the program

if args.all == True:
    if args.ip != None:
        remote_server_ip = args.ip
        time_1 = time_spent('start')
        print (port_scan(remote_server_ip, args.all))
    else:
        remote_server_ip = get_host()
        time_1 = time_spent('start')
        print (port_scan(remote_server_ip, args.all))
else:
    if args.ip != None:
        remote_server_ip = args.ip
        time_1 = time_spent('start')
        print (port_scan(remote_server_ip))
    else:
        remote_server_ip = get_host()
        time_1 = time_spent('start')
        print (port_scan(remote_server_ip))


print ("Time spent: ", time_spent('stop', time_1))
