import pygame
import random
import time

pygame.init()
pygame.display.set_caption('Colisoes')

# Define o tamanho da tela
screen_width, screen_height = 1080, 720
screen = pygame.display.set_mode((screen_width, screen_height))

# Define a cor do fundo
background_color = (255, 255, 255)

class ObjetosVerm:
  
    def __init__(self):
        # Define o tamanho do objeto
        self.width = 15
        self.height = 15
        # Gera uma posição aleatória para o objeto
        self.x = random.uniform(0, screen_width - self.width)
        self.y = random.uniform(0, screen_height - self.height)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        # Define uma cor para o objeto
        self.tipo = random.choice(['vermelho', 'verde', 'azul'])
        if self.tipo == 'vermelho':
            self.color = (255, 0, 0)
        elif self.tipo == 'verde':
            self.color = (0, 255, 0)
        elif self.tipo == 'azul':
            self.color = (0, 0, 255)
        # Define a direção do movimento do objeto
        self.dx = random.uniform(-5, 5)
        self.dy = random.uniform(-5, 5)
  
    def move(self, ObjVerm):
        # Move o objeto
        self.x += self.dx
        self.y += self.dy
        # Inverte a direção do movimento quando o objeto atingir os limites da tela
        if self.x < 0 or self.x > screen_width - self.width:
            self.dx *= -1
        if self.y < 0 or self.y > screen_height - self.height:
            self.dy *= -1
        # Verifica se o objeto está colidindo com outro objeto
        for obj in ObjVerm:
            if obj is not self:
              if self.x < obj.x + obj.width and self.x + self.width > obj.x and self.y < obj.y + obj.height and self.y + self.height > obj.y:
                  self.dx *= -1
                  self.dy *= -1
                  # Troca o tipo do objeto de acordo com o tipo do objeto com o qual ele está colidindo
                  if self.tipo == 'vermelho' and obj.tipo == 'azul':
                      obj.tipo = 'vermelho'
                      obj.color = (255, 0, 0)
                  elif self.tipo == 'verde' and obj.tipo == 'vermelho':
                      obj.tipo = 'verde'
                      obj.color = (0, 255, 0)
                  elif self.tipo == 'azul' and obj.tipo == 'verde':
                      obj.tipo = 'azul'
                      obj.color = (0, 0, 255)
                  break

    def draw(self, screen):
        # Desenha o objeto na tela
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

# Cria uma lista de objetos
objetos_verm = [ObjetosVerm() for _ in range(100)]

# Define o FPS do jogo
fps = 60

# Roda o loop principal do jogo
running = True
while running:
    # Preenche a tela com a cor de fundo
    screen.fill(background_color)

    # Move e desenha os objetos
    for obj in objetos_verm:
        obj.move(objetos_verm)
        obj.draw(screen)

    # Atualiza a tela
    pygame.display.flip()

    # Faz uma pausa para o próximo quadro
    time.sleep(1 / fps)
