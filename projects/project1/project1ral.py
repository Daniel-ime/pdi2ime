import cv2
import numpy as np
from typing import Dict, Tuple

# Dicionário com algumas cores RAL comuns (código RAL: (R,G,B))
RAL_COLORS: Dict[str, Tuple[int, int, int]] = {
    'RAL 9010': (255, 255, 255),  # Branco Puro
    'RAL 9005': (0, 0, 0),        # Preto Brilhante
    'RAL 3020': (204, 6, 5),      # Vermelho Tráfego
    'RAL 5015': (0, 127, 167),    # Azul Céu
    'RAL 6029': (0, 111, 41),     # Verde Menta
    'RAL 1021': (243, 218, 11),   # Amarelo Colza
    'RAL 2004': (244, 70, 17),    # Laranja Puro
    'RAL 4006': (160, 52, 114),   # Púrpura Tráfego
    'RAL 8017': (69, 50, 46),     # Marrom Chocolate
    'RAL 7035': (215, 215, 215),  # Cinza Claro
}

def find_closest_ral_color(pixel: np.ndarray) -> str:
    """
    Encontra a cor RAL mais próxima para um dado pixel RGB
    """
    min_distance = float('inf')
    closest_ral = None
    
    # Converte o pixel para o formato correto se necessário
    if len(pixel.shape) > 1:
        pixel = pixel.flatten()
    
    for ral_code, ral_rgb in RAL_COLORS.items():
        # Calcula a distância euclidiana entre as cores
        distance = np.sqrt(sum((pixel - np.array(ral_rgb)) ** 2))
        
        if distance < min_distance:
            min_distance = distance
            closest_ral = ral_code
            
    return closest_ral

def process_image_to_ral(image_path: str, output_path: str) -> Dict[str, int]:
    """
    Processa uma imagem e mapeia suas cores para o sistema RAL
    
    Args:
        image_path: Caminho para a imagem de entrada
        output_path: Caminho para salvar a imagem processada
    
    Returns:
        Dicionário com contagem de cores RAL encontradas
    """
    # Lê a imagem
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Cria uma nova imagem para o resultado
    result_img = img.copy()
    height, width = img.shape[:2]
    
    # Dicionário para contar ocorrências de cada cor RAL
    ral_counts = {code: 0 for code in RAL_COLORS.keys()}
    
    # Processa cada pixel
    for y in range(height):
        for x in range(width):
            pixel = img[y, x]
            closest_ral = find_closest_ral_color(pixel)
            ral_counts[closest_ral] += 1
            
            # Substitui o pixel pela cor RAL mais próxima
            result_img[y, x] = RAL_COLORS[closest_ral]
    
    # Converte de volta para BGR e salva
    result_img = cv2.cvtColor(result_img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_path, result_img)
    
    return ral_counts

# Exemplo de uso
if __name__ == "__main__":
    # Substitua pelos caminhos reais das suas imagens
    input_image = "/Users/danielsantana/Projects/pdi2ime/projects/project1/pverm.jpeg"
    output_image = "imagem_ral.jpg"
    
    color_counts = process_image_to_ral(input_image, output_image)
    
    print("Distribuição de cores RAL na imagem:")
    for ral_code, count in color_counts.items():
        if count > 0:
            print(f"{ral_code}: {count} pixels")