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
