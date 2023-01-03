# "Road Runner" (Oliver Twins) - Tutorial em Pygame 

Neste tutorial, vamos aprender como implementar o jogo "Road Runner", desenvolvido para computadores de 8 bits no ano de 1983, utilizando a biblioteca Pygame. 

O jogo foi desenvolvido pelos gêmeos Andrew e Philip Oliver, para um computador doméstico de 8 bits chamado *Dragon 32*, quando eles ainda eram adolescentes. O jogo consiste em um carrinho que percorre uma estrada e desvia de obstáculos gerados aleatoriamente. O código original foi publicado em uma revista inglesa chamada *Computer & Video Games*, e pode ser conferido [neste arquivo do GitHub](https://github.com/arhneu/road-runner/blob/master/road-runner.bas).

O jogo original foi desenvolvido em uma linguagem de programação muito popular nos computadores dos anos 80 chamada *BASIC*, que era bem simples e versátil como Python, porém não muito poderosa, principalmente devido às limitações do hardware da época. Mesmo assim, muitas pessoas — e até crianças — conseguiam fazer coisas incríveis com a linguagem. Entre essas coisas, jogos eletrônicos, alguns até bem incríveis!  

![Imagem do jogo original](/tutorial/print_road_runner.png)

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

No jogo eletrônico, as imagens serão geradas de maneira diferente, a depender de qual comando foi executado. Por exemplo, ao apertar a seta para a esquerda, o carrinho se move alguns pixels nessa direção.

Então, definiremos um ciclo que se repetirá ao longo da execução do nosso jogo (o *"game loop"*), e cada repetição desse ciclo será chamada de *"frame"*. 

## Construindo o Game Loop ##

Para começar, vamos modificar o nosso código para desenhar um quadrado branco na tela. 

```python
import pygame
# inicializando a tela do nosso jogo
screen = pygame.display.set_mode([800, 600])

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
screen = pygame.display.set_mode([800, 600])
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
            rect_y -= 10 # velocidade de 10 px\frame
        elif keys[K_DOWN]:
            rect_y += 10 
        elif keys[K_LEFT]:
            rect_x -= 10 
        elif keys[K_RIGHT]:
            rect_x += 10 

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

Depois disso vamos criar duas funções: ```show```, que vai desenhar o nosso carrinho na tela; e ```refresh```, que será executada a cada frame para atualizar a sua posição.

*Obs.:* no framework Unity, por exemplo, a função "refresh" levaria o nome de ```update```. Porém, no Pygame, já existe uma função "update" utilizada para outra tarefa, então vamos utilizar outro nome para evitar confusões.

O nosso código ficará assim:

```python
class Car(pygame.sprite.Sprite):
    
    # construtor da classe
    def __init__ (self, width, height, color):
                        # largura, altura, cor
        
        # inicializando a superclasse
        super(Car, self).__init__()
        
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
        # blit: desenha uma imagem sobre outra
        surface.blit(surface, self.rect)
                    # desenhar sobre ela mesma o retângulo

    def refresh (self, direction):
        if direction == "UP":
            self.y -= 10
        elif direction == "DOWN":
            self.y += 10
        elif direction == "LEFT":
            self.x -= 10
        elif direction == "RIGHT":
            self.x += 10
        
        # assim, vamos atualizar a posição do nosso retângulo
        self.rect.left = self.x
        self.rect.top = self.y
```

Percebeu que o funcionamento dessas funções é bem parecido com o código que escrevemos anteriormente? 

Para isso, vamos definir uma instância da classe ```Car``` dentro do ```__main```, e substituir o código que fizemos antes pelas novas funções ```show``` e ```refresh```.

O código dentro do ```__main__``` ficará da seguinte maneira:

```python
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
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            car.refresh("UP")
        elif keys[K_DOWN]:
            car.refresh("DOWN")
        elif keys[K_LEFT]:
            car.refresh("LEFT")
        elif keys[K_RIGHT]:
            car.refresh("RIGHT")

        screen.fill(BG_COLOR)

        car.show(screen)

        clock.tick(30)
        pygame.display.flip()
    
    pygame.quit()
```

## Criando a Estrada

Agora, vamos resolver mais um problema do nosso jogo: ele se chamada *Road Runner* (corredor de estradas), mas não tem... *UMA ESTRADA*! Não queremos que o nosso carrinho se mexa para tudo quanto é lado livremente, ele precisa andar dentro de uma estrada.

Então, vamos definir uma barreira que o nosso carrinho não possa atravessar. Ele pode ir para frente e para trás o quanto quiser, mas não poderá ultrapassar os pixels 200 e 600 no eixo horizontal. Além disso, não podemos deixar que o nosso carrinho saia da tela! Então precisamos limitar a posição dele entre os pixels 0 e 600 no eixo horizontal (caso contrário, ele continuará a se movimentar, porém fora da tela).

Para isso, precisamos fazer uma pequena alteração no método ```refresh``` da classe ```Car```.

Vamos definir isso fora do ```__main__`` como valores constantes:

```python
# vamos aproveitar e colocar o tamanho da janela
# em uma constante também!
WINDOW_SIZE = [800, 600]
screen = pygame.display.set_mode(WINDOW_SIZE)

...
# barreiras laterais
LEFT_BARRIER = 200
RIGHT_BARRIER = 600
```

Depois, vamos alterar o método ```refresh```:

```python
def refresh (self, direction):
    if direction == "UP" and self.y > 0:
                self.y -= 10
    elif direction == "DOWN" and self.y < WINDOW_SIZE[1]:
                                # altura da janela
        self.y += 10
    elif direction == "LEFT" and self.x > LEFT_BARRIER:
                            # se a posição X for maior
                            # que a barreira dos 200px
        self.x -= 10
    elif direction == "RIGHT" and self.x < RIGHT_BARRIER:
                                # se a posição X for menor
                                # que a barreira dos 400px
        self.x += 10
```

Se executarmos o código, perceberemos que, de fato, o carro não anda, mas não há nenhuma forma de visualizarmos isso. Que tal adicionarmos duas linhas para demarcar a estrada? Vamos definir uma nova constante para a cor da estrada chamada ```ROAD_COLOR```, com os valores RGB(0, 0, 255), fora do ```__main__```.

E antes da função ```show``` do nosso carrinho, dentro do game loop, vamos adicionar mais dois retângulos usando a função ```pygame.draw.rect```:

```python
pygame.draw.rect(screen, ROAD_COLOR, (LEFT_BARRIER - 20, 0, 20, 600))
pygame.draw.rect(screen, ROAD_COLOR, (RIGHT_BARRIER + 20, 0, 20, 600))
```

## Adicionando os obstáculos

Para finalizarmos, precisamos adicionar a classe para os nossos obstáculos. Bom, ela é idêntica ao nosso carro, porém com uma diferença: ao invés de se movimentar para as quatro direções, ela apenas se movimenta para cima, já que a nossa estrada vai aparecendo em um esquema de rolagem. 

Vamos chamar essa função também de ```refresh``` para a classe ```Obstacle```. No restante, ela será idêntica à classe ```Car```.

```python
class Obstacle(pygame.sprite.Sprite):
    
    def __init__ (self, width, height, color):
        super(Obstacle, self).__init__()

        self.width = width
        self.height = height
        self.color = color

        self.x = 200 + (randint(0,20) * 20)
        self.y = 600

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def show (self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
    
    def refresh (self):
        self.y -= 20 # velocidade de 20px\frame
        self.rect.top = self.y
```

A única coisa que não utilizamos aqui antes foi a função ```randint```, da biblioteca ```random```. Para importá-la, coloque o código ```from random import randint``` junto aos imports que fizemos antes. Assim, a coordenada inicial X será um múltiplo de 20 entre 200 e 600, fazendo com que os obstáculos estejam em uma espécie de "grid", facilitando o desafio.

Vamos adicionar também uma constante ```OBSTACLE_COLOR```, de valor RGB(255, 255, 0). Assim, todos os obstáculos terão a cor amarela, diferenciando-se dos demais elementos.

### CRIAR GRUPO DE SPRITES PARA OBSTÁCULOS ### 