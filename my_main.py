import socket
import codecs
import struct
print("hello")
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
while True:
    packet, _ = s.recvfrom(65565)
    # print(packet)
    # print(type(packet))  # hi
    #packet_decode = packet.decode('ascii')
    packet_decode = codecs.encode(packet, 'hex')
    # print(packet_decode)
    # print(type(packet_decode))  # hi
    Eth_header = packet[:14]
    Eth_header_decode = codecs.encode(Eth_header, 'hex')
    # print(type(Eth_header_decode))
    # print(len(Eth_header_decode))
    Eth_header_decode_string = Eth_header_decode.decode("utf-8")
    print(f"Eth_header_from:{Eth_header_decode_string[0:2]}:{Eth_header_decode_string[2:4]}:{Eth_header_decode_string[4:6]}:{Eth_header_decode_string[6:8]}:{Eth_header_decode_string[8:10]}:{Eth_header_decode_string[10:12]}")
    print(f"Eth_header_to:{Eth_header_decode_string[12:14]}:{Eth_header_decode_string[14:16]}:{Eth_header_decode_string[16:18]}:{Eth_header_decode_string[18:20]}:{Eth_header_decode_string[20:22]}:{Eth_header_decode_string[22:24]}")
    print(f"EtherType:{Eth_header_decode_string[24:28]}")
    # print(Eth_header_decode)
    Ip_header = packet[14:34]
    Ip_header_decode = codecs.encode(Ip_header, 'hex')
    print(struct.unpack('!BBHHHBBH4s4s', Ip_header))
    # print("Ip_header_decode")
    # print(Ip_header_decode)
