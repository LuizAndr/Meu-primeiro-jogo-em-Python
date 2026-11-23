import turtle
import time
import math
import random

# Configurações de tela
tela = turtle.Screen()
tela.title("Dragon Ball 2D")
tela.setup(width=800, height=600)
tela.tracer(0)
tela.bgpic('mapa.gif')
clique = True

# Variáveis e configurações do mapa
obstaculos = []
mapa1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1 ,1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1 ,1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1 ,1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1 ,1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
mapa2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

mapa_atual = mapa1
celula_largura = 60
celula_altura = 60
x_inicial = -455
y_inicial = 360

# Configuração inicial do Turtle
turtle.up()
turtle.hideturtle()

#função que desenha o mapa
def desenhar_mapa():
    tela.bgpic("mapa.gif")
    global obstaculos
    turtle.clear()
    obstaculos.clear()
    for linha, linha_valores in enumerate(mapa_atual):
        for coluna, valor in enumerate(linha_valores):
            x = x_inicial + coluna * celula_largura
            y = y_inicial - linha * celula_altura
            if valor == 1:
                turtle.goto(x, y)
                turtle.color("white", "white")
                turtle.down()
                turtle.begin_fill()
                for _ in range(2):
                    turtle.forward(celula_largura)
                    turtle.right(90)
                    turtle.forward(celula_altura)
                    turtle.right(90)
                turtle.end_fill()
                turtle.up()
                obstaculos.append((x, y - celula_altura))
    turtle.update()

# Funções de inicialização do jogo
def iniciar_jogo(x, y):
    global clique
    clique = False
    tela.onclick(None)  # Desativa o clique para evitar múltiplos inícios
    desenhar_mapa() 

def mostrar_intro():
    frames = ["frame1.gif", "frame2.gif", "frame3.gif", "frame4.gif", "frame5.gif"]
    while clique:
        for frame in frames:
            tela.bgpic(frame)
            tela.update()
            time.sleep(0.3)
            tela.bgpic("frame1.gif")  # Reseta para o primeiro frame

tela.onclick(iniciar_jogo)
mostrar_intro()

# Personagem principal
tela.addshape('jogador_direita.gif')
tela.addshape('jogador_esquerda.gif')
jogador = turtle.Turtle()
jogador.shape('jogador_direita.gif')
jogador.penup()
jogador.goto(-350, -190)
altura_jogador = 80 
jogador.direcao = "right"
jogador.dy = 20  # Velocidade vertical do pulo
esta_pulando = False

# Criação dos inimigos
tela.addshape('picollo_esquerda.gif')
tela.addshape('picollo_direita.gif')

inimigo1 = turtle.Turtle()
inimigo1.shape("picollo_esquerda.gif")
inimigo1.penup()
inimigo1.goto(350, -100)
inimigo1_direcao = "right"

inimigo2 = turtle.Turtle()
inimigo2.shape("picollo_direita.gif")
inimigo2.penup()
inimigo2.goto(-350, 22)
inimigo2_direcao = "right"

inimigo3 = turtle.Turtle()
inimigo3.shape("picollo_esquerda.gif")
inimigo3.color("red")
inimigo3.penup()
inimigo3.goto(350, 140)
inimigo3_direcao = "right"

inimigos = [inimigo1, inimigo2, inimigo3]

# Limites de movimento dos inimigos
inimigo1_limite_esquerdo = -100
inimigo1_limite_direito = 300
velocidade_inimigo1 = 5

inimigo2_limite_esquerdo = -350
inimigo2_limite_direito = 60
velocidade_inimigo2 = 5

inimigo3_limite_esquerdo = -100
inimigo3_limite_direito = 300
velocidade_inimigo3 = 5

# Configurações do chefe
velocidade_boss = 3
velocidade_boss_vertical = 2 
probabilidade_disparo = 0.04  # 4% de chance de disparar a cada frame
projeteis_boss = []  # Lista para armazenar os projéteis do boss

#função que cria o inimigo final
def criar_boss():
    global boss
    tela.addshape('frieza.gif')
    boss = turtle.Turtle()
    boss.shape('frieza.gif')
    boss.penup()
    boss.goto(350, 200)
    boss.direcao_horizontal = "esquerda"
    boss.direcao_vertical = "baixo"

def mover_boss():
    global boss
    if not boss:
        return
    x = boss.xcor()
    y = boss.ycor()
    # Movimento Horizontal
    if boss.direcao_horizontal == "esquerda":
        boss.setx(x - velocidade_boss)
        if boss.xcor() < -350:
            boss.direcao_horizontal = "direita"
    elif boss.direcao_horizontal == "direita":
        boss.setx(x + velocidade_boss)
        if boss.xcor() > 350:
            boss.direcao_horizontal = "esquerda"
    # Movimento Vertical (NOVO)
    if boss.direcao_vertical == "baixo":
        boss.sety(y - velocidade_boss_vertical)
        if boss.ycor() < 100:  # Limite inferior
            boss.direcao_vertical = "cima"
    elif boss.direcao_vertical == "cima":
        boss.sety(y + velocidade_boss_vertical)
        if boss.ycor() > 200: # Limite superior
            boss.direcao_vertical = "baixo"

def disparar_projetil_boss():
    global boss, projeteis_boss
    if not boss: #verifica se o boss existe
        return
    if random.random() < probabilidade_disparo:
        projetil = turtle.Turtle()
        projetil.shape("circle")  # Você pode usar outra forma
        projetil.color("purple")  # Cor do projétil
        projetil.penup()
        projetil.hideturtle()
        projetil.goto(boss.xcor(), boss.ycor() - 20) #posiciona o projetil saindo de baixo do boss
        projetil.showturtle()
        projetil.dy = -5  # Velocidade vertical do projétil (para baixo)
        projeteis_boss.append(projetil)


def mover_projeteis_boss():
    global projeteis_boss
    for projetil in projeteis_boss:
        projetil.sety(projetil.ycor() + projetil.dy)
        if projetil.ycor() < -300:
            projetil.hideturtle()
            projeteis_boss.remove(projetil)
            del projetil #limpa o projetil da memoria

def verificar_colisao_projetil_jogador():
    global projeteis_boss
    for projetil in projeteis_boss:
        distancia = math.sqrt((jogador.xcor() - projetil.xcor())**2 + (jogador.ycor() - projetil.ycor())**2)
        if distancia <= raio_colisao:
            texto.write("GAME OVER!", font=("Arial", 80, "bold"), align="center")
            jogador.hideturtle()
            kamehameha.hideturtle()
            tela.done()

acertos = []
#verifica se o boss foi atingido
def verificar_acerto():
    global acertos
    for acerto in acertos:
        distancia = math.sqrt((acerto.xcor() - boss.xcor())**2 + (acerto.ycor() - boss.ycor())**2)
        if distancia < raio_colisao: 
            texto.clear()
            texto.write("Você venceu!", font=("Arial", 80, "bold"), align="center")
            tela.done()
            acerto.hideturtle() 
            boss.hideturtle() # Esconde o kamehameha que acertou
            acertos.remove(acerto)  # Remove o kamehameha da lista para evitar reprocessamento
            tela.update()  # Atualiza a tela para refletir as mudanças
            return True
    return False
            
# Kamehameha
kamehameha = turtle.Turtle()
kamehameha.shape("circle")
kamehameha.color("cyan")
kamehameha.penup()
kamehameha.hideturtle()
kamehameha_state = "ready"
kamehameha_direction = "right"

#verifica se o jogador mudou de mapa e retira os inimigos anteriores e cria o novo
def verifica_mudanca_mapa():
    global mapa_atual
    if mapa_atual == mapa1 and jogador.xcor() == -390 and jogador.ycor() >= 270:
        mapa_atual = mapa2
        desenhar_mapa()
        criar_boss()
        loop_boss()
        jogador.goto(-350, -190)
        inimigo1.goto(500,500)
        inimigo2.goto(500,500)
        inimigo3.goto(500,500)
        turtle.goto(-350,-190)
        turtle.color("white", "white")
        turtle.down()
        turtle.begin_fill()
        tela.bgpic('mapa2.gif')
        

def verifica_chão(x, y):
    for ox, oy in obstaculos:
        # Verifica colisão considerando a base do jogador
        if ox <= x < ox + celula_largura and oy <= y - altura_jogador / 2 < oy + celula_altura:
            return True
    return False

#criando ponto central para exibição de textos
texto = turtle.Turtle()
texto.hideturtle()
texto.goto(0,0)

raio_colisao = 29

def verificar_colisao():
    for inimigo in inimigos:
    # Calcula a distância entre o jogador e o inimigo
        distancia = math.sqrt((jogador.xcor() - inimigo.xcor())**2 + (jogador.ycor() - inimigo.ycor())**2)
    # Verifica se a distância é menor ou igual ao raio de colisão
        if distancia <= raio_colisao:
            texto.write("GAME OVER!", font=("Arial", 80, "bold"), align="center")
            tela.done()

# Função para verificar se há obstáculo abaixo do jogador
def verifica_obstaculo_abaixo():
    x = jogador.xcor()
    y = jogador.ycor()
    novo_y = y - 5
    if not verifica_chão(x, novo_y):
        jogador.sety(jogador.ycor() - 5)  # Faz o jogador "cair"

jogador_velocidade = 20

# Movimentos do jogador
def esquerda():
    verificar_colisao()
    jogador.shape('jogador_esquerda.gif')
    jogador.direcao = "left"
    x, y = jogador.xcor(), jogador.ycor()
    if not verifica_chão(x - 20, y):
        jogador.setx(x - 20)
    verifica_mudanca_mapa()

def direita():
    verificar_colisao()
    jogador.shape('jogador_direita.gif')
    jogador.direcao = "right"
    x, y = jogador.xcor(), jogador.ycor()
    if not verifica_chão(x + 20, y):
        jogador.setx(x + 20)
    verifica_mudanca_mapa()

def pulo():
    verificar_colisao()
    global esta_pulando
    if not esta_pulando:
        esta_pulando = True
        jogador.dy = 32  # Velocidade inicial do pulo


# Atualiza o pulo
def update_pulo():
    global esta_pulando  
    if esta_pulando:
        y = jogador.ycor()
        novo_y = y + jogador.dy
        jogador.dy -= 1  # Gravidade
        # Verifica colisão com a base do jogador
        if not verifica_chão(jogador.xcor(), novo_y):
            jogador.sety(novo_y)
        else:
            jogador.dy = 0
            esta_pulando = False
        # Verifica se o jogador voltou ao chão (posição mínima)
        if jogador.ycor() <= -250:
            jogador.sety(-250)
            esta_pulando = False
            jogador.dy = 0

def move_inimigo1():
    global inimigo1_direcao
    x = inimigo1.xcor()

    # Movimenta para a direita ou esquerda
    if inimigo1_direcao == "right":
        verificar_colisao()
        inimigo1.setx(x + velocidade_inimigo1)
        if inimigo1.xcor() >= inimigo1_limite_direito:
            inimigo1_direcao = "left"
    elif inimigo1_direcao == "left":
        verificar_colisao()
        inimigo1.setx(x - velocidade_inimigo2)
        if inimigo1.xcor() <= inimigo1_limite_esquerdo:
            inimigo1_direcao = "right"

def move_inimigo2():
    global inimigo2_direcao
    x = inimigo2.xcor()
    # Movimenta para a direita ou esquerda
    if inimigo2_direcao == "right":
        verificar_colisao()
        inimigo2.setx(x + velocidade_inimigo2)
        if inimigo2.xcor() >= inimigo2_limite_direito:
            inimigo2_direcao = "left"
    elif inimigo2_direcao == "left":
        verificar_colisao()
        inimigo2.setx(x - velocidade_inimigo2)
        if inimigo2.xcor() <= inimigo2_limite_esquerdo:
            inimigo2_direcao = "right"

def move_inimigo3():
    global inimigo3_direcao
    x = inimigo3.xcor()
    # Movimenta para a direita ou esquerda
    if inimigo3_direcao == "right":
        verificar_colisao()
        inimigo3.setx(x + velocidade_inimigo3)
        if inimigo3.xcor() >= inimigo3_limite_direito:
            inimigo3_direcao = "left"
    elif inimigo3_direcao == "left":
        verificar_colisao()
        inimigo3.setx(x - velocidade_inimigo3)
        if inimigo3.xcor() <= inimigo3_limite_esquerdo:
            inimigo3_direcao = "right"

def lanca_kamehameha():
    global kamehameha_state, kamehameha_direction
    acertos.append(kamehameha)
    if kamehameha_state == "ready":
        kamehameha_state = "fire"
        kamehameha_direction = jogador.direcao
        kamehameha.goto(jogador.xcor(), jogador.ycor())
        kamehameha.showturtle()

# Atualiza o projétil
def update_kamehameha():
    global kamehameha_state
    if kamehameha_state == "fire":
        if kamehameha_direction == "right":
            kamehameha.setx(kamehameha.xcor() + 20)
        else:
            kamehameha.setx(kamehameha.xcor() - 20)
            tela.update()
        if kamehameha.xcor() > 400 or kamehameha.xcor() < -400:
            kamehameha.hideturtle()
            kamehameha_state = "ready"

# Função para fechar o jogo
def fechar_jogo():
    tela.bye()

#loop que inicia apenas na segunda fase
def loop_boss():
    mover_boss() 
    disparar_projetil_boss()
    mover_projeteis_boss()
    verificar_colisao_projetil_jogador()
    verificar_acerto() 
    tela.update()
    tela.ontimer(loop_boss, 50)
    tela.onkeypress(lanca_kamehameha, "y")

#loop do jogo
def game_loop():
    update_kamehameha()
    update_pulo()
    verifica_obstaculo_abaixo()
    move_inimigo1()
    move_inimigo2()
    move_inimigo3()
    tela.update()
    tela.ontimer(game_loop, 50)

# Controles
tela.listen()
tela.onkeypress(esquerda, "a")
tela.onkeypress(direita, "d")
tela.onkeypress(pulo, "space")
tela.onkeypress(fechar_jogo,"q")

game_loop()
desenhar_mapa()
tela.mainloop()