    # Este arquivo é utilizado para encontrar as coordenadas para a correção de perpectiva no arquivo view_transformer
    
    # Basta executar o arquivo e a imagem(frame) abrirá para marcação dos pontos, que serão impressos na tela 
    
import cv2

# Carregar o frame do vídeo
img = cv2.imread('view_transformer/frame_video.png')
clone = img.copy()  # Fazer uma cópia da imagem original para resetar

# Variável para armazenar os pontos
ref_point = []

# Função para selecionar pontos manualmente
def select_points(event, x, y, flags, param):
    global ref_point
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(ref_point) < 4:
            ref_point.append((x, y))  # Adicionar o ponto
            print(f"Ponto {len(ref_point)}: {x}, {y}")  # Exibir as coordenadas no console
            cv2.circle(img, (x, y), 5, (0, 255, 0), -1)  # Desenhar um círculo no ponto selecionado
            cv2.imshow("image", img)

        if len(ref_point) == 4:
            print("4 pontos capturados: ", ref_point)

# Inicializar a janela e definir o callback do mouse
cv2.namedWindow("image")
cv2.setMouseCallback("image", select_points)

# Exibir a imagem e esperar a seleção dos pontos
while True:
    cv2.imshow("image", img)
    key = cv2.waitKey(1) & 0xFF

    # Pressione 'r' para resetar a seleção
    if key == ord("r"):
        print("Resetando a seleção...")
        img = clone.copy()  # Restaurar a imagem original
        ref_point = []  # Limpar os pontos selecionados
        cv2.imshow("image", img)

    # Pressione 'q' para sair do loop
    elif key == ord("q"):
        break

# Fechar as janelas ao sair
cv2.destroyAllWindows()
