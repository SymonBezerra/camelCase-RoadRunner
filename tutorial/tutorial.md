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

Para desenhar um quadrado na tela, vamos utilizar a função ```pygame.draw.rect``` da seguinte forma:

```python
pygame.draw.rect(screen, (255,255,255), (400, 300, 20, 40))
                
pygame.display.flip()
```

Isto é, passamos a função ```draw.rect``` da biblioteca uma superfície onde será desenhado o retângulo, a sua cor em RGB (neste caso, branco), e um objeto do tipo retângulo, que receberá como argumentos uma coordenada X, uma coordenada Y, largura e altura. Ou seja, ao passarmos a tupla ```(400, 300, 20, 40)```, o nosso retângulo será desenhado no ponto (400,300) da nossa tela, e terá um tamanho de 20x40.

Por fim, a função ```flip``` atualizará toda a tela ao final deste ciclo.

O resultado será como na imagem a seguir:

![](/tutorial/imagem_1.png)

## Adicionando a Movimentação

Para adicionarmos a movimentação, vamos retirar as coordenadas (400,300) para duas variáveis, que chamaremos de ```rect_x``` e ```rect_y```:

*Atenção*: é importante que estas variáveis estejam definidas FORA do game loop.

Além disso, vamos realizar mais alguns ```import```'s para recebermos as constantes da biblioteca Pygame equivalentes ao comando das setas do teclado. E vamos incluir isso no game loop, da seguinte maneira:

E adicionaremos mais uma função chamada ```pygame.key.get_pressed()```. Assim, enquanto alguma tecla for pressionada, será realizado um comando. Caso isto fosse feito no loop ```for``` que está fechando o nosso jogo, o nosso retângulo só se movimentaria a cada vez que a tecla fosse pressionada.

Outra coisa que vamos adicionar é um ```pygame.time.Clock```. Este objeto será guardado dentro de uma variável e servirá para definir o *framerate*, isto é, a taxa de quadros do nosso jogo, que também afetará sua velocidade. Logo antes da função ```flip```, chamaremos a função ```clock.tick(30)```, acertando a taxa de quadros no máximo de 30 FPS (frames por segundo).

```python
import pygame
# setas do teclado + tecla pressionada
from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT, KEYDOWN
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()

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

        pygame.draw.rect(screen, (255,255,255), rect=(rect_x, rect_y, 20, 40))

        clock.tick(30)
        pygame.display.flip()
    
    pygame.quit()
```

Agora o nosso "carrinho" consegue se mexer, mas tem um pequeno detalhe... *Agora temos vários dele na nossa tela!*

![](/tutorial/imagem_2.png)

## Corrigindo o bug

Calma, não há o que temer! Isso acontece porque nós simplesmente estamos desenhando outro carrinho na tela, e não fizemos nada com o outro que já estava lá. Notou que há um fundo preto na nossa tela? Então, *esse fundo não é exatamente preto*. Na verdade, ele está vazio, e o computador simplesmente preencheu ele com uma cor padrão para "nada" (neste caso, o preto). 

Uma solução simples para isso é preenchermos a tela com um fundo preto a cada *frame* (lembra do conceito de frame que vimos antes?), assim o carrinho anterior também vai embora junto. E que tal tirarmos as cores e deixarmos guardadas em constantes? Assim, não vamos precisar alterar cada função quando quisermos mudá-las.

Então, vamos definir, fora do ```__main__```, dois valores constantes (em Python, por convenção, constantes têm seu nome escrito em caixa alta):

```python
BG_COLOR = (0, 0, 0) # "BG" = "background", fundo; RGB para preto
FG_COLOR = (255, 255, 255) # FG = "foreground", principal; RGB para branco

# assim, podemos alterar apenas o valor destas constantes e utilizá-las no resto do código!
```

E lá no nosso game loop, vamos adicionar a função ```fill```, que vai preencher a tela inteira, neste caso, com a cor de fundo que nós definimos:

```python
screen.fill(BG_COLOR)

# vamos aproveitar e trocar aquela tupla (255, 255, 255)
# pela nova constante FG_COLOR aqui também!
pygame.draw.rect(screen, FG_COLOR, rect=(rect_x, rect_y, 20, 40))
```

Agora sim: o nosso carrinho pode se mexer sem deixar um rastro branco na tela!

## Introduzindo a classe Sprite

Porém, ainda temos muito o que fazer! Ainda precisamos definir as funções de colisão do nosso carrinho, os obstáculos que caem na tela, criar uma estrada para ele... Vocês ainda estão aí? 

Muita hora nessa calma, porque não vai levar dias para criar este código. E para isso, vamos introduzir uma classe da biblioteca Pygame chamada ```Sprite```. Se você sabe o mínimo de jogos 2D, sabe que as imagens que possuem interação com o jogo são chamadas de *sprites* (se pronuncia /spɹaɪt/). E além disso, vamos utilizar o paradigma de orientação a objetos, que vai nos ajudar muito a organizar isto aqui.

Dentro da biblioteca Pygame, é até possível criar funções de detecção de colisão apenas desenhando retângulos e comparando as suas coordenadas. Porém, vamos acelerar as coisas utilizando os sprites da biblioteca. 

Para isso, vamos começar criando uma classe ```Car```, que terá relação de herança com a classe ```Sprite```, fora do nosso ```__main__```. Vamos aproveitar e também criar uma classe ```Obstacle```, que servirá para os obstáculos da nossa estrada. Mas não vamos nos preocupar com ela por enquanto.

O nosso código ficará assim:

```python
class Car(pygame.sprite.Sprite):
    # no Python, a herança é sinalizada ao colocarmos
    # o nome da superclasse entre parênteses
    pass # nada aqui por enquanto

class Obstacle(pygame.sprite.Sprite):
    pass
```

A primeira coisa que precisamos definir para o nosso carrinho é um retângulo, e suas coordenadas — igual fizemos com o nosso retângulo lá embaixo. 

Depois disso vamos criar duas funções: ```show```, que vai desenhar o nosso carrinho na tela; e ```refresh```, que vai atualizar a posição dele a cada frame.

*Obs.:* no framework Unity, a função "refresh" levaria o nome de ```update```. Porém, no Pygame, já existe uma função "update" utilizada para outra tarefa, então vamos utilizar outro nome para evitar confusões.

O nosso código ficará assim:

```python
class Car(pygame.sprite.Sprite):
    
    # construtor da classe
    def __init__ (self, width, height, color):
                        # largura, altura, cor
        
        # transformando os argumentos em atributos da classe Car
        self.width = width
        self.height = height
        # não vamos fazer o mesmo com color, porque este argumento
        # só será utilizado para construir o retângulo do carrinho

        # coordenadas X e Y iniciais do nosso retângulo
        self.x = 400
        self.y = 300

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        def show (self, surface):
                        # superfície (onde será desenhado o retângulo)
            surface.blit(self.rect, (self.x, self.y))

        def refresh (self, direction):
            if direction == "UP":
                self.y -= 5
            elif direction == "DOWN":
                self.y += 5
            elif direction == "LEFT":
                self.x -= 5
            elif direction == "RIGHT":
                self.x += 5
```