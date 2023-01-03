import pygame
# inicializando a tela do nosso jogo
screen = pygame.display.set_mode([800,600])

if __name__ == "__main__":
    
    pygame.init()

    # criando a variável que gerenciará o nosso game loop
    running = True

    while running:
        # recebendo a entrada de comandos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.draw.rect(screen, (255,255,255), rect=(400, 300, 20, 40))

        pygame.display.flip()
    
    pygame.quit()