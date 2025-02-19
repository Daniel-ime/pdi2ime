import cv2
import numpy as np

image_path='/Users/danielsantana/Projects/pdi2ime/projects/project1/pverm.jpeg'

img = cv2.imread(image_path)

    # Converte de BGR para HSV (OpenCV usa HSV ao invés de HSI)
hsi = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Cria cópias para manipular cada canal
h_modified = hsi.copy()
s_modified = hsi.copy()
i_modified = hsi.copy()

    # Modifica o canal H (Matiz)
    # Adiciona 30 graus ao matiz (lembrando que H vai de 0-179 no OpenCV)
h_modified[:,:,0] = (h_modified[:,:,0] + 30) % 180

    # Modifica o canal S (Saturação)
    # Aumenta a saturação em 30 (lembrando que vai de 0 a 255 no OpenCV)
s_modified[:,:,1] = cv2.add(s_modified[:,:,1], 30)

    # Modifica o canal I (Intensidade/Valor)
    # Aumenta o brilho em 30 (lembrando que vai de 0 a 255 no OpenCV)
i_modified[:,:,2] = cv2.add(i_modified[:,:,2], 30)

# Converte de volta para BGR para exibição
h_result = cv2.cvtColor(h_modified, cv2.COLOR_HSV2BGR)
s_result = cv2.cvtColor(s_modified, cv2.COLOR_HSV2BGR)
i_result = cv2.cvtColor(i_modified, cv2.COLOR_HSV2BGR)

    # Exibe as imagens
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.imshow('Modificacao no Matiz', h_result)
cv2.waitKey(0)
cv2.imshow('Modificacao na Saturacao', s_result)
cv2.waitKey(0)
cv2.imshow('Modificacao na Intensidade', i_result)
cv2.waitKey(0)
    # Salva as imagens
cv2.imwrite('matiz_modificado.jpg', h_result)
cv2.imwrite('saturacao_modificada.jpg', s_result)
cv2.imwrite('intensidade_modificada.jpg', i_result)

    # Espera uma tecla ser pressionada

cv2.destroyAllWindows()

