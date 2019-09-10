import sys, pygame
import myfuns as mf
import random as r

#Importante: Se esta utilizando la libreria pygame para el desarrollo del juego...
#Inicializacion correspondiente a Pygame
pygame.init()
size = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Juego BALL')
run=True
#################
wallzomb = pygame.image.load('Imagenes/fondo.jpg') #Crear fondo del nivel (lectura de imagen)
wallzomb = pygame.transform.scale(wallzomb, (800, 600))

mainf = pygame.image.load('Imagenes/main.jpg') #Fondo para la pantallar de inicio
mainf = pygame.transform.scale(mainf, (800, 600))

goverf = pygame.image.load('Imagenes/gover.jpg') #Fondo para la pantalla de Game Over
goverf = pygame.transform.scale(goverf, (800, 600))

pausaf = pygame.image.load('Imagenes/pausa.jpg') #Fondo para la pantalla de Pausa
pausaf = pygame.transform.scale(pausaf, (800, 600))

zombi = pygame.image.load('Imagenes/zombie.png') #Sprite del zombie
zombi = pygame.transform.scale(zombi, (50, 50))

zatak = pygame.image.load('Imagenes/zatack.png') #Sprite del zombie atacando
zatak = pygame.transform.scale(zatak, (50, 50))

player = pygame.image.load('Imagenes/spider.png') #Sprite del jugador
player = pygame.transform.scale(player, (50, 50))

fball = pygame.image.load('Imagenes/fireball.png') #Sprite de la bola de fuego
fball = pygame.transform.scale(fball, (50, 50))

bplay = pygame.image.load('Imagenes/play.png') #Sprite de el boton para jugar/reanudar
bplay = pygame.transform.scale(bplay, (100, 100))

brelo = pygame.image.load('Imagenes/replay.png') #Sprite del boton para jugar denuevo
brelo = pygame.transform.scale(brelo, (100, 100))

font1 = pygame.font.Font(None, 40) #Fuentes de letras
font3 = pygame.font.Font(None, 70)
font2 = pygame.font.Font(None, 100)

zombies = [] #Lista de los zombies que apareceran
fballs = [] #Lista de las bolas de fuego en pantalla

puntaje = 0 #Inicializar puntaje y vida
vida = 10
pausa = False #Para controlar menus de pausa
gover = False #Para controlar menus de game over
inicio = True #Para controlar menus de inicio

#more images para el mapa del juego (objetos y demás):
map1 = pygame.image.load('Imagenes/map1.png')
map1 = pygame.transform.scale(map1, (50, 50))
map2 = pygame.image.load('Imagenes/map2.png')
map2 = pygame.transform.scale(map2, (50, 50))
map3 = pygame.image.load('Imagenes/map3.png')
map3 = pygame.transform.scale(map3, (50, 50))
map4 = pygame.image.load('Imagenes/map4.png')
map4 = pygame.transform.scale(map4, (50, 50))
map5 = pygame.image.load('Imagenes/map5.png')
map5 = pygame.transform.scale(map5, (50, 50))
map6 = pygame.image.load('Imagenes/map6.png')
map6 = pygame.transform.scale(map6, (50, 50))

mapa = [[1, 1, 1, 0, 0, 3, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1], #Mapa del juego representado en matriz
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 6, 0, 0, 1, 0, 2, 1, 0, 3, 0, 5, 0],
        [3, 0, 4, 0, 0, 5, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 5, 0, 1, 1, 4, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 2, 2, 2, 0, 3, 0, 0, 0, 2, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 6, 0, 5, 0, 6, 0],
        [0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 2, 0, 2, 0, 0, 1, 0, 0, 0, 6, 0, 0, 3, 0],
        [0, 0, 2, 0, 1, 0, 0, 1, 0, 6, 0, 0, 5, 0, 0, 0],
        [0, 0, 2, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 6, 0]]
    
playi = mf.player((7, 7)) #Posicion inicial del jugador
delzom = 0 #Para controlar el movimiento del zombie
creazom = 800 #Cada 400 iteraciones se creara zombies
delbal = 0 #Para controlar el movimiento de las bolas de fuego
vansa = 1 #Numero de zombies que se crearan
golp = False
cgol = 0
#
while run:
    pygame.time.delay(2) #delay
    screen.fill((255, 255, 255))
    if (inicio == True): #Pantalla de inicio
        screen.blit(mainf, (0,0)) #Fondo
        mtit = font2.render("ROOM SURVIVE", True, (20, 255, 45)) #Titulo del juego
        screen.blit(mtit, (130, 180))
        screen.blit(bplay, (350, 300)) #Boton para jugar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: #Comprobación si se presiono el boton para jugar?
                    if (event.pos[0] > 350) and (event.pos[0] < 450) and (event.pos[1] > 300) and (event.pos[1] < 400):
                        inicio = False #Salir de inicio
    elif (gover == True): #Pantalla de Game Over
        screen.blit(goverf, (0,0)) #Fondo
        mtit = font2.render("GAME OVER", True, (240, 20, 245)) #Titulo del Game Over
        screen.blit(mtit, (170, 170))
        ptjeg = font3.render("Puntaje: " + str(puntaje), True, (50, 50, 255)) #Texto de puntaje
        screen.blit(ptjeg, (250, 270)) 
        screen.blit(brelo, (330, 350)) #Boton para jugar denuevo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: #Se presiono el boton de jugar denuevo?
                    if (event.pos[0] > 330) and (event.pos[0] < 430) and (event.pos[1] > 350) and (event.pos[1] < 450):
                        gover = False #Inicializar todo y empezar nueva partida:
                        zombies = []
                        fballs = []
                        puntaje = 0
                        vida = 10
                        playi = mf.player((7, 7))
                        delzom = 0
                        creazom = 800
                        delbal = 0
                        vansa = 1
    elif (pausa == True): #Pantalla de pausa
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: #Se presiono el boton de reanudar?
                    if (event.pos[0] > 80) and (event.pos[0] < 180) and (event.pos[1] > 300) and (event.pos[1] < 400):
                        pausa = False #Reanudar
                    #Se presiono el boton de jugar de nuevo?
                    elif (event.pos[0] > 250) and (event.pos[0] < 350) and (event.pos[1] > 300) and (event.pos[1] < 400):
                        pausa = False #Inicializar todo y empezar nueva partida:
                        zombies = []
                        fballs = []
                        puntaje = 0
                        vida = 10
                        playi = mf.player((7, 7))
                        creazom = 800
                        delbal = 0
                        vansa = 1
        screen.blit(pausaf, (0,0)) #Fondo
        PausaTitle = font2.render("Pausa", True, (190, 80, 255)) #Titulo de pausa
        screen.blit(PausaTitle, (100, 100))
        screen.blit(bplay, (80, 300)) #Boton de reanudar
        screen.blit(brelo, (250, 300)) #Boton de jugar de nuevo
    elif (pausa != True and gover != True and inicio != True): #Pantalla de nivel o juego
        screen.blit(wallzomb, (0,0)) #Fondo
        limitcre = 800 - 20*vansa #Cada cuento se creara el zombie
        if limitcre <= 50: #Si es menor a 50
            limitcre = 50 #Sera 50
        if (creazom >= limitcre): #Creacion de los zombies
            sald = r.randint(1, 4) #De que parte del mapa saldra el zombie? (Aleatorio)
            if (sald == 1): #de la 1?
                zomb = mf.zombie((1, 0)) #Inicializar correspondientemente
            elif (sald == 2): #de la 2?
                zomb = mf.zombie((11, 0)) #Inicializar correspondientemente
            elif (sald == 3): #de la 3?
                zomb = mf.zombie((1, 15)) #Inicializar correspondientemente
            elif (sald == 4): #de la 4?
                zomb = mf.zombie((11, 15)) #Inicializar correspondientemente
            zombies.append(zomb) #Agregar a lista de zombies
            creazom = 0 #Incializar temporizador
            vansa = vansa + 1 #Aumentar la rapidez que salen cada vez los zombies
        else:
            creazom = creazom + 1 #Aumentar temporizador
        for i in range(len(mapa)):
            for j in range(len(mapa[0])): #LLenar el mapa correspondientemente a los numeros d la matriz
                if (mapa[i][j] == 1): #Con obstaculos u objetos diferentes dependiendo del numero
                    screen.blit(map1, (j*50,i*50)) #Objeto 1
                elif (mapa[i][j] == 2):
                    screen.blit(map2, (j*50,i*50)) #Objeto 2
                elif (mapa[i][j] == 3):
                    screen.blit(map3, (j*50,i*50)) #Objeto 3
                elif (mapa[i][j] == 4):
                    screen.blit(map4, (j*50,i*50)) #Objeto 4
                elif (mapa[i][j] == 5):
                    screen.blit(map5, (j*50,i*50)) #Objeto 5
                elif (mapa[i][j] == 6):
                    screen.blit(map6, (j*50,i*50)) #Objeto 6
        #
        if (delzom == 80): #Cada 40 iters los zombies se mueven
            for zm in zombies: 
                zm.caminar(playi.pos, mapa) #Todos los zombies se mueven calculando su ruta hacia el jugador con Astar
                if zm.atacar(playi.pos): #Si el zombie puede atacar al jugador
                    vida = vida - 1 #El jugador pierde vida
            delzom = 0 #Incializar temporizador
        else:
            delzom = delzom + 1 #Aumentar temporizador

        if (delbal == 10): #Cada 5 iters las bolas de fuego se mueven
            for idx, ba in enumerate(fballs): #Todas las bolas de fuego se mueve
                if ba.move(mapa) == False: 
                    fballs.pop(idx)
            delbal = 0 #Incializar temporizador
        else:
            delbal = delbal + 1 #Aumentar temporizador
        #Combrobar colisiones
        for ba in fballs:
            for iz, zi in enumerate(zombies): #Se comprueva si alguna bola de fuego choco con algun zombie?
                if (ba.pos == zi.pos):
                    zombies.pop(iz) #eliminar zombie si es así
                    puntaje = puntaje + 1 #Aumentar puntaje del jugador
        #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE: #Pausar si se apreto espacio
                    pausa = True
                ##
                if event.key == pygame.K_LEFT: #Que el jugador vaya a la izquierda si se apreta la flecha correspondiente
                    if playi.pos[1]-1 >= 0 and mapa[playi.pos[0]][playi.pos[1]-1] == 0:
                        playi.setpos(playi.pos[0],playi.pos[1]-1)
                if event.key == pygame.K_RIGHT: #Que el jugador vaya a la derecha si se apreta la flecha correspondiente
                    if playi.pos[1]+1 <= 15 and mapa[playi.pos[0]][playi.pos[1]+1] == 0:
                        playi.setpos(playi.pos[0],playi.pos[1]+1)
                if event.key == pygame.K_UP: #Que el jugador vaya arriba si se apreta la flecha correspondiente
                    if playi.pos[0]-1 >= 0 and mapa[playi.pos[0]-1][playi.pos[1]] == 0:
                        playi.setpos(playi.pos[0]-1,playi.pos[1])
                if event.key == pygame.K_DOWN: #Que el jugador vaya abajo si se apreta la flecha correspondiente
                    if playi.pos[0]+1 <= 11 and mapa[playi.pos[0]+1][playi.pos[1]] == 0:
                        playi.setpos(playi.pos[0]+1,playi.pos[1])
                ####
                if event.key == pygame.K_a and golp == False: #Que el jugador dispare bola de fuego a la izquierda si se apreta la flecha correspondiente
                    bali = mf.fireball((playi.pos[0],playi.pos[1]-1), 1) #Crear bola de fuego
                    golp = True
                    fballs.append(bali)
                if event.key == pygame.K_w and golp == False: #Que el jugador dispare bola de fuego arriba si se apreta la flecha correspondiente
                    bali = mf.fireball((playi.pos[0]-1,playi.pos[1]), 2) #Crear bola de fuego
                    golp = True
                    fballs.append(bali)
                if event.key == pygame.K_d and golp == False: #Que el jugador dispare bola de fuego a la derecha si se apreta la flecha correspondiente
                    bali = mf.fireball((playi.pos[0],playi.pos[1]+1), 3) #Crear bola de fuego
                    golp = True
                    fballs.append(bali)
                if event.key == pygame.K_s and golp == False: #Que el jugador dispare bola de fuego abajo si se apreta la flecha correspondiente
                    bali = mf.fireball((playi.pos[0]+1,playi.pos[1]), 4) #Crear bola de fuego
                    fballs.append(bali)
                    golp = True
        screen.blit(player,(playi.pos[1]*50, playi.pos[0]*50)) #Pintar al jugador
        for zm in zombies: #Pintar a los zombies
            if (zm.atckin == False): #Atacando si estan atacando
                screen.blit(zombi, (zm.pos[1]*50, zm.pos[0]*50))
            else: #O caminando si estan persiguiendo al jugador
                screen.blit(zatak, (zm.pos[1]*50, zm.pos[0]*50))
        for ba in fballs: #Pintar las bolas de fuego
            screen.blit(fball, (ba.pos[1]*50, ba.pos[0]*50))
        ptje = font1.render("Puntaje: " + str(puntaje), True, (150, 250, 55)) #Mostrar puntaje en pantalla
        screen.blit(ptje, (10, 10))
        vid = font1.render("Vida: " + str(vida), True, (240, 50, 255)) #Mostrar vida en pantalla
        screen.blit(vid, (660, 10))
        if (vida <= 0): #Si la vida se acaba
            gover = True #Ir a game over
        if (golp == True):
            cgol = cgol + 1
        if (cgol == 50):
            cgol = 0
            golp = False
    pygame.display.flip()
pygame.quit()
