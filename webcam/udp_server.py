import socket
import sys
import cv2
import pickle


udp_port = 8084
ip_dest = []
porc = 1.0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def add_ip(ip):
    global ip_dest
    ip_dest.append(ip)


def add_ip_range(a, b):
    for i in range(a, b+1):
        add_ip(f'192.168.246.{i}')

add_ip_range(1, 100)

#Abre a camera
cap = cv2.VideoCapture(0)

# Checa se a webcam abriu corretamente
if not cap.isOpened():
    raise IOError("Problema ao acessar webcam")

ret, frame = cap.read()
tam = 64*1024
while sys.getsizeof(pickle.dumps(frame)) >= tam:
    porc -= 0.01
    frame = cv2.resize(frame, None, fx=porc, fy=porc, interpolation=cv2.INTER_AREA)


print(f'Porcentagem={porc}')
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=porc, fy=porc, interpolation=cv2.INTER_AREA)

    cv2.imshow('Servidor', frame)

    c = cv2.waitKey(1)
    if c == 27: break

    frame = pickle.dumps(frame)
    for ip in ip_dest:
        sock.sendto(frame, (ip, udp_port))
        print(f'Frame enviado para {ip}')

cap.release()
cv2.destroyAllWindows
sock.close()