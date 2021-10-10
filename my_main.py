import socket
print("hello")
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
while True:
    packet, _ = s.recvfrom(65565)
    print(packet)
    print(type(packet))  # hi
    packet_decode = packet.decode('ascii')
    print(packet_decode)
    print(type(packet_decode))  # hi
