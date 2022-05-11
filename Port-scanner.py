import sys
import socket

print('''
BY AL2AL2624
''')

ip_objetivo = socket.gethostbyname(input("Introduzca la IP objetivo : "))

print("Escaneando --> "+ ip_objetivo)

try:
    for ports in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        resultado = s.connect_ex((ip_objetivo, ports))
        if resultado == 0:
            print("El puerto {} esta abierto".format(ports))
        s.close()
except:
    print("\n Saliendo...")
    sys.exit(0)