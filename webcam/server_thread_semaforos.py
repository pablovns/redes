#Biblioteca sockets
import socket
import pickle
import time

from threading import Thread
from threading import Semaphore

import cv2

frame_g = None

#inicializa semáforo
semaforo_g = Semaphore(1)

#Thread que acessa a camera e lê os frames
class ThreadCam(Thread):
    def __init__ (self):
        Thread.__init__(self)

        #Abre a camera
        self.cap = cv2.VideoCapture(0)

        # Check if the webcam is opened correctly
        if not self.cap.isOpened():
            raise IOError("Problema ao acessar webcam")
    
    def run(self):
        global frame_g
        while True:
            #Obtém o frame da camera
            ret, frame = self.cap.read()
            #Redimensiona a imagem
            frame = cv2.resize(frame, None, fx=1.0, fy=1.0, interpolation=cv2.INTER_AREA)
            #Copia o frame para o frame global
            semaforo_g.acquire()
            frame_g = frame
            semaforo_g.release()



class ThreadCamServer(Thread):
    def __init__ (self, addr, conn):
        Thread.__init__(self)
        self.addr = addr
        self.conn = conn

    def run(self):
        global frame_g
        
        #Empacota o frame e envia
        semaforo_g.acquire()
        data_object = pickle.dumps(frame_g)
        semaforo_g.release()

        if data_object:
            self.conn.send(data_object)
            # self.conn.send(''.encode())


        #Fecha a conexao
        conn.close()
        # print('== Cliente desconectado ==')



#Porta do servidor
port = 8084

#Objeto socket
serv  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Associa o socket a uma porta local
serv.bind(('0.0.0.0',port))
serv.listen()

#Acessa camera em background
Camera = ThreadCam()
Camera.start()

#Servidor fica aguardando conexões
while True:
    # print(f'*** Servidor aguardando conexões na porta {port} ***')
    conn, addr = serv.accept()

    #Ao receber uma conexão, cria uma thread para enviar dados ao cliente
    # print(f'== Conexao recebida de {addr} ==')
    ThreadCamServer(addr, conn).start() 
 
    