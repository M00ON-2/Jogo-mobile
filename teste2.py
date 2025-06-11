import pygame

pygame.init()

largura = 720
altura = 1280
tela = pygame.display.set_mode((largura, altura))

branco = (255, 0, 0)
cinza_claro = (10, 12, 13)

class Caixa:
    def __init__(self, largura=None, altura=None, cor=None, texto=None, arredondamento, x=None, y=None):
        self.largura = largura
        self.altura = altura
        self.cor = cor
        self.texto = texto
        self.x = x
        self.y = y
        self.arredondamento = {
            "tamanho_borda": 15,
            "shadow_posicao": 5,
            "cor_sombra": (80, 80, 80)
        }

caixa1 = Caixa(largura=680, cor=(0, 255, 0), texto="Caixa 1", x=20, y=100, altura=50,arredondamento)

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    tela.fill(branco)

    # Desenhar o retângulo
    rect = pygame.Rect(caixa1.x, caixa1.y, caixa1.largura, caixa1.altura)
    radius = caixa1.arredondamento["tamanho_borda"]

    pygame.draw.rect(tela, caixa1.cor, rect, bordar=["tamanho_borda"])

    pygame.display.flip()


#    radius = caixa1.arredondamento["tamanho_borda"]
