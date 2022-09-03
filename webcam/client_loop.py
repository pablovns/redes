import socket
import pickle 
import numpy as np

import cv2

#Porta do servidor
PORT = 8084

#Endereço do servidor
dest = 'localhost'

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#greyscale filter
def greyscale(img):
    greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return greyscale

# brightness adjustment
def bright(img, beta_value ):
    img_bright = cv2.convertScaleAbs(img, beta=beta_value)
    return img_bright

#sepia effect
def sepia(img):
    img_sepia = np.array(img, dtype=np.float64) # converting to float to prevent loss
    img_sepia = cv2.transform(img_sepia, np.matrix([[0.272, 0.534, 0.131],
                                    [0.349, 0.686, 0.168],
                                    [0.393, 0.769, 0.189]])) # multipying image with special sepia matrix
    img_sepia[np.where(img_sepia > 255)] = 255 # normalizing values greater than 255 to 255
    img_sepia = np.array(img_sepia, dtype=np.uint8)
    return img_sepia

# invert filter
def invert(img):
    inv = cv2.bitwise_not(img)
    return inv

#loop para conectar e obter os frames
while True: 

    #Objeto socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Conecta ao servidor
    # print(f'== Conectando a {dest}:{PORT}==')
    client.connect((dest, PORT))

    data = []
    while True:
        # print('#', end='')
        pacote = client.recv(4096)
        if not pacote: 
            break
        data.append(pacote)


    if data:
        frame = pickle.loads(b"".join(data))
        # frame = pickle.loads(pacote)

        # frame = greyscale(frame)
        # frame = bright(frame, 100)
        # frame = sepia(frame)
        # frame = invert(frame)

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Imagem', frame)

        c = cv2.waitKey(1)
        if c == 27:
            break

#Fecha a conexão
client.close()

#Fecha todas as janelas
cv2.destroyAllWindows()
