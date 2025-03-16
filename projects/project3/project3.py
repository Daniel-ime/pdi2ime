import cv2
import numpy as np
import matplotlib.pyplot as plt

def aplicar_hit_or_miss(imagem_path,kernel):
    # Carregar a imagem
    imagem = cv2.imread(imagem_path, cv2.IMREAD_GRAYSCALE)
    
    # Verificar se a imagem foi carregada corretamente
    if imagem is None:
        print(f"Erro ao carregar a imagem: {imagem_path}")
        return
    
    # Binarizar a imagem (converter para preto e branco)
    _, imagem_bin = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)
    
    # Definir os kernels para o hit-or-miss
    # Kernel para detectar cantos superiores direitos, por exemplo

    
    # Aplicar o algoritmo hit-or-miss
    resultado = cv2.morphologyEx(imagem_bin, cv2.MORPH_HITMISS, kernel)
    
    # Mostrar os resultados
    plt.figure(figsize=(15, 5))
    
    plt.subplot(131)
    plt.title('Imagem Original')
    plt.imshow(imagem, cmap='gray')
    plt.axis('off')
    
    plt.subplot(132)
    plt.title('Imagem Binarizada')
    plt.imshow(imagem_bin, cmap='gray')
    plt.axis('off')
    
    plt.subplot(133)
    plt.title('Resultado Hit-or-Miss')
    plt.imshow(resultado, cmap='gray')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    return imagem, imagem_bin, resultado

if __name__ == "__main__":
    caminho_da_imagem = "/Users/danielsantana/Projects/pdi2ime/projects/project3/imagem_original.jpg"
    
    kernel1 = np.array([
        [0, 1, 1],
        [-1, 1, 1],
        [-1, -1, 0]
    ], dtype=np.int8)
    
    # Aplicar o algoritmo
    imagem_original, imagem_bin, resultado_hit_or_miss = aplicar_hit_or_miss(caminho_da_imagem,kernel1)
    
    cv2.imwrite("resultado_hit_or_missk1.jpg", resultado_hit_or_miss)
    
    # outros kernels
    kernel_vertical = np.array([
        [-1, 1, -1],
        [-1, 1, -1],
        [-1, 1, -1]
    ], dtype=np.int8)
    imagem_original, imagem_bin, resultado_hit_or_miss = aplicar_hit_or_miss(caminho_da_imagem,kernel_vertical)
    cv2.imwrite("binary.jpg", imagem_bin)
    cv2.imwrite("resultado_hit_or_misskv.jpg", resultado_hit_or_miss)
    
    kernel_horizontal = np.array([
        [-1, -1, -1],
        [1, 1, 1],
        [-1, -1, -1]
    ], dtype=np.int8)
    
    imagem_original, imagem_bin, resultado_hit_or_miss = aplicar_hit_or_miss(caminho_da_imagem,kernel_horizontal)
    
    cv2.imwrite("resultado_hit_or_misskh.jpg", resultado_hit_or_miss)