# "Road Runner" (Oliver Twins) - Tutorial em Pygame 

Neste tutorial, vamos aprender como implementar o jogo "Road Runner", desenvolvido para computadores de 8 bits no ano de 1983, utilizando a biblioteca Pygame. 

Para isso, é necessário fazermos a instalação da biblioteca através do gerenciador de pacotes do Python, o PIP.
Ao começarmos o nosso código, vamos importar a biblioteca Pygame e inicializá-la em nosso programa: 

```python
import pygame

if __name__ == "__main__":
    # aqui definimos a função principal a ser executada
    # pelo interpretador Python
    pygame.init()
```

É importante entendermos que todo jogo eletrônico gera imagens à medida que recebe comandos. Quando assistimos um filme ou programa de TV, damos o play em um programa já pré-definido.

No jogo eletrônico, as imagens serão geradas de maneira diferente, a depender de qual comando foi executado. Por exemplo, ao apertar a seta para a esquerda, o carrinho se move alguns pixels nessa direção. #####

Então, definiremos um ciclo que se repetirá ao longo da execução do nosso jogo (o *"game loop"*), e cada repetição desse ciclo será chamada de *"frame"*. 

## Construindo o Game Loop ##

Para começar, vamos modificar o nosso código para desenhar um quadrado branco na tela. 

```python
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

        pygame.draw.rect(screen, (255,255,255), (400, 300, 20, 40))

        pygame.display.flip()
    
    pygame.quit()
```

Chamaremos a função ```pygame.display.set_mode``` para inicializar a nossa janela, que receberá como argumentos uma lista (valores entre colchetes) com a largura e a altura, respectivamente, da nossa tela. 

A nossa tela será guardada em uma variável, que chamaremos ```screen```, pois ela também será a superfície (```pygame.Surface```) onde desenharemos todos os objetos do nosso jogo.

Para criar o game loop, vamos utilizar uma variável de valor booleano chamada ```running```. Enquanto ```running``` for verdadeira, o game loop será executado. Porém, precisamos também de uma maneira de encerrá-lo, e para tal vamos receber comandos do usuário atráves da seguinte estrutura:

```python
for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```

Neste loop ```for```, o programa irá alterar o valor da nossa variável ```running``` para ```False```, fazendo com que o programa caia na linha de código com a função ```pygame.quit()```, encerrando o programa. Não queremos um jogo que rode para sempre, não é?

*Atenção para esta parte do nosso código*: logo mais, vamos receber a entrada para os comandos que movimentarão o nosso carrinho!

Para desenhar um quadrado na tela, vamos utilizar a função ```pygame.draw.rect``` da seguinte forma:

```python
pygame.draw.rect(screen, (255,255,255), (400, 300, 20, 40))
                
pygame.display.flip()
```

Isto é, passamos a função ```draw.rect``` da biblioteca uma superfície onde será desenhado o retângulo, a sua cor em RGB (neste caso, branco), e um objeto do tipo retângulo, que receberá como argumentos uma coordenada X, uma coordenada Y, largura e altura. Ou seja, ao passarmos a tupla ```(400, 300, 20, 40)```, o nosso retângulo será desenhado no ponto (400,300) da nossa tela, e terá um tamanho de 20x40.

![O resultado será como na imagem a seguir:](/tutorial/imagem_1.png)