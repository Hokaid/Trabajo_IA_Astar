import math

class node(): #Con esta clase se crean los nodos correspondientes a las posiciones que se analizaran en el algoritmo Astar
    def __init__(self, dad=None, pos=None):
        self.dad = dad
        self.pos = pos
        self.g = 0
        self.h = 0
        self.f = 0
    def __eq__(self, otro):
        return self.pos == otro.pos

def astar(mapi, ini, obj): #Algoritmo Astar
    nodoini = node(None, ini) #Se inicializa el nodo de posición inicial
    nodoini.g = nodoini.h = nodoini.f = 0 
    nodofin = node(None, obj) #Se reconoce el nodo objetivo
    nodofin.g = nodofin.h = nodofin.f = 0
    lopen = [] #Lista Abierta
    lclose = [] #Lista Cerrada
    lopen.append(nodoini) #Agregando el nodo inicio a la lista
    iters = 0
    while len(lopen) > 0: # mientras que la lista abierta tenga elementos
        iters = iters + 1
        nodoact = lopen[0] # obtener el nodo actual con f minima
        indxac = 0
        for ind, item in enumerate(lopen):
            if item.f < nodoact.f:
                nodoact = item
                indxac = ind
        lopen.pop(indxac) # sacar de la lista abierta y meter a la lista cerrada
        lclose.append(nodoact)
        # Encuentra el objetivo
        #Puesto que Astar busca lo optimo, tiende a tardarse, lo cual afecta la fluidez del juego, ya que este algoritmo se llama a cada rato
        #Por ello, se pone un limite de 200 iteraciones, aceptando la solucion parcial que nos podria retornar
        #Solucion que, para propositos del juego, es más que suficiente
        if nodoact == nodofin or iters == 200: #Limite de 200 iteraciones para no volver lento el juego
            path = []
            current = nodoact
            while current is not None:
                path.append(current.pos)
                current = current.dad
            return path[::-1] 
        suce = [] # Genera los sucesores
        for p in [(0, -1), (0, 1), (-1, 0), (1, 0)]: 
            nodepo = (nodoact.pos[0] + p[0], nodoact.pos[1] + p[1]) #Get Nodo posicion
            # Asegurarse que está en el rango
            if nodepo[0] > (len(mapi) - 1) or nodepo[0] < 0 or nodepo[1] > (len(mapi[len(mapi)-1]) -1) or nodepo[1] < 0:
                continue
            # asegurase del camino transitable
            if mapi[nodepo[0]][nodepo[1]] != 0:
                continue
            nodenew = node(nodoact, nodepo)# crear nuevo nodo
            suce.append(nodenew)# agregar dicho nodo
        for su in suce: # tratando los sucesores
            for closed_child in lclose: # sucesor esta en la lista cerrada
                if su == closed_child:
                    continue
            su.g = nodoact.g + 1 # creando los valores f,g,h
            su.h = math.sqrt((su.pos[0] - nodofin.pos[0])**2 + (su.pos[1] - nodofin.pos[1])**2)
            su.f = su.g + su.h
            for nopen in lopen: # sucesor esta ya en la lisa abierta
                if su == nopen and su.g > nopen.g:
                    continue
            lopen.append(su) # agregando sucesor en la lista abierta

class zombie(): #Clase para modelar al zombie
    def __init__(self, pos=None):
        self.pos = pos #Posicion del zombie
        self.path = [] #Camino a recorrer del zombie
        self.poway = 0 #posicion en el camino inicial del zombie
        self.objpos = (-1,-1) #posicion objetivo inicializada
        self.atckin = False #Para ver si el zombie puede atacar

    def atacar(self, ppos): #Funcion atacar al objetivo
        if (self.pos == ppos): #Encontramos al objetivo?
            self.atckin = True #Atacar
            return True
        self.atckin = False #No Atacar
        return False
        
    def caminar(self, ppos, mapa): #Funcion para ir hasta el objetivo
        if (ppos != self.objpos): #El objetivo se ha movido?
            self.path = astar(mapa, self.pos, ppos) #Volver a calcular ruta
            self.poway = 0
            self.pos = self.path[self.poway] #Recorrer ruta
            self.objpos = ppos #Modificar la posicion del objetivo
        if (self.poway < len(self.path) - 1): #No terminamos de recorrer la ruta encontrada?
            self.poway = self.poway + 1 #Seguir caminando por dicha ruta
            self.pos = self.path[self.poway] #Hacia el objetivo

class player():
    def __init__(self, pos=None):
        self.pos = pos #Posicion del jugador
    def setpos(self, x, y):
        self.pos = (x, y) #Cambiar posicion

class fireball():
    def __init__(self, pos=None, dire =0):
        self.pos = pos #posicion de la bola de fuego
        self.dire = dire #direccion de la bola de fuego
    def move(self, mapa): #Funcion para mover bola de fuego
        if (self.dire == 1): #Si la direccion es 1?
            if self.pos[1]-1 >= 0 and mapa[self.pos[0]][self.pos[1]-1] == 0: #Si no hemos llegado a los limites o chocado con algo?
                self.pos = (self.pos[0],self.pos[1]-1) #Mover correspondientemente
                return True
        if (self.dire == 2):#Si la direccion es 2?
            if self.pos[0]-1 >= 0 and mapa[self.pos[0]-1][self.pos[1]] == 0: #Si no hemos llegado a los limites o chocado con algo?
                self.pos = (self.pos[0]-1,self.pos[1])#Mover correspondientemente
                return True
        if (self.dire == 3):#Si la direccion es 3?
            if self.pos[1]+1 <= 15 and mapa[self.pos[0]][self.pos[1]+1] == 0: #Si no hemos llegado a los limites o chocado con algo?
                self.pos = (self.pos[0],self.pos[1]+1)#Mover correspondientemente
                return True
        if (self.dire == 4):#Si la direccion es 4?
            if self.pos[0]+1 <= 11 and mapa[self.pos[0]+1][self.pos[1]] == 0:#Si no hemos llegado a los limites o chocado con algo?
                self.pos = (self.pos[0]+1,self.pos[1])#Mover correspondientemente
                return True
        return False

