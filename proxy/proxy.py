#!/usr/bin/env python3.10

import argparse
from validate_Args import is_valid_args
from start_proxy import start_proxy


parser = argparse.ArgumentParser(description='A simple proxy - man in the middle')

# define the arguments that the script receives.
parser.add_argument("listen-port", type=int, help="The port number that our proxy receives clients from.")
parser.add_argument("fake-ip", type=str, help="The IP to bind with outgoing requests to the server")
parser.add_argument("server-ip", type=str, help="The server IP address")

args = vars(parser.parse_args())

listen_port = args['listen-port']
fake_ip = args['fake-ip']
server_ip = args['server-ip']


# listen_port = 11233
# fake_ip = '127.0.0.1'
# server_ip = '127.0.0.1'

if not is_valid_args(listen_port, fake_ip, server_ip):
    print("Invalid Arguments, quitting the script.")
else:
    print("starting the proxy.")
    start_proxy(listen_port, fake_ip, server_ip)

