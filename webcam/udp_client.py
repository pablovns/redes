import socket
import pickle
import cv2


udp_ip = "192.168.246.25"
udp_port = 8084

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udp_ip, udp_port))

while True:
    data, addr = sock.recvfrom(128*1024)
    frame = pickle.loads(data)
    cv2.imshow("Cliente", frame)

    if cv2.waitKey(1) == 27: break

cv2.destroyAllWindows()
sock.close()