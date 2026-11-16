import cv2 as cv
import os

imagen = 'media/bmw.jpg'

if not os.path.exists(imagen):
    print(f"La imagen no existe")
    exit()

lectura = cv.imread(imagen)
# Apliqué esto debido a que la foto era demasiado grande, el resto de lógica continúa igual. 
resize = cv.resize(lectura, (0, 0), fx=0.5, fy=0.5)
gris = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)

edges = cv.Canny(gris, 100, 200)

cv.putText(edges, 'Foto procesada', (30, 50), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

cv.imshow('Foto original', resize)
cv.imshow('Imagen con canny', edges)

print("Presiona cualquier tecla en la ventana de la imagen para cerrar")
cv.waitKey(0)
cv.destroyAllWindows()