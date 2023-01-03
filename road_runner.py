import pygame
# setas do teclado + tecla pressionada
from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT
WINDOW_SIZE = [800, 600]
            # largura x altura
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

BG_COLOR = (0,0,0)
FG_COLOR = (255,255,255)
ROAD_COLOR = (0, 0, 255)
OBSTACLE_COLOR = (255, 255, 0)

# barreiras laterais
LEFT_BARRIER = 200
RIGHT_BARRIER = 600

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
        self.y = 20

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def show (self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def refresh (self, direction):
        if direction == "UP" and self.y > 0:
            self.y -= 5
        elif direction == "DOWN" and self.y < WINDOW_SIZE[1]:
                                    # altura da janela
            self.y += 5
        elif direction == "LEFT" and self.x > LEFT_BARRIER:
                                # se a posição X for maior
                                # que a barreira dos 200px
            self.x -= 5
        elif direction == "RIGHT" and self.x < RIGHT_BARRIER:
                                    # se a posição X for menor
                                    # que a barreira dos 400px
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

        pygame.draw.rect(screen, ROAD_COLOR, (LEFT_BARRIER - 20, 0, 20, 600))
        pygame.draw.rect(screen, ROAD_COLOR, (RIGHT_BARRIER + 20, 0, 20, 600))

        car.show(screen)

        clock.tick(30)
        pygame.display.flip()
    
    pygame.quit()