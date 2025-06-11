import pygame

pygame.init()

largura = 720
altura = 1280
tela = pygame.display.set_mode((largura, altura))

branco = (255, 0, 0)
cinza_claro = (10, 12, 13)

#Defini os atributos de uma caixa (todos eles não tem valor, tem que se atribuir dps)
class Caixa:
    def __init__(self, largura= None, altura= None, cor= None, texto= None, arredondamento = None, x= None, y= None):
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


caixa1 = Caixa(largura = 300, cor= (0, 255, 0), texto = "Caixa 1", x = 100, y = 100, altura = 200)
caixa1.arredondamento

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    tela.fill(branco)
     
    pygame.draw.rect(caixa1,tela,)
    
    pygame.display.flip()
    
# if caixa1 = perguntacorreta:
#     print("correta")
# else:
#     print("incorreta")
# (adicionar alguma coisa aqui)