import socket
import codecs
print("hello")
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
while True:
    packet, _ = s.recvfrom(65565)
    print(packet)
    print(type(packet))  # hi
    #packet_decode = packet.decode('ascii')
    packet_decode = codecs.encode(packet, 'hex')
    print(packet_decode)
    print(type(packet_decode))  # hi
    Eth_header = packet[:14]
    Eth_header_decode = codecs.encode(Eth_header, 'hex')
    print(f"Eth_header_from:{Eth_header_decode[0:2]}:{Eth_header_decode[2:4]}:{Eth_header_decode[4:6]}:{Eth_header_decode[6:8]}:{Eth_header_decode[8:10]}:{Eth_header_decode[10:12]}")
    print(Eth_header_decode)
    Ip_header = packet[14:34]
    Ip_header_decode = codecs.encode(Ip_header, 'hex')
    print("Ip_header_decode")
    print(Ip_header_decode)
