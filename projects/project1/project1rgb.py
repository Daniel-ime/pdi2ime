import cv2
import numpy as np
imagepath = '/Users/danielsantana/Projects/pdi2ime/projects/pverm.jpeg'
# Lê a imagem
img = cv2.imread(imagepath)

# Separa os canais
blue, green, red = cv2.split(img)

# Cria imagens para cada canal, preenchendo os outros canais com zero
zeros = np.zeros(img.shape[:2], dtype="uint8")
blue_channel = cv2.merge([blue, zeros, zeros])
green_channel = cv2.merge([zeros, green, zeros])
red_channel = cv2.merge([zeros, zeros, red])

cv2.imwrite('imagem_original.jpg', img)
cv2.imwrite('canal_vermelho.jpg', red_channel)
cv2.imwrite('canal_verde.jpg', green_channel)
cv2.imwrite('canal_azul.jpg', blue_channel)

# Mostra as imagens
cv2.imshow('Imagem Original', img)
cv2.waitKey(0)
cv2.imshow('Canal Vermelho', red_channel)
cv2.waitKey(0)
cv2.imshow('Canal Verde', green_channel)
cv2.waitKey(0)
cv2.imshow('Canal Azul', blue_channel)
cv2.waitKey(0)

# Espera pressionar qualquer tecla para fechar
cv2.waitKey(0)

# Fecha todas as janelas
cv2.destroyAllWindows()

