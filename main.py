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
ifc='08:00:27:1f:67:f4'
sniffer = Sniffer(ifc=ifc, verb=verbose)
sniffer.start()
