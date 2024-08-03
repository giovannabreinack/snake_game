import pygame
import random

pygame.init()
pygame.display.set_caption("Snake Game em Python")
largura, altura = 700, 500
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

# Cores RGB dentro do jogo
# Plano de fundo
preto = (0, 0, 0)
# Cor da snake
vermelho = (255, 0, 0)
# Cor do objetivo
azul = (0, 0, 255)
# Cor da pontuação
branco = (255, 255, 255)

# Estruturação da tela
tamanho_quadrado = 30
velocidade_snake = 15
def gerar_objetivo():
    objetivo_x = round(random.randrange(0, largura - tamanho_quadrado) / 30.0) * 30.0
    objetivo_y = round(random.randrange(0, altura - tamanho_quadrado) / 30.0) * 30.0
    return objetivo_x, objetivo_y

def iniciar_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_snake = 1
    pixels = []

    objetivo_x, objetivo_y = gerar_objetivo()


    while not fim_jogo:

      tela.fill(preto)

      for evento in pygame.event.get():
          if evento.type == pygame.QUIT:
              fim_jogo = True


