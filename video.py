# Importando as libs 

import cv2 
import matplotlib as plt 


# Carregando o vídeo 
video_input = cv2.VideoCapture('la_cabra.mp4')

# Carregar o classificador de faces 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Definindo características do output com base no input
frame_width = int(video_input.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_input.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(video_input.get(cv2.CAP_PROP_FPS))

# Inicializando o gravador de vídeo da opencv e definindo o output
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('output.avi', fourcc, fps, (frame_width, frame_height))
 

while True:

        ret, frame = video_input.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (234, 224, 213), 2)

        # Escrevendo as predições no vídeo novo
        output.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video_input.release()
output.release() 
cv2.destroyAllWindows()


