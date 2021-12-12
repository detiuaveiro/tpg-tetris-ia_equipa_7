from shape import Shape
import common

def next_key(state):
    if state['piece'] == [[3, 3], [4, 3], [3, 4], [4, 4]]:
        peca = "quadrado"
        keys = possible_positions(state,peca)
    elif state['piece'] == [[2, 2], [3, 2], [4, 2], [5, 2]]:
        peca = "I"
        keys = possible_positions(state,peca)
    elif state['piece'] == [[4, 2], [4, 3], [5, 3], [4, 4]]:
        peca = "T"
        keys = possible_positions(state,peca)
    elif state['piece'] == [[4, 2], [4, 3], [5, 3], [5, 4]]:
        peca = "S"
        keys = possible_positions(state,peca)
    elif state['piece'] == [[4, 2], [3, 3], [4, 3], [3, 4]]:
        peca = "Z"
        keys = possible_positions(state,peca)
    elif state['piece'] == [[4, 2], [4, 3], [4, 4], [5, 4]]:
        peca = "L"
        keys = possible_positions(state,peca)
    elif state['piece'] == [[4, 2], [5, 2], [4, 3], [4, 4]]:
        peca = "J"
        keys = possible_positions(state,peca)
    else:
        keys = []
    
    return keys

def possible_moves(state,peca):
    moves = []
    if peca == "quadrado":
        moves = [["s"], ["a","s"], ["a","a","s"], ["d","s"], ["d", "d","s"], ["d", "d", "d","s"], ["d", "d", "d", "d","s"]]
    elif peca == "L":
        moves = [["s"], ["a","s"], ["a","a","s"], ["a","a", "a","s"], ["d","s"], ["d", "d","s"], ["d", "d", "d","s"], ["w","s"], ["w","a","s"], ["w","a","a","s"], ["w","d","s"], ["w","d", "d","s"], ["w","d", "d", "d","s"], ["w", "w","s"], ["w","w","a","s"], ["w","w","a","a","s"], ["w","w","d","s"], ["w","w","d", "d","s"], ["w","w","d", "d", "d","s"], ["w","w","d", "d", "d", "d","s"], ["w", "w", "w","s"], ["w","w","w","a","s"], ["w","w","w","a","a","s"], ["w","w","w","d","s"], ["w","w","w","d", "d","s"], ["w","w","w","d", "d", "d","s"]]
    elif peca == "J":
        moves = [["s"], ["a","s"], ["a","a","s"], ["a","a", "a","s"], ["d","s"], ["d", "d","s"], ["d", "d", "d","s"], ["w","s"], ["w","a","s"], ["w","a","a","s"], ["w","d","s"], ["w","d", "d","s"], ["w","d", "d", "d","s"], ["w", "w","s"], ["w","w","a","s"], ["w","w","a","a","s"], ["w","w","d","s"], ["w","w","d", "d","s"], ["w","w","d", "d", "d","s"], ["w","w","d", "d", "d", "d","s"], ["w", "w", "w","s"], ["w","w","w","a","s"], ["w","w","w","a","a","s"], ["w","w","w","d","s"], ["w","w","w","d", "d","s"], ["w","w","w","d", "d", "d","s"]]
    elif peca == "T":
        moves = [["s"], ["a","s"], ["a","a","s"], ["a","a", "a","s"], ["d","s"], ["d", "d","s"], ["d", "d", "d","s"], ["w","s"], ["w","a","s"], ["w","a","a","s"], ["w","d","s"], ["w","d", "d","s"], ["w","d", "d", "d","s"], ["w", "w","s"], ["w","w","a","s"], ["w","w","a","a","s"], ["w","w","d","s"], ["w","w","d", "d","s"], ["w","w","d", "d", "d","s"], ["w","w","d", "d", "d", "d","s"], ["w", "w", "w","s"], ["w","w","w","a","s"], ["w","w","w","a","a","s"], ["w","w","w","d","s"], ["w","w","w","d", "d","s"], ["w","w","w","d", "d", "d","s"]]
    elif peca == "I":
        moves = [["s"], ["a","s"], ["d","s"], ["d", "d","s"], ["d", "d", "d","s"], ["w","s"], ["w","a","s"], ["w","a","a","s"], ["w","a","a","a","s"], ["w","d","s"], ["w","d", "d","s"], ["w","d", "d", "d","s"], ["w","d", "d", "d", "d","s"]]
    elif peca == "S":
        moves = [["s"], ["a","s"], ["a", "a","s"], ["a", "a", "a","s"], ["d","s"], ["d", "d","s"], ["d", "d", "d","s"], ["w","s"], ["w","a","s"], ["w","a","a","s"], ["w","d","s"], ["w","d", "d","s"], ["w","d", "d", "d","s"]]
    elif peca == "Z":
        moves = [["s"], ["a","s"], ["a", "a","s"], ["d","s"], ["d", "d","s"], ["d", "d", "d","s"], ["d", "d", "d", "d","s"], ["w","s"], ["w","a","s"], ["w","a","a","s"], ["w","d","s"], ["w","d", "d","s"], ["w","d", "d", "d","s"]]
    return moves

def possible_positions(state,peca):
    moves = possible_moves(state,peca)
    i=0
    heuristic_list = []
    while i<len(moves): 
        lista_game = state['game']
        move = moves[i]
        estado_final = final_state_piece(state,move,peca)     
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
                                        


def final_state_piece(state,move,peca):
    if peca == "quadrado":
        initial_state = [[3, 3], [4, 3], [3, 4], [4, 4]]
        final_state = initial_state
        i=0
        while i<len(move)-1:
            if move[i] == "a":
                j=0
                while j<len(initial_state):          
                    aux = final_state[j]
                    aux[0] = aux[0] - 1               
                    final_state[j] = [aux[0], final_state[j][1]]
                    j += 1
            elif move[i] == "d":
                j=0
                while j<len(initial_state):
                    aux = final_state[j]
                    aux[0] = aux[0] + 1              
                    final_state[j] = [aux[0], final_state[j][1]]
                    j += 1
            i += 1

        crosta = calculate_crust(state["game"])
        x0 = final_state[0][0]
        x1 = final_state[1][0]

        crosta0 = crosta[x0-1]
        crosta1 = crosta[x1-1]
        crosta_list = [crosta0] + [crosta1]
        minimo = min(crosta_list)

        final_state[0] = [final_state[0][0], minimo]
        final_state[1] = [final_state[1][0], minimo]
        final_state[2] = [final_state[2][0], minimo - 1]
        final_state[3] = [final_state[3][0], minimo - 1]
        return final_state

    elif peca == "I":
        initial_state =  [[2, 2], [3, 2], [4, 2], [5, 2]]
        final_state = initial_state
        i=0
        houve_w = False
        while i<len(move)-1:
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

                houve_w = True
            
            elif move[i] == "a":
                j=0
                while j<len(initial_state):           
                    aux = final_state[j]
                    aux[0] = aux[0] - 1               
                    final_state[j] = [aux[0], final_state[j][1]]
                    j += 1
            elif move[i] == "d":
                j=0
                while j<len(initial_state):
                    aux = final_state[j]
                    aux[0] = aux[0] + 1               
                    final_state[j] = [aux[0], final_state[j][1]]
                    j += 1
            i += 1

        if houve_w == False:
            crosta = calculate_crust(state["game"])

            x0 = final_state[0][0]
            x1 = final_state[1][0]
            x2 = final_state[2][0]
            x3 = final_state[3][0]

            crosta0 = crosta[x0-1]
            crosta1 = crosta[x1-1]
            crosta2 = crosta[x2-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta0] + [crosta1] + [crosta2] + [crosta3]
            minimo = min(crost_temp)

            final_state[0] = [final_state[0][0], minimo]
            final_state[1] = [final_state[1][0], minimo]
            final_state[2] = [final_state[2][0], minimo]
            final_state[3] = [final_state[3][0], minimo]
                
        else:
            crosta = calculate_crust(state["game"])

            x0 = final_state[0][0]
            crosta0 = crosta[x0-1]
    
            final_state[0] = [final_state[0][0], crosta0 - 3]
            final_state[1] = [final_state[1][0], crosta0 - 2]
            final_state[2] = [final_state[2][0], crosta0 - 1]
            final_state[3] = [final_state[3][0], crosta0]

        return final_state

    elif peca == "T":
        initial_state =  [[4, 2], [4, 3], [5, 3], [4, 4]]
        final_state = initial_state
        i=0
        houve_w0 = False
        houve_w1 = False
        houve_w2 = False
        while i<len(move)-1:
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
                    
                    houve_w2 = True
                
            elif move[i] == "a":
                j=0
                while j<len(initial_state):         
                    aux = final_state[j]
                    aux[0] = aux[0] - 1               
                    final_state[j] = [aux[0], final_state[j][1]]
                    j += 1
            elif move[i] == "d":
                j=0
                while j<len(initial_state):
                    aux = final_state[j]
                    aux[0] = aux[0] + 1             
                    final_state[j] = [aux[0], final_state[j][1]]
                    j += 1
            i += 1
        
        if houve_w0 == False:    # [[4, 2], [4, 3], [5, 3], [4, 4]]  não rodou nenhuma vez
            crosta = calculate_crust(state["game"])

            x0 = final_state[0][0] 
            x2 = final_state[2][0]
            

            crosta0 = crosta[x0-1]
            crosta2 = crosta[x2-1]

            crost_temp = [crosta0] + [crosta2] 
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
    
            x0 = final_state[0][0] 
            x1 = final_state[1][0]
            x2 = final_state[2][0]
            

            crosta0 = crosta[x0-1]
            crosta1 = crosta[x1-1]
            crosta2 = crosta[x2-1]

            crost_temp = [crosta0] + [crosta1] + [crosta2] 

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
            x1 = final_state[1][0] 
            x3 = final_state[3][0]
            

            crosta1 = crosta[x1-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta1] + [crosta3] 
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
            x1 = final_state[1][0] 
            x2 = final_state[2][0]
            x3 = final_state[3][0]

            crosta1 = crosta[x1-1]
            crosta2 = crosta[x2-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta1] + [crosta2] + [crosta3] 
            minimo = min(crost_temp)

            final_state[0] = [final_state[0][0], minimo-1]
            final_state[1] = [final_state[1][0], minimo]
            final_state[2] = [final_state[2][0], minimo]
            final_state[3] = [final_state[3][0], minimo]
        return final_state 

    elif peca == "S":
        initial_state =  [[4, 2], [4, 3], [5, 3], [5, 4]]
        final_state = initial_state
        i=0
        houve_w = False
        while i<len(move)-1:
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

                houve_w = True
            
            elif move[i] == "a":
                j=0
                while j<len(initial_state):          
                    aux = final_state[j]
                    aux[0] = aux[0] - 1               
                    final_state[j] = [aux[0], final_state[j][1]]
                    j += 1
            elif move[i] == "d":
                j=0
                while j<len(initial_state):
                    aux = final_state[j]
                    aux[0] = aux[0] + 1              
                    final_state[j] = [aux[0], final_state[j][1]]
                    j += 1
                    
                   
            i += 1
        
        if houve_w==False:    # [[4, 2], [4, 3], [5, 3], [5, 4]]
            crosta = calculate_crust(state["game"])
        
            x1 = final_state[1][0]
            x3 = final_state[3][0]

            crosta1 = crosta[x1-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta1] + [crosta3]
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
        else:                                                       #[[4, 4], [5, 4], [3, 5], [4, 5]]
            crosta = calculate_crust(state["game"])
    
            x1 = final_state[1][0]
            x2 = final_state[2][0]
            x3 = final_state[3][0]
           
            crosta1 = crosta[x1-1]
            crosta2 = crosta[x2-1]
            crosta3 = crosta[x3-1]
           

            crost_temp = [crosta1] + [crosta2] + [crosta3]

            minimo = min(crost_temp)
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

    elif peca == "Z":
        initial_state =  [[4, 2], [3, 3], [4, 3], [3, 4]]
        final_state = initial_state
        i=0
        houve_w = False
        while i<len(move)-1:
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


                houve_w = True
            
            elif move[i] == "a":
                j=0
                while j<len(initial_state):           
                    aux = final_state[j]
                    aux[0] = aux[0] - 1               
                    final_state[j] = [aux[0], final_state[j][1]]
                    j += 1
            elif move[i] == "d":
                j=0
                while j<len(initial_state):
                    aux = final_state[j]
                    aux[0] = aux[0] + 1              
                    final_state[j] = [aux[0], final_state[j][1]]
                    j += 1
            i += 1
        
        if houve_w==False:     # [[4, 2], [3, 3], [4, 3], [3, 4]]
            crosta = calculate_crust(state["game"])
           
            x2 = final_state[2][0]
            x3 = final_state[3][0]

            crosta2 = crosta[x2-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta2] + [crosta3]
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
        else:                                                       #[[3, 4], [4, 4], [4, 5], [5, 5]] 
            crosta = calculate_crust(state["game"])
            
            x0 = final_state[0][0]
            x2 = final_state[2][0]
            x3 = final_state[3][0]

            crosta0 = crosta[x0-1]
            crosta2 = crosta[x2-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta0] + [crosta2] + [crosta3]
            minimo = min(crost_temp)
           
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

    elif peca == "L":
        initial_state =  [[4, 2], [4, 3], [4, 4], [5, 4]] 
        final_state = initial_state
        i=0
        houve_w0 = False
        houve_w1 = False
        houve_w2 = False
        while i<len(move)-1:
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
                   
                    houve_w2 = True
                
            elif move[i] == "a":
                j=0
                while j<len(initial_state):          
                    aux = final_state[j]
                    aux[0] = aux[0] - 1               
                    final_state[j] = [aux[0], final_state[j][1]]
                    j += 1
            elif move[i] == "d":
                j=0
                while j<len(initial_state):
                    aux = final_state[j]
                    aux[0] = aux[0] + 1               
                    final_state[j] = [aux[0], final_state[j][1]]
                    j += 1
            i += 1
        
        if houve_w0 == False:    # [[4, 2], [4, 3], [4, 4], [5, 4]]  não rodou nenhuma vez
            crosta = calculate_crust(state["game"])
           
            x2 = final_state[2][0] 
            x3 = final_state[3][0]
            

            crosta2 = crosta[x2-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta2] + [crosta3] 
            minimo = min(crost_temp)

            final_state[0] = [final_state[0][0], minimo-2]
            final_state[1] = [final_state[1][0], minimo-1]
            final_state[2] = [final_state[2][0], minimo]
            final_state[3] = [final_state[3][0], minimo]

        elif houve_w1 == False:    # [[3, 4], [4, 4], [5, 4], [3, 5]]   #rodou uma vez, pois houve_w0 deu True no if acima
            crosta = calculate_crust(state["game"])
           
            x1 = final_state[1][0]
            x2 = final_state[2][0]
            x3 = final_state[3][0]
            
            crosta1 = crosta[x1-1]
            crosta2 = crosta[x2-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta1] + [crosta2] + [crosta3] 
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
            
            x0 = final_state[0][0] 
            x3 = final_state[3][0]
            

            crosta0 = crosta[x0-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta0] + [crosta3] 
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
           
            x1 = final_state[1][0] 
            x2 = final_state[2][0]
            x3 = final_state[3][0]

            crosta1 = crosta[x1-1]
            crosta2 = crosta[x2-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta1] + [crosta2] + [crosta3] 
            minimo = min(crost_temp)

            final_state[0] = [final_state[0][0], minimo-1]
            final_state[1] = [final_state[1][0], minimo]
            final_state[2] = [final_state[2][0], minimo]
            final_state[3] = [final_state[3][0], minimo]
        return final_state

    elif peca == "J":
        initial_state =  [[4, 2], [5, 2], [4, 3], [4, 4]]
        final_state = initial_state
        i=0
        houve_w0 = False
        houve_w1 = False
        houve_w2 = False
        while i<len(move)-1:
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
                  
                    houve_w2 = True
                
            elif move[i] == "a":
                j=0
                while j<len(initial_state):           
                    aux = final_state[j]
                    aux[0] = aux[0] - 1               
                    final_state[j] = [aux[0], final_state[j][1]]
                    j += 1
            elif move[i] == "d":
                j=0
                while j<len(initial_state):
                    aux = final_state[j]
                    aux[0] = aux[0] + 1               
                    final_state[j] = [aux[0], final_state[j][1]]
                    j += 1
            i += 1
        
        if houve_w0 == False:    # [[4, 2], [5, 2], [4, 3], [4, 4]]  não rodou nenhuma vez
            crosta = calculate_crust(state["game"])
            
            x1 = final_state[1][0] 
            x3 = final_state[3][0]
            

            crosta1 = crosta[x1-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta1] + [crosta3] 
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
            
            x0 = final_state[0][0]
            x1 = final_state[1][0]
            x3 = final_state[3][0]
            
            crosta0 = crosta[x0-1]
            crosta1 = crosta[x1-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta0] + [crosta1] + [crosta3] 
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
            
            x2 = final_state[2][0] 
            x3 = final_state[3][0]
            

            crosta2 = crosta[x2-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta2] + [crosta3] 
            minimo = min(crost_temp)

            final_state[0] = [final_state[0][0], minimo-2]
            final_state[1] = [final_state[1][0], minimo-1]
            final_state[2] = [final_state[2][0], minimo]
            final_state[3] = [final_state[3][0], minimo]
            

        else:                       # [[3, 5], [3, 6], [4, 6], [5, 6]]   #rodou tres vezes, pois houve_w2 deu True no if acima
            crosta = calculate_crust(state["game"])
           
            x1 = final_state[1][0] 
            x2 = final_state[2][0]
            x3 = final_state[3][0]

            crosta1 = crosta[x1-1]
            crosta2 = crosta[x2-1]
            crosta3 = crosta[x3-1]

            crost_temp = [crosta1] + [crosta2] + [crosta3] 
            minimo = min(crost_temp)

            final_state[0] = [final_state[0][0], minimo-1]
            final_state[1] = [final_state[1][0], minimo]
            final_state[2] = [final_state[2][0], minimo]
            final_state[3] = [final_state[3][0], minimo]
        return final_state

def calculate_total_height(state, x=10, y=30):
    column_heights_min= [y] * x
    for coordinate in state: 
        if coordinate[1] < column_heights_min[coordinate[0]]:
            column_heights_min[coordinate[0]]=coordinate[1]
    for value in range(0,x):
        column_heights_min[value] = y - column_heights_min[value]

    return column_heights_min

def calculate_holes(state, x=10, y=30):
    num_holes = 0

    for i in range(1,9):
        col = [0]*33
        for fragment in state:
            x,y = fragment
            if x==i and y<30:
                col[29-y]=1
        j=29
        while j>=0:
            if col[j]==1:
                while j>=0:
                    if col[j]==0:
                        num_holes=num_holes + 1
                    j=j-1
                break
            j=j-1
    return num_holes

def calculate_bumpiness(state, x=10, y=30):
    column_heights = calculate_total_height(state, x, y)
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
            crust[i] = (y-heights[i]-1)
    crust = crust[1:]
    crust = crust[:-1]  
    return crust

def calculate_completed_lines(game_state,piece=None,x=10,y=30):

    columns=[0]*(y)
    line=0
    for coordinate in game_state:
        columns[coordinate[1]-1]+=1
    columns = columns[:-1]
    for value in columns:
        if value==x-2:
            line+=1
    return line
def total_height(state):
    array_heights = calculate_total_height(state)
    total = 0
    for i in range(len(array_heights)):
        total += array_heights[i]
    return total

def heuristic(lista):  

    a = -0.510066
    b =  0.760666
    c = -0.35663
    d = -0.184483
    
    aggr = total_height(lista)
    comp = calculate_completed_lines(lista)
    hole = calculate_holes(lista)
    bump = calculate_bumpiness (lista)
    best_pos = (a*aggr) + (b*comp) + (c*hole) + (d*bump) 

    return best_pos