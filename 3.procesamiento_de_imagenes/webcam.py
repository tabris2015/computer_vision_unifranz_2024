import numpy as np
import cv2

# para camaras ip: 'rtsp://192.168.1.64/1'
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("error de captura!")

while True:
    # lectura de un frame
    ret, frame = cap.read()

    # procesar frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 180, 200)
    out = gray * 0.001 + edges
    print(np.mean(gray), np.amax(edges), np.amax(out))
    # desplegar imagenes en la pantalla
    cv2.imshow("input", frame)
    cv2.imshow("output", out)

    # detectar el final del programa
    c = cv2.waitKey(1)

    # salir con tecla 'esc'
    if c == 27:
        # salir del bucle
        break

# liberar recursos
cap.release()
cv2.destroyAllWindows()