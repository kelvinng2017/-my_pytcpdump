import sys
import socket
import signal
from utils.sniffer import Sniffer

def exit(signum, frame):
    global sniffer
    del sniffer
    print()
    sys.exit()

signal.signal(signal.SIGINT, exit)
signal.signal(signal.SIGTERM, exit)


verbose = 1
ifc='fe80::920:c9e9:f0d2:7b27'
sniffer = Sniffer(ifc=ifc, verb=verbose)
sniffer.start()
