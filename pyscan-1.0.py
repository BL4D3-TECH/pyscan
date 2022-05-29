import sys
import socket

print('''
BY BL4D3
''')

ip_target = socket.gethostbyname(input("Which IP you will scan: "))
print("Scanning --> "+ ip_target)
try:
    for ports in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        resultado = s.connect_ex((ip_target, ports))
        if resultado == 0:
            print("the port {} is open".format(ports))
        s.close()
except:
    print("\n going down :(")
    sys.exit(0)