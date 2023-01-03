import pygame
# setas do teclado + tecla pressionada
from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT, KEYDOWN
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()

BG_COLOR = (0,0,0)
FG_COLOR = (255,255,255)

class Car(pygame.sprite.Sprite):
    
    # construtor da classe
    def __init__ (self, width, height, color):
                        # largura, altura, cor
        
        # transformando os argumentos em atributos da classe Car
        self.width = width
        self.height = height
        self.color = color

        # coordenadas X e Y iniciais do nosso retângulo
        self.x = 400
        self.y = 300

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def show (self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def refresh (self, direction):
        if direction == "UP":
            self.y -= 5
        elif direction == "DOWN":
            self.y += 5
        elif direction == "LEFT":
            self.x -= 5
        elif direction == "RIGHT":
            self.x += 5
        
        # assim, vamos atualizar a posição do nosso retângulo
        self.rect.left = self.x
        self.rect.top = self.y
        
            

class Obstacle(pygame.sprite.Sprite):
    pass

if __name__ == "__main__":
    
    pygame.init()

    running = True

    car = Car(20, 50, FG_COLOR)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # função para executar comandos
        # enquanto alguma tecla estiver pressionada

        screen.fill(BG_COLOR)

        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            car.refresh("UP")
        elif keys[K_DOWN]:
            car.refresh("DOWN")
        elif keys[K_LEFT]:
            car.refresh("LEFT")
        elif keys[K_RIGHT]:
            car.refresh("RIGHT")

        car.show(screen)

        clock.tick(30)
        pygame.display.flip()
    
    pygame.quit()