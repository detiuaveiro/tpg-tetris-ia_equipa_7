from shape import Shape
import common


def next_key(state):
    pecas_sup = []
    pecas_sup.append(state['game'])
    # print(pecas_sup)
    current_piece = peca(state)
    next_piece = prox_peca(state)


    superf_ocup = pecas_sup.pop(0)

    keys = melhor_sitio(state)
    return keys


def prox_peca(state):
    peca = state['next_pieces'][0]
    if peca == [[3, 3], [4, 3], [3, 4], [4, 4]]:
        return "quadrado"
    elif peca == [[2, 4], [3, 4], [2, 5], [3, 5]]:
        return "L"
    elif peca == [[4, 4], [5, 4], [6, 4], [7, 4]]:
        return "I"


def melhor_sitio(state):
    peca1 = peca(state)
    if peca1 == "quadrado":
        keys = ["a", "a"]
    elif peca1 == "L":
        keys = ["w", "w", "w"]
    elif peca1 == "J":
        keys = ["w", "w", "w"]
    elif peca1 == "T":
        keys = ["w", "w", "w"]
    elif peca1 == "I":
        keys = ["w"]
    elif peca1 == "S":
        keys = ["w"]
    elif peca1 == "Z":
        keys = ["w"]
    else:
        keys=[]
    return keys

    
         
def peca(state):

    if state['piece'] == [[3, 3], [4, 3], [3, 4], [4, 4]]:  # quadrado
        return "quadrado"
    elif state['piece'] == [[4, 2], [4, 3], [4, 4], [5, 4]]:  # L

        return "L"
    elif state['piece'] == [[4, 2], [5, 2], [4, 3], [4, 4]]:  #J

        return "J"
    elif state['piece'] == [[4, 2], [4, 3], [5, 3], [4, 4]]:  # T

        return "T"
    elif state['piece'] == [[2, 2], [3, 2], [4, 2], [5, 2]]:  # I

        return "I"
    elif state['piece'] == [[4, 2], [4, 3], [5, 3], [5, 4]]:  # S

        return "S"
    elif state['piece'] == [[4, 2], [3, 3], [4, 3], [3, 4]]:  # Z
        return "Z"

def possible_moves(state):   # talvez fazer assim??? depois passar a lista de movimentos possiveis de cada peça para outra funçao, que vai calcular as coordenadas finais para cada movimento dependendo 
    moves = []               # das posiçoes já existentes no game, e usar função da heuristica pra determinar qual o melhor movimento?
    current_piece = peca(state)
    if current_piece == "quadrado":
        moves = [[""], ["a"], ["a","a"], ["d"], ["d", "d"], ["d", "d", "d"], ["d", "d", "d", "d"]]
    elif current_piece == "L":
        moves = [[""], ["a"], ["a","a"], ["a","a", "a"], ["d"], ["d", "d"], ["d", "d", "d"], ["w"], ["w","a"], ["w","a","a"], ["w","d"], ["w","d", "d"], ["w","d", "d", "d"], ["w", "w"], ["w","w","a"], ["w","w","a","a"], ["w","w","d"], ["w","w","d", "d"], ["w","w","d", "d", "d"], ["w","w","d", "d", "d", "d"], ["w", "w", "w"], ["w","w","w","a"], ["w","w","w","a","a"], ["w","w","w","d"], ["w","w","w","d", "d"], ["w","w","w","d", "d", "d"]]
    elif current_piece == "J":
        moves = [[""], ["a"], ["a","a"], ["a","a", "a"], ["d"], ["d", "d"], ["d", "d", "d"], ["w"], ["w","a"], ["w","a","a"], ["w","d"], ["w","d", "d"], ["w","d", "d", "d"], ["w", "w"], ["w","w","a"], ["w","w","a","a"], ["w","w","d"], ["w","w","d", "d"], ["w","w","d", "d", "d"], ["w","w","d", "d", "d", "d"], ["w", "w", "w"], ["w","w","w","a"], ["w","w","w","a","a"], ["w","w","w","d"], ["w","w","w","d", "d"], ["w","w","w","d", "d", "d"]]
    elif current_piece == "T":
        moves = [[""], ["a"], ["a","a"], ["a","a", "a"], ["d"], ["d", "d"], ["d", "d", "d"], ["w"], ["w","a"], ["w","a","a"], ["w","d"], ["w","d", "d"], ["w","d", "d", "d"], ["w", "w"], ["w","w","a"], ["w","w","a","a"], ["w","w","d"], ["w","w","d", "d"], ["w","w","d", "d", "d"], ["w","w","d", "d", "d", "d"], ["w", "w", "w"], ["w","w","w","a"], ["w","w","w","a","a"], ["w","w","w","d"], ["w","w","w","d", "d"], ["w","w","w","d", "d", "d"]]
    elif current_piece == "I":
        moves = [[""], ["a"], ["d", "d"], ["d", "d", "d"], ["w"], ["w","a"], ["w","a","a"], ["w","a","a","a"], ["w","d"], ["w","d", "d"], ["w","d", "d", "d"], ["w","d", "d", "d", "d"]]
    elif current_piece == "S":
        moves = [[""], ["a"], ["a", "a"], ["a", "a", "a"], ["d"], ["d", "d"], ["d", "d", "d"], ["w"], ["w","a"], ["w","a","a"], ["w","d"], ["w","d", "d"], ["w","d", "d", "d"]]
    elif current_piece == "Z":
        moves = [[""], ["a"], ["a", "a"], ["d"], ["d", "d"], ["d", "d", "d"], ["d", "d", "d", "d"], ["w"], ["w","a"], ["w","a","a"], ["w","d"], ["w","d", "d"], ["w","d", "d", "d"]]
    return moves

def possible_positions(state):
    current_piece = peca(state)
    if current_piece == "quadrado":
        moves = possible_moves(state)
        i=0
        while i<len(moves):
            move = moves[i]
            estado_final = final_state(state,move)   
                                                      #dependendo dos varios estados finais para cada move, adicionar cada estado final de cada move ao state game, calcular heuristicas para 
            #falta codigo                             # cada state game diferente e ver qual o melhor move a fazer

def final_state(state,move):
    current_piece = peca(state)
    if current_piece == "quadrado":
        initial_state = [[3, 3], [4, 3], [3, 4], [4, 4]]
        final_state = initial_state
        i=0
        while i<len(move):
            if move[i] == "a":
                j=0
                while j<len(initial_state):           # para cada coordenada
                    aux = final_state[j]
                    aux[0] = aux[0] - 1               # x vai 1 vez para a esquerda
                    final_state[j] = [aux[0], final_state[j][1]]
                    j += 1
            elif move[i] == "d":
                j=0
                while j<len(initial_state):
                    aux = final_state[j]
                    aux[0] = aux[0] + 1               # x vai 1 vez para a direita
                    final_state[j] = [aux[0], final_state[j][1]]
                    j += 1
            i += 1
        
        crosta = calculate_crust(state)
        x0 = final_state[0][0]
        x1 = final_state[1][0]
        x2 = final_state[2][0]
        x3 = final_state[3][0]

        crosta0 = crosta[x0]
        crosta1 = crosta[x1]
        crosta2 = crosta[x2]
        crosta3 = crosta[x3]
        
        crosta_list = [crosta0] + [crosta1] + [crosta2] + [crosta3]
        i = 0
        minimo = 30
        while i < len(crosta_list):
            if crosta_list[i] < minimo:
                minimo = crosta_list[i]
        
        j = 0
        while j < len(final_state):
            aux = final_state[j]
            aux[1] = minimo - 1
            final_state[i] = [final_state[i][0], aux[1]]     
        
    # elif   # falta fazer para restantes peças  (as restantes também têm o move[i] = "w")
                    








def calculate_total_height(state, x=10, y=30):
    column_heights_min= [y] * x
    for coordinate in state['game']:
        if coordinate[1] < column_heights_min[coordinate[0]]:
            column_heights_min[coordinate[0]]=coordinate[1]
    for value in range(0,x):
        column_heights_min[value] =y - column_heights_min[value]
    return column_heights_min


def calculate_holes(state, x=10, y=30):
    count = [0] * x
    max_height = [y] * x
    num_holes = 0
    for coordinate in state['game']:

        if max_height[coordinate[0]] > coordinate[1]:
            count[coordinate[0]] += 1
            max_height[coordinate[0]] = coordinate[1]

    for column in range(len(count)):
        if count[column] < y - 1 - max_height[column]:
            num_holes += 1
    return num_holes


def calculate_bumpiness(state, x=10, y=30):
    column_heights = calculate_total_height(state, x, y)
    column_heights = column_heights[1:]
    column_heights = column_heights[:-1]  # remover colunas das bordas 

    diffs = 0
    for value in range(len(column_heights) - 1):
        diffs += abs(column_heights[value] - column_heights[value + 1])

    return diffs


def calculate_free_spots(state, x=10, y=30):
    y_max = y - max(calculate_total_height(state, x, y))-1
    count = []
    for j in range(y_max, y):
        for i in range(1, 9):    # tirei indices das bordas
            coordinate = [i, j]
            if coordinate not in state['game']:
                count.append(coordinate)
    count.sort()
    return count

def calculate_crust(state, x=10, y=30):
    heights = calculate_total_height(state, x, y)
    crust= [0]* x
    for i in range(0, x):
        if [i,y-heights[i]-1] not in state['game']:
                crust[i] = (y-heights[i]-1)
    crust = crust[1:]
    crust = crust[:-1]  # remover bordas
    return crust

def piece_equation(state,x,y):
    equation=[]
    if state['next_pieces'][0] == [[1, 2], [2, 2], [1, 3], [2, 3]]:     #Q
        return [[x-1,y-1],[x,y-1],[x-1,y],[x,y]]

    elif state['next_pieces'][0]  == [[0, 1], [1, 1], [2, 1], [3, 1]]:  #I
        return [[x,y],[x+1,y],[x+2,y],[x+3,y]]

    elif state['next_pieces'][0]  == [[2, 1], [2, 2], [3, 2], [3, 3]]:  #S
        return [[x-1,y-2],[x-1,y-1],[x,y-1],[x,y+-1]]

    elif state['next_pieces'][0]  == [[2, 1], [1, 2], [2, 2], [1, 3]]:  #Z
        return [[x+1,y-2],[x,y-1],[x+1,y-1],[x,y]]

    elif state['next_pieces'][0] == [[2, 1], [3, 1], [2, 2], [2, 3]]:   #L
        return [[x-1,y-2],[x-1,y-1],[x-1,y],[x,y]]

    elif state['next_pieces'][0] == [[2, 1], [2, 2], [2, 3], [3, 3]]:   #J
        return [[x,y-2],[x+1,y-2],[x,y-1],[x,y]]

    elif state['next_pieces'][0]  == [[2, 1], [2, 2], [3, 2], [2, 3]]:  #T
        return [[x,y-2],[x,y-1],[x+1,y-1],[x,y]]

    return equation

def calculate_possible_spots(state, x=10, y=30):
    free_spots = calculate_free_spots(state, x=10, y=30)
    crust = calculate_crust(state, x=10, y=30)
    possible_spots = []
    for i in range(0,len(crust)):
        new_piece=piece_equation(state, i, crust[i])
        Test=True
        for coordinate in new_piece:
            if coordinate in state["game"] or coordinate[1] > crust[i] or coordinate[0] <= 0 or coordinate[0]>x-1 :
                Test=False
        if Test:
            possible_spots.append(new_piece)
    return possible_spots

def total_height(state):
    array_heights = calculate_total_height(state)
    total = 0
    for i in range(len(array_heights)):
        total += array_heights[i]
    return total



def heuristic(state):  # falta completar e fazer outras funçoes   def heuristic(state)
    lista_aggr = []

    a = -0.510066
    b =  0.760666
    c = -0.35663
    d = -0.184483

    for i in pos:  # pos é a lista de movimentos possiveis/coordenadas finais possiveis  (falta funçao)

        aggr = calculate_total_height(state)
        #comp    , falta funçao pra calcular completed lines
        hole = calculate_holes(state)
        bump = calculate_bumpiness (state)
        best_pos = (a*aggr) + (c*hole) + (d*bump) # + (b*comp)
        lista_aggr.append(best_pos)

    max_valor = max(lista_aggr)
    index_max_valor = lista_aggr.index(max_valor)
    best_pos = pos[max_value_index]

    return best_pos