from shape import Shape
import common


def next_key(state):
    current_piece = peca(state)
    next_piece = prox_peca(state)
    if peca(state) == "quadrado":
        keys = possible_positions(state)
    elif peca(state) == "I":
        keys = possible_positions(state)
    elif peca(state) == "T":
        keys = possible_positions(state)
    elif peca(state) == "S":
        keys = possible_positions(state)
    elif peca(state) == "Z":
        keys = possible_positions(state)
    elif peca(state) == "L":
        keys = possible_positions(state)
    elif peca(state) == "J":
        keys = possible_positions(state)
    else:
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
        keys = ["w", "w"]
    elif peca1 == "T":
        keys = ["w"]
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
        moves = [["s"], ["a","s"], ["a","a","s"], ["d","s"], ["d", "d","s"], ["d", "d", "d","s"], ["d", "d", "d", "d","s"]]
    elif current_piece == "L":
        moves = [["s"], ["a","s"], ["a","a","s"], ["a","a", "a","s"], ["d","s"], ["d", "d","s"], ["d", "d", "d","s"], ["w","s"], ["w","a","s"], ["w","a","a","s"], ["w","d","s"], ["w","d", "d","s"], ["w","d", "d", "d","s"], ["w", "w","s"], ["w","w","a","s"], ["w","w","a","a","s"], ["w","w","d","s"], ["w","w","d", "d","s"], ["w","w","d", "d", "d","s"], ["w","w","d", "d", "d", "d","s"], ["w", "w", "w","s"], ["w","w","w","a","s"], ["w","w","w","a","a","s"], ["w","w","w","d","s"], ["w","w","w","d", "d","s"], ["w","w","w","d", "d", "d","s"]]
    elif current_piece == "J":
        moves = [["s"], ["a","s"], ["a","a","s"], ["a","a", "a","s"], ["d","s"], ["d", "d","s"], ["d", "d", "d","s"], ["w","s"], ["w","a","s"], ["w","a","a","s"], ["w","d","s"], ["w","d", "d","s"], ["w","d", "d", "d","s"], ["w", "w","s"], ["w","w","a","s"], ["w","w","a","a","s"], ["w","w","d","s"], ["w","w","d", "d","s"], ["w","w","d", "d", "d","s"], ["w","w","d", "d", "d", "d","s"], ["w", "w", "w","s"], ["w","w","w","a","s"], ["w","w","w","a","a","s"], ["w","w","w","d","s"], ["w","w","w","d", "d","s"], ["w","w","w","d", "d", "d","s"]]
    elif current_piece == "T":
        moves = [["s"], ["a","s"], ["a","a","s"], ["a","a", "a","s"], ["d","s"], ["d", "d","s"], ["d", "d", "d","s"], ["w","s"], ["w","a","s"], ["w","a","a","s"], ["w","d","s"], ["w","d", "d","s"], ["w","d", "d", "d","s"], ["w", "w","s"], ["w","w","a","s"], ["w","w","a","a","s"], ["w","w","d","s"], ["w","w","d", "d","s"], ["w","w","d", "d", "d","s"], ["w","w","d", "d", "d", "d","s"], ["w", "w", "w","s"], ["w","w","w","a","s"], ["w","w","w","a","a","s"], ["w","w","w","d","s"], ["w","w","w","d", "d","s"], ["w","w","w","d", "d", "d","s"]]
    elif current_piece == "I":
        moves = [["s"], ["a","s"], ["d","s"], ["d", "d","s"], ["d", "d", "d","s"], ["w","s"], ["w","a","s"], ["w","a","a","s"], ["w","a","a","a","s"], ["w","d","s"], ["w","d", "d","s"], ["w","d", "d", "d","s"], ["w","d", "d", "d", "d","s"]]
    elif current_piece == "S":
        moves = [["s"], ["a","s"], ["a", "a","s"], ["a", "a", "a","s"], ["d","s"], ["d", "d","s"], ["d", "d", "d","s"], ["w","s"], ["w","a","s"], ["w","a","a","s"], ["w","d","s"], ["w","d", "d","s"], ["w","d", "d", "d","s"]]
    elif current_piece == "Z":
        moves = [["s"], ["a","s"], ["a", "a","s"], ["d","s"], ["d", "d","s"], ["d", "d", "d","s"], ["d", "d", "d", "d","s"], ["w","s"], ["w","a","s"], ["w","a","a","s"], ["w","d","s"], ["w","d", "d","s"], ["w","d", "d", "d","s"]]
    return moves

def possible_positions(state):
        current_piece = peca(state)
        moves = possible_moves(state)
        i=0
        heuristic_list = []
        while i<len(moves): 
            lista_game = state['game']
            move = moves[i]
            estado_final = final_state_piece(state,move,current_piece)
            for coord in estado_final:
                lista_game.append(coord)    
            h = heuristic(lista_game)
            state['game'] = lista_game[:-4]
            heuristic_list.append(h)   
            i += 1
        max_value = max(heuristic_list)
        max_value_index = heuristic_list.index(max_value) 
        best_move = moves[max_value_index]
        return best_move

def final_state_piece(state,move,current_piece):
    if current_piece == "quadrado":
        ##print(current_piece)
        initial_state = [[3, 3], [4, 3], [3, 4], [4, 4]]
        final_state = initial_state
        i=0
        while i<len(move):
            # #print(len(move))
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

        crosta = calculate_crust(state["game"])
        # #print(crosta)
        x0 = final_state[0][0]
        x1 = final_state[1][0]

        crosta0 = crosta[x0-1]
        crosta1 = crosta[x1-1]
        # #print(crosta0)
        # #print(crosta1)

        crosta_list = [crosta0] + [crosta1]
        # #print(crosta_list)
        minimo = min(crosta_list)
        # #print(minimo)

        final_state[0] = [final_state[0][0], minimo]
        final_state[1] = [final_state[1][0], minimo]
        final_state[2] = [final_state[2][0], minimo - 1]
        final_state[3] = [final_state[3][0], minimo - 1]
        # #print(final_state)
        return final_state

    elif current_piece == "I":
        ##print(current_piece)
        initial_state =  [[2, 2], [3, 2], [4, 2], [5, 2]]
        final_state = initial_state
        i=0
        houve_w = False
        while i<len(move):
            if move[i] == "w":
                aux0 = final_state[0]
                aux1 = final_state[1]
                aux2 = final_state[2]
                aux3 = final_state[3]

                aux0 = [aux0[0]+2, aux0[1]]                     #[[4, 2], [4, 3], [4, 4], [4, 5]], depois de um w
                aux1 = [aux1[0]+1, aux1[1]+1]
                aux2 = [aux2[0], aux2[1]+2]
                aux3 = [aux3[0]-1,aux3[1]+3]

                final_state[0] = aux0
                final_state[1] = aux1
                final_state[2] = aux2
                final_state[3] = aux3

                # #print(final_state)

                houve_w = True
            
            elif move[i] == "a":
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
                    # #print("AQUI------")
                    # #print(final_state)
            i += 1

        if houve_w == False:
            crosta = calculate_crust(state["game"])
            # #print(crosta)
            x0 = final_state[0][0]
            x1 = final_state[1][0]
            x2 = final_state[2][0]
            x3 = final_state[3][0]

            crosta0 = crosta[x0-1]
            crosta1 = crosta[x1-1]
            crosta2 = crosta[x2-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta0] + [crosta1] + [crosta2] + [crosta3]
            # #print(crost_temp)

            minimo = min(crost_temp)
            # #print(minimo)

            final_state[0] = [final_state[0][0], minimo]
            final_state[1] = [final_state[1][0], minimo]
            final_state[2] = [final_state[2][0], minimo]
            final_state[3] = [final_state[3][0], minimo]
                # #print(final_state)
        else:
            crosta = calculate_crust(state["game"])

            x0 = final_state[0][0]
            crosta0 = crosta[x0-1]
    
            final_state[0] = [final_state[0][0], crosta0 - 3]
            final_state[1] = [final_state[1][0], crosta0 - 2]
            final_state[2] = [final_state[2][0], crosta0 - 1]
            final_state[3] = [final_state[3][0], crosta0]
            # #print(final_state)

        return final_state

    elif current_piece == "T":
        ##print(current_piece)
        initial_state =  [[4, 2], [4, 3], [5, 3], [4, 4]]
        final_state = initial_state
        i=0
        houve_w0 = False
        houve_w1 = False
        houve_w2 = False
        while i<len(move):
            if move[i] == "w":
                if houve_w0 == False:
                    aux0 = final_state[0]
                    aux1 = final_state[1]
                    aux2 = final_state[2]
                    aux3 = final_state[3]

                    aux0 = [aux0[0]-1, aux0[1]+2]                     #[[3, 4], [4, 4], [5, 4], [4, 5]], depois de um w
                    aux1 = [aux1[0], aux1[1]+1]
                    aux2 = [aux2[0], aux2[1]+1]
                    aux3 = [aux3[0],aux3[1]+1]

                    final_state[0] = aux0
                    final_state[1] = aux1
                    final_state[2] = aux2
                    final_state[3] = aux3

                    # #print(final_state)
                    houve_w0 = True
                elif houve_w1 == False:     
                    aux0 = final_state[0]                  # [[4, 4], [3, 5], [4, 5], [4, 6]], depois de 2 w's
                    aux1 = final_state[1]           
                    aux2 = final_state[2]
                    aux3 = final_state[3]

                    aux0 = [aux0[0]+1, aux0[1]]                     
                    aux1 = [aux1[0]-1, aux1[1]+1]
                    aux2 = [aux2[0]-1, aux2[1]+1]
                    aux3 = [aux3[0],aux3[1]+1]

                    final_state[0] = aux0
                    final_state[1] = aux1
                    final_state[2] = aux2
                    final_state[3] = aux3
                    # #print(final_state)
                    houve_w1 = True
                elif houve_w2 == False:     
                    aux0 = final_state[0]                  # [[4, 5], [3, 6], [4, 6], [5, 6]], depois de 3 w's
                    aux1 = final_state[1]           
                    aux2 = final_state[2]
                    aux3 = final_state[3]

                    aux0 = [aux0[0], aux0[1]+1]                     
                    aux1 = [aux1[0], aux1[1]+1]
                    aux2 = [aux2[0], aux2[1]+1]
                    aux3 = [aux3[0]+1,aux3[1]]

                    final_state[0] = aux0
                    final_state[1] = aux1
                    final_state[2] = aux2
                    final_state[3] = aux3
                    # #print(final_state)
                    houve_w2 = True
                
            elif move[i] == "a":
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
                    # #print("AQUI------")
                    # #print(final_state)
            i += 1
        
        if houve_w0 == False:    # [[4, 2], [4, 3], [5, 3], [4, 4]]  não rodou nenhuma vez
            crosta = calculate_crust(state["game"])
            # #print(crosta)
            x0 = final_state[0][0] 
            x2 = final_state[2][0]
            

            crosta0 = crosta[x0-1]
            crosta2 = crosta[x2-1]

            crost_temp = [crosta0] + [crosta2] 
            ##print(crost_temp)
            minimo = min(crost_temp)

            if minimo==crosta0:
                final_state[0] = [final_state[0][0], minimo-2]
                final_state[1] = [final_state[1][0], minimo-1]
                final_state[2] = [final_state[2][0], minimo-1]
                final_state[3] = [final_state[3][0], minimo]
            else:
                final_state[0] = [final_state[0][0], minimo-1]
                final_state[1] = [final_state[1][0], minimo]
                final_state[2] = [final_state[2][0], minimo]
                final_state[3] = [final_state[3][0], minimo+1]

        elif houve_w1 == False:    # [[3, 4], [4, 4], [5, 4], [4, 5]]   #rodou uma vez, pois houve_w0 deu True no if acima
            crosta = calculate_crust(state["game"])
            # #print(crosta)
            x0 = final_state[0][0] 
            x1 = final_state[1][0]
            x2 = final_state[2][0]
            

            crosta0 = crosta[x0-1]
            crosta1 = crosta[x1-1]
            crosta2 = crosta[x2-1]

            crost_temp = [crosta0] + [crosta1] + [crosta2] 
            # #print(crost_temp)

            minimo = min(crost_temp)
            if minimo == crosta1:
                final_state[0] = [final_state[0][0], minimo-1]
                final_state[1] = [final_state[1][0], minimo-1]
                final_state[2] = [final_state[2][0], minimo-1]
                final_state[3] = [final_state[3][0], minimo]
            else:
                final_state[0] = [final_state[0][0], minimo]
                final_state[1] = [final_state[1][0], minimo]
                final_state[2] = [final_state[2][0], minimo]
                final_state[3] = [final_state[3][0], minimo+1]

        elif houve_w2 == False:    # [[4, 4], [3, 5], [4, 5], [4, 6]]   #rodou duas vezes, pois houve_w1 deu True no if acima
            crosta = calculate_crust(state["game"])
            # #print(crosta)
            x1 = final_state[1][0] 
            x3 = final_state[3][0]
            

            crosta1 = crosta[x1-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta1] + [crosta3] 
            # #print(crost_temp)
            minimo = min(crost_temp)

            if minimo==crosta3:
                final_state[0] = [final_state[0][0], minimo-2]
                final_state[1] = [final_state[1][0], minimo-1]
                final_state[2] = [final_state[2][0], minimo-1]
                final_state[3] = [final_state[3][0], minimo]
            else:
                final_state[0] = [final_state[0][0], minimo-1]
                final_state[1] = [final_state[1][0], minimo]
                final_state[2] = [final_state[2][0], minimo]
                final_state[3] = [final_state[3][0], minimo+1]

        else:                       # [[4, 5], [3, 6], [4, 6], [5, 6]]   #rodou tres vezes, pois houve_w2 deu True no if acima
            crosta = calculate_crust(state["game"])
            # #print(crosta)
            x1 = final_state[1][0] 
            x2 = final_state[2][0]
            x3 = final_state[3][0]

            crosta1 = crosta[x1-1]
            crosta2 = crosta[x2-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta1] + [crosta2] + [crosta3] 
            # #print(crost_temp)
            minimo = min(crost_temp)

            final_state[0] = [final_state[0][0], minimo-1]
            final_state[1] = [final_state[1][0], minimo]
            final_state[2] = [final_state[2][0], minimo]
            final_state[3] = [final_state[3][0], minimo]
        return final_state 

    elif current_piece == "S":
        ##print(current_piece)
        initial_state =  [[4, 2], [4, 3], [5, 3], [5, 4]]
        final_state = initial_state
        i=0
        houve_w = False
        while i<len(move):
            if move[i] == "w":
                aux0 = final_state[0]
                aux1 = final_state[1]
                aux2 = final_state[2]
                aux3 = final_state[3]

                aux0 = [aux0[0], aux0[1]+2]                     #[[4, 4], [5, 4], [3, 5], [4, 5]], depois de um w
                aux1 = [aux1[0]+1, aux1[1]+1]                   #[[4, 2], [4, 3], [5, 3], [5, 4]]
                aux2 = [aux2[0]-2, aux2[1]+2]
                aux3 = [aux3[0]-1,aux3[1]+1]

                final_state[0] = aux0
                final_state[1] = aux1
                final_state[2] = aux2
                final_state[3] = aux3

                # #print(final_state)

                houve_w = True
            
            elif move[i] == "a":
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
                    # #print("AQUI------")
                    # #print(final_state)
            i += 1
        
        if houve_w==False:    # [[4, 2], [4, 3], [5, 3], [5, 4]]
            crosta = calculate_crust(state["game"])
            # #print(crosta)
            x1 = final_state[1][0]
            x3 = final_state[3][0]

            crosta1 = crosta[x1-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta1] + [crosta3]
            # #print(crost_temp)

            minimo = min(crost_temp)
            # #print(minimo)
            if minimo==crosta3:
                final_state[0] = [final_state[0][0], minimo-2]
                final_state[1] = [final_state[1][0], minimo-1]
                final_state[2] = [final_state[2][0], minimo-1]
                final_state[3] = [final_state[3][0], minimo]
            else:
                final_state[0] = [final_state[0][0], minimo-1]
                final_state[1] = [final_state[1][0], minimo]
                final_state[2] = [final_state[2][0], minimo]
                final_state[3] = [final_state[3][0], minimo+1]
        else:                                                       #[[4, 4], [5, 4], [3, 5], [4, 5]]
            crosta = calculate_crust(state["game"])
            # #print(crosta)
            x1 = final_state[1][0]
            x2 = final_state[2][0]
            x3 = final_state[3][0]
           
            crosta1 = crosta[x1-1]
            crosta2 = crosta[x2-1]
            crosta3 = crosta[x3-1]
           

            crost_temp = [crosta1] + [crosta2] + [crosta3]
            # #print(crost_temp)

            minimo = min(crost_temp)
            # #print(minimo)
            if minimo==crosta2 or minimo==crosta3:
                final_state[0] = [final_state[0][0], minimo-1]
                final_state[1] = [final_state[1][0], minimo-1]
                final_state[2] = [final_state[2][0], minimo]
                final_state[3] = [final_state[3][0], minimo]
            else:
                final_state[0] = [final_state[0][0], minimo]
                final_state[1] = [final_state[1][0], minimo]
                final_state[2] = [final_state[2][0], minimo+1]
                final_state[3] = [final_state[3][0], minimo+1]
        return final_state

    elif current_piece == "Z":
        ##print(current_piece)
        initial_state =  [[4, 2], [3, 3], [4, 3], [3, 4]]
        final_state = initial_state
        i=0
        houve_w = False
        while i<len(move):
            if move[i] == "w":
                aux0 = final_state[0]
                aux1 = final_state[1]
                aux2 = final_state[2]
                aux3 = final_state[3]
                                                                 # [[4, 2], [3, 3], [4, 3], [3, 4]]
                aux0 = [aux0[0]-1, aux0[1]+2]                    # [[3, 4], [4, 4], [4, 5], [5, 5]] depois de w
                aux1 = [aux1[0]+1, aux1[1]+1]                     
                aux2 = [aux2[0], aux2[1]+2]
                aux3 = [aux3[0]+2,aux3[1]+1]

                final_state[0] = aux0
                final_state[1] = aux1
                final_state[2] = aux2
                final_state[3] = aux3

                # #print(final_state)

                houve_w = True
            
            elif move[i] == "a":
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
                    # #print("AQUI------")
                    # #print(final_state)
            i += 1
        
        if houve_w==False:     # [[4, 2], [3, 3], [4, 3], [3, 4]]
            crosta = calculate_crust(state["game"])
            # #print(crosta)
            x2 = final_state[2][0]
            x3 = final_state[3][0]

            crosta2 = crosta[x2-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta2] + [crosta3]
            # #print(crost_temp)

            minimo = min(crost_temp)
            # #print(minimo)
            if minimo==crosta3:
                final_state[0] = [final_state[0][0], minimo-2]
                final_state[1] = [final_state[1][0], minimo-1]
                final_state[2] = [final_state[2][0], minimo-1]
                final_state[3] = [final_state[3][0], minimo]
            else:
                final_state[0] = [final_state[0][0], minimo-1]
                final_state[1] = [final_state[1][0], minimo]
                final_state[2] = [final_state[2][0], minimo]
                final_state[3] = [final_state[3][0], minimo+1]
        else:                                                       #[[3, 4], [4, 4], [4, 5], [5, 5]] 
            crosta = calculate_crust(state["game"])
            # #print(crosta)
            x0 = final_state[0][0]
            x2 = final_state[2][0]
            x3 = final_state[3][0]

            crosta0 = crosta[x0-1]
            crosta2 = crosta[x2-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta0] + [crosta2] + [crosta3]
            # #print(crost_temp)

            minimo = min(crost_temp)
            # #print(minimo)
            if minimo==crosta2 or minimo==crosta3:
                final_state[0] = [final_state[0][0], minimo-1]
                final_state[1] = [final_state[1][0], minimo-1]
                final_state[2] = [final_state[2][0], minimo]
                final_state[3] = [final_state[3][0], minimo]
            else:
                final_state[0] = [final_state[0][0], minimo]
                final_state[1] = [final_state[1][0], minimo]
                final_state[2] = [final_state[2][0], minimo+1]
                final_state[3] = [final_state[3][0], minimo+1]
        return final_state

    elif current_piece == "L":
        #(current_piece)
        initial_state =  [[4, 2], [4, 3], [4, 4], [5, 4]] 
        final_state = initial_state
        i=0
        houve_w0 = False
        houve_w1 = False
        houve_w2 = False
        while i<len(move):
            if move[i] == "w":
                if houve_w0 == False:
                    aux0 = final_state[0]
                    aux1 = final_state[1]
                    aux2 = final_state[2]
                    aux3 = final_state[3]
                                                                      #[[4, 2], [4, 3], [4, 4], [5, 4]]
                    aux0 = [aux0[0]-1, aux0[1]+2]                     #[[3, 4], [4, 4], [5, 4], [3, 5]] , depois de 1 w
                    aux1 = [aux1[0], aux1[1]+1]                       
                    aux2 = [aux2[0]+1, aux2[1]]
                    aux3 = [aux3[0]-2,aux3[1]+1]

                    final_state[0] = aux0
                    final_state[1] = aux1
                    final_state[2] = aux2
                    final_state[3] = aux3

                    # #print(final_state)
                    houve_w0 = True
                elif houve_w1 == False:                    # [[3, 4], [4, 4], [5, 4], [3, 5]]
                    aux0 = final_state[0]                  # [[3, 4], [4, 4], [4, 5], [4, 6]], depois de 2 w's 
                    aux1 = final_state[1]           
                    aux2 = final_state[2]
                    aux3 = final_state[3]

                    aux0 = [aux0[0], aux0[1]]                     
                    aux1 = [aux1[0], aux1[1]]
                    aux2 = [aux2[0]-1, aux2[1]+1]
                    aux3 = [aux3[0]+1,aux3[1]+1]

                    final_state[0] = aux0
                    final_state[1] = aux1
                    final_state[2] = aux2
                    final_state[3] = aux3
                    # #print(final_state)
                    houve_w1 = True
                elif houve_w2 == False:                    # [[3, 4], [4, 4], [4, 5], [4, 6]]
                    aux0 = final_state[0]                  # [[5, 5], [3, 6], [4, 6], [5, 6]], depois de 3 w's 
                    aux1 = final_state[1]           
                    aux2 = final_state[2]
                    aux3 = final_state[3]

                    aux0 = [aux0[0]+2, aux0[1]-1]                     
                    aux1 = [aux1[0]-1, aux1[1]+2]
                    aux2 = [aux2[0], aux2[1]+1]
                    aux3 = [aux3[0]+1,aux3[1]]

                    final_state[0] = aux0
                    final_state[1] = aux1
                    final_state[2] = aux2
                    final_state[3] = aux3
                    # #print(final_state)
                    houve_w2 = True
                
            elif move[i] == "a":
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
                    # #print("AQUI------")
                    # #print(final_state)
            i += 1
        
        if houve_w0 == False:    # [[4, 2], [4, 3], [4, 4], [5, 4]]  não rodou nenhuma vez
            crosta = calculate_crust(state["game"])
            # #print(crosta)
            x2 = final_state[2][0] 
            x3 = final_state[3][0]
            

            crosta2 = crosta[x2-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta2] + [crosta3] 
            # #print(crost_temp)
            minimo = min(crost_temp)

            final_state[0] = [final_state[0][0], minimo-2]
            final_state[1] = [final_state[1][0], minimo-1]
            final_state[2] = [final_state[2][0], minimo]
            final_state[3] = [final_state[3][0], minimo]

        elif houve_w1 == False:    # [[3, 4], [4, 4], [5, 4], [3, 5]]   #rodou uma vez, pois houve_w0 deu True no if acima
            crosta = calculate_crust(state["game"])
            # #print(crosta)
            x1 = final_state[1][0]
            x2 = final_state[2][0]
            x3 = final_state[3][0]
            
            crosta1 = crosta[x1-1]
            crosta2 = crosta[x2-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta1] + [crosta2] + [crosta3] 
            # #print(crost_temp)

            minimo = min(crost_temp)

            if minimo == crosta3: 
                final_state[0] = [final_state[0][0], minimo-1]
                final_state[1] = [final_state[1][0], minimo-1]
                final_state[2] = [final_state[2][0], minimo-1]
                final_state[3] = [final_state[3][0], minimo]
            else:
                final_state[0] = [final_state[0][0], minimo]
                final_state[1] = [final_state[1][0], minimo]
                final_state[2] = [final_state[2][0], minimo]
                final_state[3] = [final_state[3][0], minimo+1]

        elif houve_w2 == False:    # # [[3, 4], [4, 4], [4, 5], [4, 6]]   #rodou duas vezes, pois houve_w1 deu True no if acima
            crosta = calculate_crust(state["game"])
            # #print(crosta)
            x0 = final_state[0][0] 
            x3 = final_state[3][0]
            

            crosta0 = crosta[x0-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta0] + [crosta3] 
            # #print(crost_temp)

            minimo = min(crost_temp)

            if crosta0 - crosta3 < -1:
                minimo = crosta0
                final_state[0] = [final_state[0][0], minimo]
                final_state[1] = [final_state[1][0], minimo]
                final_state[2] = [final_state[2][0], minimo+1]
                final_state[3] = [final_state[3][0], minimo+2]
            elif crosta0 - crosta3 == -1:
                minimo = crosta0
                final_state[0] = [final_state[0][0], minimo-1]
                final_state[1] = [final_state[1][0], minimo-1]
                final_state[2] = [final_state[2][0], minimo]
                final_state[3] = [final_state[3][0], minimo+1]
            else:
                minimo = crosta3
                final_state[0] = [final_state[0][0], minimo-2]
                final_state[1] = [final_state[1][0], minimo-2]
                final_state[2] = [final_state[2][0], minimo-1]
                final_state[3] = [final_state[3][0], minimo]

        else:                       # [[5, 5], [3, 6], [4, 6], [5, 6]]   #rodou tres vezes, pois houve_w2 deu True no if acima
            crosta = calculate_crust(state["game"])
            # #print(crosta)
            x1 = final_state[1][0] 
            x2 = final_state[2][0]
            x3 = final_state[3][0]

            crosta1 = crosta[x1-1]
            crosta2 = crosta[x2-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta1] + [crosta2] + [crosta3] 
            # #print(crost_temp)
            minimo = min(crost_temp)

            final_state[0] = [final_state[0][0], minimo-1]
            final_state[1] = [final_state[1][0], minimo]
            final_state[2] = [final_state[2][0], minimo]
            final_state[3] = [final_state[3][0], minimo]
        return final_state

    elif current_piece == "J":
        ##print(current_piece)
        initial_state =  [[4, 2], [5, 2], [4, 3], [4, 4]]
        final_state = initial_state
        i=0
        houve_w0 = False
        houve_w1 = False
        houve_w2 = False
        while i<len(move):
            if move[i] == "w":
                if houve_w0 == False:
                    aux0 = final_state[0]
                    aux1 = final_state[1]
                    aux2 = final_state[2] 
                    aux3 = final_state[3]
                                                                      #[[4, 2], [5, 2], [4, 3], [4, 4]]
                    aux0 = [aux0[0]-1, aux0[1]+2]                     #[[3, 4], [4, 4], [5, 4], [5, 5]], depois de um w
                    aux1 = [aux1[0]-1, aux1[1]+2]
                    aux2 = [aux2[0]+1, aux2[1]+1]
                    aux3 = [aux3[0]+1,aux3[1]+1]

                    final_state[0] = aux0
                    final_state[1] = aux1
                    final_state[2] = aux2
                    final_state[3] = aux3

                    # #print(final_state)
                    houve_w0 = True
                elif houve_w1 == False:                    # [[3, 4], [4, 4], [5, 4], [5, 5]]
                    aux0 = final_state[0]                  # [[4, 4], [4, 5], [3, 6], [4, 6]], depois de 2 w's 
                    aux1 = final_state[1]           
                    aux2 = final_state[2]
                    aux3 = final_state[3]

                    aux0 = [aux0[0]+1, aux0[1]]                     
                    aux1 = [aux1[0], aux1[1]+1]
                    aux2 = [aux2[0]-2, aux2[1]+2]
                    aux3 = [aux3[0]-1,aux3[1]+1]

                    final_state[0] = aux0
                    final_state[1] = aux1
                    final_state[2] = aux2
                    final_state[3] = aux3
                    # #print(final_state)
                    houve_w1 = True
                elif houve_w2 == False:                    # [[4, 4], [4, 5], [3, 6], [4, 6]]
                    aux0 = final_state[0]                  # [[3, 5], [3, 6], [4, 6], [5, 6]], depois de 3 w's 
                    aux1 = final_state[1]           
                    aux2 = final_state[2]
                    aux3 = final_state[3]

                    aux0 = [aux0[0]-1, aux0[1]+1]                     
                    aux1 = [aux1[0]-1, aux1[1]+1]
                    aux2 = [aux2[0]+1, aux2[1]]
                    aux3 = [aux3[0]+1,aux3[1]]

                    final_state[0] = aux0
                    final_state[1] = aux1
                    final_state[2] = aux2
                    final_state[3] = aux3
                    # #print(final_state)
                    houve_w2 = True
                
            elif move[i] == "a":
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
                    # #print("AQUI------")
                    # #print(final_state)
            i += 1
        
        if houve_w0 == False:    # [[4, 2], [5, 2], [4, 3], [4, 4]]  não rodou nenhuma vez
            crosta = calculate_crust(state["game"])
            # #print(crosta)
            x1 = final_state[1][0] 
            x3 = final_state[3][0]
            

            crosta1 = crosta[x1-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta1] + [crosta3] 
            # #print(crost_temp)

            minimo = min(crost_temp)

            if crosta3 - crosta1 > 1:
                minimo = crosta1
                final_state[0] = [final_state[0][0], minimo]
                final_state[1] = [final_state[1][0], minimo]
                final_state[2] = [final_state[2][0], minimo+1]
                final_state[3] = [final_state[3][0], minimo+2]
            elif crosta3 - crosta1 == 1:
                minimo = crosta1
                final_state[0] = [final_state[0][0], minimo-1]
                final_state[1] = [final_state[1][0], minimo-1]
                final_state[2] = [final_state[2][0], minimo]
                final_state[3] = [final_state[3][0], minimo+1]
            else:
                minimo = crosta3
                final_state[0] = [final_state[0][0], minimo-2]
                final_state[1] = [final_state[1][0], minimo-2]
                final_state[2] = [final_state[2][0], minimo-1]
                final_state[3] = [final_state[3][0], minimo]

        elif houve_w1 == False:    # [[3, 4], [4, 4], [5, 4], [5, 5]]   #rodou uma vez, pois houve_w0 deu True no if acima
            crosta = calculate_crust(state["game"])
            # #print(crosta)
            x0 = final_state[0][0]
            x1 = final_state[1][0]
            x3 = final_state[3][0]
            
            crosta0 = crosta[x0-1]
            crosta1 = crosta[x1-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta0] + [crosta1] + [crosta3] 
            # #print(crost_temp)

            minimo = min(crost_temp)

            if minimo == crosta3: 
                final_state[0] = [final_state[0][0], minimo-1]
                final_state[1] = [final_state[1][0], minimo-1]
                final_state[2] = [final_state[2][0], minimo-1]
                final_state[3] = [final_state[3][0], minimo]
            else:
                final_state[0] = [final_state[0][0], minimo]
                final_state[1] = [final_state[1][0], minimo]
                final_state[2] = [final_state[2][0], minimo]
                final_state[3] = [final_state[3][0], minimo+1]

        elif houve_w2 == False:    # [[4, 4], [4, 5], [3, 6], [4, 6]]  #rodou duas vezes, pois houve_w1 deu True no if acima
            crosta = calculate_crust(state["game"])
            # #print(crosta)
            x2 = final_state[2][0] 
            x3 = final_state[3][0]
            

            crosta2 = crosta[x2-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta2] + [crosta3] 
            # #print(crost_temp)

            minimo = min(crost_temp)

            final_state[0] = [final_state[0][0], minimo-2]
            final_state[1] = [final_state[1][0], minimo-1]
            final_state[2] = [final_state[2][0], minimo]
            final_state[3] = [final_state[3][0], minimo]
            

        else:     # [[3, 5], [3, 6], [4, 6], [5, 6]]   #rodou tres vezes, pois houve_w2 deu True no if acima
            crosta = calculate_crust(state["game"])
            # #print(crosta)
            x1 = final_state[1][0] 
            x2 = final_state[2][0]
            x3 = final_state[3][0]

            crosta1 = crosta[x1-1]
            crosta2 = crosta[x2-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta1] + [crosta2] + [crosta3] 
            # #print(crost_temp)
            minimo = min(crost_temp)

            final_state[0] = [final_state[0][0], minimo-1]
            final_state[1] = [final_state[1][0], minimo]
            final_state[2] = [final_state[2][0], minimo]
            final_state[3] = [final_state[3][0], minimo]
        return final_state


def calculate_total_height(state, x=10, y=30):
    column_heights_min= [y] * x
    for coordinate in state: #mudei
        if coordinate[1] < column_heights_min[coordinate[0]]:
            column_heights_min[coordinate[0]]=coordinate[1]
    for value in range(0,x):
        column_heights_min[value] = y - column_heights_min[value]

    return column_heights_min

def calculate_holes(state, x_max=10, y_max=30):
    num_holes = 0
    for i in range(1,x_max-1):
        col = [0]*33
        for fragment in state:
            x,y = fragment
            if x==i and y<y_max:
                col[(y_max-1)-y]=1
        j=(y_max-1)
        while j>=0:
            if col[j]==1:
                while j>=0:
                    if col[j]==0:
                        num_holes=num_holes + 1
                    j=j-1
                break
            j=j-1
    return num_holes

def calculate_bumpiness(state,column_heights, x=10, y=30):
    column_heights = column_heights[1:]
    column_heights = column_heights[:-1]

    diffs = 0
    for value in range(len(column_heights) - 1):
        diffs += abs(column_heights[value] - column_heights[value + 1])

    return diffs


def calculate_crust(state, x=10, y=30):
    heights = calculate_total_height(state, x, y)
    crust= [0]* x
    for i in range(0, x):
        if [i,y-heights[i]-1] not in state:
                crust[i] = (y-heights[i]-1)
    crust = crust[1:]
    crust = crust[:-1]  # remover bordas
    return crust




def calculate_completed_lines(state,x=10,y=30):
    game_state= state
    columns=[0]*(y)
    line=0
    for coordinate in game_state:
        columns[coordinate[1]-1]+=1
    columns = columns[:-1]
    for value in columns:
        if value==x-2:
            line+=1
    return line

def total_height(state,array_heights):
    #print(array_heights)
    total = 0
    for i in range(len(array_heights)):
        total += array_heights[i]
    return total

def heuristic(lista):
    # #print(lista)

    a = -0.510066
    b =  0.760666
    c = -0.35663
    d = -0.184483
    tt_height=calculate_total_height(lista)
    aggr = total_height(lista,tt_height)
    comp = calculate_completed_lines(lista)
    hole = calculate_holes(lista)
    bump = calculate_bumpiness (lista,tt_height)
    best_pos = (a*aggr) + (c*hole) + (d*bump) + (b*comp)
    # lista_aggr.append(best_pos)
    # #print(aggr,comp,hole,bump)
    # max_valor = max(lista_aggr)
    # index_max_valor = lista_aggr.index(max_valor)
    # best_pos = pos[max_value_index]

    return best_pos

def piece_equation(piece,x,y):
    equation=[]
    if piece == "Q":
        return [[x-1,y-1],[x,y-1],[x-1,y],[x,y]]

    elif piece == "I":
        return [[x,y],[x+1,y],[x+2,y],[x+3,y]]

    elif piece == "S":
        return [[x-1,y-2],[x-1,y-1],[x,y-1],[x,y+-1]]

    elif piece == "Z":
        return [[x+1,y-2],[x,y-1],[x+1,y-1],[x,y]]

    elif piece == "L":
        return [[x-1,y-2],[x-1,y-1],[x-1,y],[x,y]]

    elif piece == "J":
        return [[x,y-2],[x+1,y-2],[x,y-1],[x,y]]

    elif piece== "T":
        return [[x,y-2],[x,y-1],[x+1,y-1],[x,y]]
    return equation

def nextpiece_type(state):
    if  state['next_pieces'][0]  == [[1, 2], [2, 2], [1, 3], [2, 3]]:   # Q
        return "Q"
    elif state['next_pieces'][0] == [[0, 1], [1, 1], [2, 1], [3, 1]]:   # I
        return "I"
    elif state['next_pieces'][0] == [[2, 1], [2, 2], [3, 2], [3, 3]]:   # S
        return "S"
    elif state['next_pieces'][0] == [[2, 1], [1, 2], [2, 2], [1, 3]]:   # Z
        return "Z"
    elif state['next_pieces'][0] == [[2, 1], [3, 1], [2, 2], [2, 3]]:   # L
        return "L"
    elif state['next_pieces'][0] == [[2, 1], [2, 2], [2, 3], [3, 3]]:   # J
        return "J"
    elif state['next_pieces'][0] == [[2, 1], [2, 2], [3, 2], [2, 3]]:   # T
        return "T"

def calculate_possible_spots(state, x=10, y=30):
    crust = calculate_crust(state, x=10, y=30)
    possible_spots = []
    next_piece = nextpiece_type(state)
    for i in range(0,len(crust)):
        new_piece=piece_equation(next_piece, i, crust[i])
        Test=True
        for coordinate in new_piece:
            if coordinate in state["game"] or coordinate[1] > crust[i] or coordinate[1]<0 or coordinate[0] <= 0 or coordinate[0]>=x-1 :
                Test=False
        if Test:
            possible_spots.append(new_piece)
    return possible_spots


def calculate_free_spots(state, x=10, y=30):
    y_max = y - max(calculate_total_height(state, x, y))-1
    count = []
    for j in range(y_max, y):
        for i in range(1, x-1):    # tirei indices das bordas
            coordinate = [i, j]
            if coordinate not in state['game']:
                count.append(coordinate)
    count.sort()
    return count