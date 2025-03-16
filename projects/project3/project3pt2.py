import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import morphology
from skimage import img_as_ubyte, img_as_bool

def aplicar_espessamento(imagem_path):
    """
    Aplica o algoritmo de espessamento (thickening) em uma imagem binária.
    
    Parâmetros:
    imagem_path (str): Caminho para a imagem de entrada
    num_iteracoes (int): Número de iterações do algoritmo de espessamento
    
    Retorna:
    tuple: (imagem_original, imagem_binarizada, resultado_espessamento)
    """
    # Carregar a imagem
    imagem = cv2.imread(imagem_path, cv2.IMREAD_GRAYSCALE)
    
    # Verificar se a imagem foi carregada corretamente
    if imagem is None:
        print(f"Erro ao carregar a imagem: {imagem_path}")
        return None, None, None
    
    # Binarizar a imagem (converter para preto e branco)
    _, imagem_bin = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)
    
    # Método: Utilizando scikit-image (que tem o espessamento implementado diretamente)
    # Converter para o formato booleano que o scikit-image espera
    imagem_bool = img_as_bool(imagem_bin)
    
    # Aplicar o algoritmo de espessamento
    resultado_scikit = morphology.binary_dilation(
        imagem_bool, 
        morphology.disk(1)
    )
    
    # Converter de volta para o formato de imagem do OpenCV
    resultado_espessamento = img_as_ubyte(resultado_scikit)
    

    
    plt.subplot(221)
    plt.title('Imagem Original')
    plt.imshow(imagem, cmap='gray')
    plt.axis('off')
    
    plt.subplot(222)
    plt.title('Imagem Binarizada')
    plt.imshow(imagem_bin, cmap='gray')
    plt.axis('off')
    
    plt.subplot(223)
    plt.title('Espessamento (scikit-image)')
    plt.imshow(resultado_espessamento, cmap='gray')
    plt.axis('off')
    
    
    plt.tight_layout()
    plt.show()
    
    return imagem, imagem_bin, resultado_espessamento

# Exemplo de uso
if __name__ == "__main__":
    # Substitua pelo caminho da sua imagem
    caminho_da_imagem = "/Users/danielsantana/Projects/pdi2ime/projects/project3/imagem_original.jpg"
    
    # Aplicar o algoritmo com 2 iterações
    imagem_original, imagem_bin, resultado_scikit = aplicar_espessamento(caminho_da_imagem)
    
    cv2.imwrite("espessamento_scikit.jpg", resultado_scikit)
   
    # Comparar as diferenças entre os métodos
    if imagem_original is not None:
        plt.figure(figsize=(10, 5))
        plt.subplot(121)
        plt.title('Diferença (Original vs scikit-image)')
        diferenca_scikit = cv2.absdiff(imagem_bin, resultado_scikit)
        plt.imshow(diferenca_scikit, cmap='hot')
        plt.axis('off')
  
        plt.tight_layout()
        plt.show()