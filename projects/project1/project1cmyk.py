from PIL import Image
import numpy as np

def manipular_canais_cmyk_pil(caminho_imagem):
    # Abre a imagem
    imagem = Image.open(caminho_imagem)
    
    # Converte para CMYK
    imagem_cmyk = imagem.convert('CMYK')
    
    # Separa os canais
    c, m, y, k = imagem_cmyk.split()
    
    # Função auxiliar para aumentar a intensidade de um canal
    def aumentar_intensidade(canal, fator=1.5):
        canal_array = np.array(canal)
        canal_modificado = np.clip(canal_array * fator, 0, 255).astype(np.uint8)
        return Image.fromarray(canal_modificado)
    
    # Cria 4 versões diferentes
    
    # 1. Aumenta Ciano
    c_modificado = aumentar_intensidade(c)
    imagem_c = Image.merge('CMYK', (c_modificado, m, y, k))
    
    # 2. Aumenta Magenta
    m_modificado = aumentar_intensidade(m)
    imagem_m = Image.merge('CMYK', (c, m_modificado, y, k))
    
    # 3. Aumenta Amarelo
    y_modificado = aumentar_intensidade(y)
    imagem_y = Image.merge('CMYK', (c, m, y_modificado, k))
    
    # 4. Aumenta Preto
    k_modificado = aumentar_intensidade(k)
    imagem_k = Image.merge('CMYK', (c, m, y, k_modificado))
    
    # Salva as imagens
    # Convertendo para RGB antes de salvar para garantir compatibilidade
    imagem_c.convert('RGB').save('imagem_ciano_pil.jpg', quality=95)
    imagem_m.convert('RGB').save('imagem_magenta_pil.jpg', quality=95)
    imagem_y.convert('RGB').save('imagem_amarelo_pil.jpg', quality=95)
    imagem_k.convert('RGB').save('imagem_preto_pil.jpg', quality=95)
    
    # Opcionalmente, salva também em formato TIFF que suporta CMYK nativo
    imagem_c.save('imagem_ciano_pil.tiff')
    imagem_m.save('imagem_magenta_pil.tiff')
    imagem_y.save('imagem_amarelo_pil.tiff')
    imagem_k.save('imagem_preto_pil.tiff')
    
    return imagem_c, imagem_m, imagem_y, imagem_k

# Exemplo de uso
if __name__ == "__main__":
    try:
        imagens = manipular_canais_cmyk_pil('/Users/danielsantana/Projects/pdi2ime/projects/project1/pverm.jpeg')
        print("Imagens geradas com sucesso!")
    except Exception as e:
        print(f"Erro ao processar imagem: {str(e)}")