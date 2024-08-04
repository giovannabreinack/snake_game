import pygame
import random

pygame.init()
pygame.display.set_caption("Snake Game em Python")
largura, altura = 700, 500
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

# Cores RGB dentro do jogo: plano de fundo
preto = (0, 0, 0)
# Cor da snake
vermelho = (255, 0, 0)
# Cor do objetivo
azul = (0, 0, 255)
# Cor da pontuação
branco = (255, 255, 255)

# Estruturação da tela
tamanho_quadrado = 20
velocidade_snake = 15
def gerar_objetivo():
    objetivo_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0
    objetivo_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0) * 20.0
    return objetivo_x, objetivo_y

def visual_objetivo(tamanho, objetivo_x, objetivo_y):
    pygame.draw.rect(tela, azul, [objetivo_x, objetivo_y, tamanho, tamanho])

def visual_snake(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, vermelho, [pixel[0], pixel[1], tamanho, tamanho])

def visual_pontos(pontos):
    fonte = pygame.font.SysFont("Arial", 30)
    texto = fonte.render(f"Pontos: {pontos}", True, branco)
    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla):

        if tecla == pygame.K_DOWN:
            velocidade_x = 0
            velocidade_y = tamanho_quadrado

        elif tecla == pygame.K_UP:
                velocidade_x = 0
                velocidade_y = -tamanho_quadrado

        elif tecla == pygame.K_RIGHT:
            velocidade_x = tamanho_quadrado
            velocidade_y = 0

        elif tecla == pygame.K_LEFT:
            velocidade_x = -tamanho_quadrado
            velocidade_y = 0

        return velocidade_x, velocidade_y

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
          elif evento.type == pygame.KEYDOWN:
              velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

      visual_objetivo(tamanho_quadrado, objetivo_x, objetivo_y)

      if x < 0 or x >= largura or y < 0 or y >= altura:
          fim_jogo = True

      x+= velocidade_x
      y+= velocidade_y

      pixels.append([x, y])

      if len(pixels) > tamanho_snake:
          del pixels[0]

      for pixel in pixels[:-1]:
        if pixel == [x, y]:
             fim_jogo = True


      visual_snake(tamanho_quadrado, pixels)
      visual_pontos(tamanho_snake - 1)

      pygame.display.update()

      if x == objetivo_x and y == objetivo_y:
          tamanho_snake += 1
          objetivo_x, objetivo_y = gerar_objetivo()

      relogio.tick(velocidade_snake)

iniciar_jogo()



