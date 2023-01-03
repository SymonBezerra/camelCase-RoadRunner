import pygame
# setas do teclado + tecla pressionada
from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT, KEYDOWN
# inicializando a tela do nosso jogo
screen = pygame.display.set_mode([800,600])

if __name__ == "__main__":
    
    pygame.init()

    # criando a variável que gerenciará o nosso game loop
    running = True

    while running:
        # recebendo a entrada de comandos
        rect_x = 400
        rect_y = 300

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    rect_y -= 5 
                elif event.key == K_DOWN:
                    rect_y += 5
                elif event.key == K_LEFT:
                    rect_x -= 5
                elif event.key == K_RIGHT:
                    rect_x += 5


        pygame.draw.rect(screen, (255,255,255), rect=(rect_x, rect_y, 20, 40))

        pygame.display.flip()
    
    pygame.quit()