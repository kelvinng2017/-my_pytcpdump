import codecs
mac_add = ("d\x95\xe2\xff").encode('utf-8')
src_IP_hex = codecs.encode(mac_add, 'hex')
print(int(src_IP_hex[0:2], 16))
print(int(src_IP_hex[2:4], 16))
print(int(src_IP_hex[4:6], 16))
print(int(src_IP_hex[6:8], 16))
