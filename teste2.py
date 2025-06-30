import pygame

pygame.init()

largura = 720
altura = 1280
tela = pygame.display.set_mode((largura, altura))

branco = (222, 222, 222)    
cinza_claro = (10, 12, 13)
vermelho = (255, 0, 0)
verde = (52, 142, 145)
cinza = (200, 200, 200)

fonte = pygame.font.SysFont("Inter", 23)

class Caixa:
    def __init__(self, largura=None, altura=None, cor=None, texto=None, x=None, y=None):
        self.largura = largura
        self.altura = altura
        self.cor = cor
        self.texto = texto
        self.x = x
        self.y = y
    
    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura), border_radius=10)
        texto = fonte.render(self.texto, True, (0, 0, 0))
        texto_x = self.x + (self.largura - texto.get_width()) / 2
        texto_y = self.y + (self.altura - texto.get_height()) / 2
        tela.blit(texto, (texto_x, texto_y))
    
    def clicado(self, x, y):
        return self.x < x < self.x + self.largura and self.y < y < self.y + self.altura

# Lista de perguntas com alternativas e resposta correta
perguntas = [
    {
        "texto": "O que caracteriza um processo adiabático?",
        "alternativas": [
            "O sistema absorve calor, mas não realiza trabalho",
            "O sistema realiza trabalho, mas não há troca de calor com o ambiente",
            "O sistema realiza calor e trabalho ao mesmo tempo",
            "O sistema mantém a temperatura constante"
        ],
        "resposta_correta": 1  # índice da resposta correta
    },
    {
        "texto": "Qual é a capital do Brasil?",
        "alternativas": [
            "Rio de Janeiro",
            "Brasília",
            "São Paulo",
            "Salvador"
        ],
        "resposta_correta": 1
    }
]

# Estado atual do quiz
indice_pergunta = 0
selecionado = None

def desenhar_pergunta(pergunta, selecionado):
    pergunta_caixa = Caixa(largura=600, cor=branco, texto=pergunta["texto"], x=60, y=100, altura=80)
    pergunta_caixa.desenhar(tela)

    caixas = []
    for i, texto in enumerate(pergunta["alternativas"]):
        cor = cinza

        if selecionado is not None:
            if i == pergunta["resposta_correta"]:
                cor = verde
            elif i == selecionado:
                cor = vermelho

        caixa = Caixa(largura=600, cor=cor, texto=texto, x=50, y=250 + i * 120, altura=100)
        caixa.desenhar(tela)
        caixas.append(caixa)

    return caixas

# Loop principal
running = True
while running:
    tela.fill(branco)
    pergunta_atual = perguntas[indice_pergunta]

    caixas_opcoes = desenhar_pergunta(pergunta_atual, selecionado)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and selecionado is None:
            for i, caixa in enumerate(caixas_opcoes):
                if caixa.clicado(*event.pos):
                    selecionado = i

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and selecionado is not None:
                indice_pergunta += 1
                if indice_pergunta >= len(perguntas):
                    running = False  # ou mostrar "fim do quiz"
                else:
                    selecionado = None

    pygame.display.flip()

pygame.quit()
