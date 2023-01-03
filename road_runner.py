import pygame
# setas do teclado + tecla pressionada
from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT, KEYDOWN
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()

BG_COLOR = (0,0,0)
FG_COLOR = (255,255,255)

class Car(pygame.sprite.Sprite):
    # no Python, a herança é sinalizada ao colocarmos
    # o nome da superclasse entre parênteses
    pass # nada aqui por enquanto

class Obstacle(pygame.sprite.Sprite):
    pass

if __name__ == "__main__":
    
    pygame.init()

    running = True

    rect_x = 400
    rect_y = 300

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # função para executar comandos
        # enquanto alguma tecla estiver pressionada
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            rect_y -= 5
        elif keys[K_DOWN]:
            rect_y += 5
        elif keys[K_LEFT]:
            rect_x -= 5
        elif keys[K_RIGHT]:
            rect_x += 5

        screen.fill(BG_COLOR)

        pygame.draw.rect(screen, FG_COLOR, rect=(rect_x, rect_y, 20, 40))

        clock.tick(30)
        pygame.display.flip()
    
    pygame.quit()