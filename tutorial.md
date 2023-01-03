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