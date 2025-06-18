import pygame

pygame.init()

largura = 720
altura = 1280
tela = pygame.display.set_mode((largura, altura))

branco = (222, 222, 222)    
cinza_claro = (10, 12, 13)

class Caixa:
    def __init__(self, largura=None, altura=None, cor=None, texto=None, x=None, y=None):
        self.largura = largura
        self.altura = altura
        self.cor = cor
        self.texto = texto
        self.x = x
        self.y = y
    
    def desenhar(self, tela):
        # Desenhar o retângulo arredondado
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura), border_radius=10)

        # Renderizar o texto
        fonte = pygame.font.SysFont("Inter", 23)
        texto = fonte.render(self.texto, True, (0, 0, 0))

        # Calcular a posição do texto para centralizá-lo
        texto_x = self.x + (self.largura - texto.get_width()) / 2
        texto_y = self.y + (self.altura - texto.get_height()) / 2

        # Desenhar o texto dentro da caixa
        tela.blit(texto, (texto_x, texto_y))
    
    def clicado(self, x, y):
        return self.x < x < self.x + self.largura and self.y < y < self.y + self.altura

caixa_progressao = Caixa(largura = 1000, cor = (65, 67, 67), x = 0, y = 50, altura = 75)

caixa1 = Caixa(largura=600, cor=(200, 200, 200), texto= "O sistema absorve calor, mas não realiza trabalho", x=50, y=300, altura=100)
caixa2 = Caixa(largura=600, cor=(200, 200, 200), texto="o sistema realiza trabalho, mas não há troca de calor com o ambiente", x=50, y=500, altura=100)
caixa3 = Caixa(largura=600, cor=(200, 200, 200), texto="O sistema realiza calor e trabalho ao mesmo tempo", x=50, y=700, altura=100)
caixa4 = Caixa(largura=600, cor=(200, 200, 200), texto="O sistema mantém a temperatura constante", x=50, y=900, altura=100)

pergunta1 = Caixa(largura=300, cor=(222, 222, 222), texto="O que caracteriza um processo adiabático?", x=210, y=100, altura=100)

resposta_correta = "B"

selecionado = None

caixa_resposta = Caixa(largura=600, cor=(52, 142, 145), texto="O sistema realiza trabalho mas não há troca de calor com o ambiente", x=0, y=0, altura=50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if caixa1.clicado(event.pos[0], event.pos[1]):
                selecionado = "A"
            elif caixa2.clicado(event.pos[0], event.pos[1]):
                selecionado = "B"
            elif caixa3.clicado(event.pos[0], event.pos[1]):
                selecionado = "C"
            elif caixa4.clicado(event.pos[0], event.pos[1]):
                selecionado = "D"

    tela.fill(branco)
    pergunta1.desenhar(tela)
    caixa_progressao.desenhar(tela) 
    caixa1.desenhar(tela)
    caixa2.desenhar(tela)
    caixa3.desenhar(tela)
    caixa4.desenhar(tela)

    if selecionado == resposta_correta:
        caixa_resposta.desenhar(tela)

    pygame.display.flip()