from shape import Shape
import common

def next_key(state):

    pecas_sup = []
    pecas_sup.append(state['game'])
    #print(pecas_sup)
    current_piece = peca(state)
    next_piece = prox_peca(state)

    # if state['game'] != []:
    #     print(state['game'][0])
    superf_ocup = pecas_sup.pop(0)

    keys = melhor_sitio(state).copy()

    
    # if current_piece == "quadrado": 
    #     keys = ["d", "d", "d", "d"]
    # elif current_piece == "I":
    #     keys = ["w", "a", "a", "a"]
    # elif current_piece == "L":
    #     keys = ["d", "w", "w", "w"]
    # elif current_piece == "J":
    #     keys = ["a", "w", "w"]
    # else:
    #     keys = []
    return keys

def prox_peca(state):
    peca = state['next_pieces'][0]
    if peca == [[3,3], [4,3], [3,4], [4,4]]:
        return "quadrado"
    elif peca == [[2,4], [3,4], [2,5], [3,5]]:
        return "L"
    elif peca == [[4,4], [5,4], [6,4], [7,4]]:
        return "I"

def melhor_sitio(state):
    if peca(state) == "quadrado":
        if state['game'] == []:
            keys = ["d", "d", "d", "d"]
        else:
            if [1,29] not in state['game'] and [2,29] not in state['game'] and [1,28] not in state['game'] and [2,28] not in state['game']:
                keys = ["a", "a", "a", "a"]
            elif [2,29] not in state['game'] and [3,29] not in state['game'] and [2,28] not in state['game'] and [3,28] not in state['game']:
                keys = ["a"]
            elif [3,29] not in state['game'] and [4,29] not in state['game'] and [3,28] not in state['game'] and [4,28] not in state['game']:
                keys = []
            elif [4,29] not in state['game'] and [5,29] not in state['game'] and [4,28] not in state['game'] and [5,28] not in state['game']:
                keys = ["d"]
            elif [5,29] not in state['game'] and [6,29] not in state['game'] and [5,28] not in state['game'] and [6,28] not in state['game']:
                keys = ["d", "d"]
            elif [6,29] not in state['game'] and [7,29] not in state['game'] and [6,28] not in state['game'] and [7,28] not in state['game']:
                keys = ["d", "d", "d"]
            elif [7,29] not in state['game'] and [8,29] not in state['game'] and [7,28] not in state['game'] and [8,28] not in state['game']: #fim quadrado 1 camada
                keys = ["d", "d", "d", "d"]
            
            #### 1 camada-----------
            
            elif [1,28] not in state['game'] and [2,28] not in state['game'] and [1,27] not in state['game'] and [2,27] not in state['game']:
                keys = ["a", "a", "a", "a"]
            elif [2,28] not in state['game'] and [3,28] not in state['game'] and [2,27] not in state['game'] and [3,27] not in state['game']:
                keys = ["a"]
            elif [3,28] not in state['game'] and [4,28] not in state['game'] and [3,27] not in state['game'] and [4,27] not in state['game']:
                keys = []
            elif [4,28] not in state['game'] and [5,28] not in state['game'] and [4,27] not in state['game'] and [5,27] not in state['game']:
                keys = ["d"]
            elif [5,28] not in state['game'] and [6,28] not in state['game'] and [5,27] not in state['game'] and [6,27] not in state['game']:
                keys = ["d", "d"]
            elif [6,28] not in state['game'] and [7,28] not in state['game'] and [6,27] not in state['game'] and [7,27] not in state['game']:
                keys = ["d", "d", "d"]
            elif [7,28] not in state['game'] and [8,28] not in state['game'] and [7,27] not in state['game'] and [8,27] not in state['game']:#fim quadrado 2 camada
                keys = ["d", "d", "d", "d"]

            ### 2 camada-----------

            elif [1,27] not in state['game'] and [2,27] not in state['game'] and [1,26] not in state['game'] and [2,26] not in state['game']:
                keys = ["a", "a", "a", "a"]
            elif [2,27] not in state['game'] and [3,27] not in state['game'] and [2,26] not in state['game'] and [3,26] not in state['game']:
                keys = ["a"]
            elif [3,27] not in state['game'] and [4,27] not in state['game'] and [3,26] not in state['game'] and [4,26] not in state['game']:
                keys = []
            elif [4,27] not in state['game'] and [5,27] not in state['game'] and [4,26] not in state['game'] and [5,26] not in state['game']:
                keys = ["d"]
            elif [5,27] not in state['game'] and [6,27] not in state['game'] and [5,26] not in state['game'] and [6,26] not in state['game']:
                keys = ["d", "d"]
            elif [6,27] not in state['game'] and [7,27] not in state['game'] and [6,26] not in state['game'] and [7,26] not in state['game']:
                keys = ["d", "d", "d"]
            elif [7,27] not in state['game'] and [8,27] not in state['game'] and [7,26] not in state['game'] and [8,26] not in state['game']:#fim quadrado 3 camada
                keys = ["d", "d", "d", "d"]

            ### 3 camada-----------

            elif [1,26] not in state['game'] and [2,26] not in state['game'] and [1,25] not in state['game'] and [2,25] not in state['game']:
                keys = ["a", "a", "a", "a"]
            elif [2,26] not in state['game'] and [3,26] not in state['game'] and [2,25] not in state['game'] and [3,25] not in state['game']:
                keys = ["a"]
            elif [3,26] not in state['game'] and [4,26] not in state['game'] and [3,25] not in state['game'] and [4,25] not in state['game']:
                keys = []
            elif [4,26] not in state['game'] and [5,26] not in state['game'] and [4,25] not in state['game'] and [5,25] not in state['game']:
                keys = ["d"]
            elif [5,26] not in state['game'] and [6,26] not in state['game'] and [5,25] not in state['game'] and [6,25] not in state['game']:
                keys = ["d", "d"]
            elif [6,26] not in state['game'] and [7,26] not in state['game'] and [6,25] not in state['game'] and [7,25] not in state['game']:
                keys = ["d", "d", "d"]
            elif [7,26] not in state['game'] and [8,26] not in state['game'] and [7,25] not in state['game'] and [8,25] not in state['game']:#fim quadrado 4 camada
                keys = ["d", "d", "d", "d"]

                ### 4 camada-----------

            elif [1,25] not in state['game'] and [2,25] not in state['game'] and [1,24] not in state['game'] and [2,24] not in state['game']:
                keys = ["a", "a", "a", "a"]
            elif [2,25] not in state['game'] and [3,25] not in state['game'] and [2,24] not in state['game'] and [3,24] not in state['game']:
                keys = ["a"]
            elif [3,25] not in state['game'] and [4,25] not in state['game'] and [3,24] not in state['game'] and [4,24] not in state['game']:
                keys = []
            elif [4,25] not in state['game'] and [5,25] not in state['game'] and [4,24] not in state['game'] and [5,24] not in state['game']:
                keys = ["d"]
            elif [5,25] not in state['game'] and [6,25] not in state['game'] and [5,24] not in state['game'] and [6,24] not in state['game']:
                keys = ["d", "d"]
            elif [6,25] not in state['game'] and [7,25] not in state['game'] and [6,24] not in state['game'] and [7,24] not in state['game']:
                keys = ["d", "d", "d"]
            elif [7,25] not in state['game'] and [8,25] not in state['game'] and [7,24] not in state['game'] and [8,24] not in state['game']:#fim quadrado 5 camada
                keys = ["d", "d", "d", "d"]
            
                ### 5 camada-----------

            elif [1,24] not in state['game'] and [2,24] not in state['game'] and [1,23] not in state['game'] and [2,23] not in state['game']:
                keys = ["a", "a", "a", "a"]
            elif [2,24] not in state['game'] and [3,24] not in state['game'] and [2,23] not in state['game'] and [3,23] not in state['game']:
                keys = ["a"]
            elif [3,24] not in state['game'] and [4,24] not in state['game'] and [3,23] not in state['game'] and [4,23] not in state['game']:
                keys = []
            elif [4,24] not in state['game'] and [5,24] not in state['game'] and [4,23] not in state['game'] and [5,23] not in state['game']:
                keys = ["d"]
            elif [5,24] not in state['game'] and [6,24] not in state['game'] and [5,23] not in state['game'] and [6,23] not in state['game']:
                keys = ["d", "d"]
            elif [6,24] not in state['game'] and [7,24] not in state['game'] and [6,23] not in state['game'] and [7,23] not in state['game']:
                keys = ["d", "d", "d"]
            elif [7,24] not in state['game'] and [8,24] not in state['game'] and [7,23] not in state['game'] and [8,23] not in state['game']:#fim quadrado 6 camada
                keys = ["d", "d", "d", "d"]

            ### 6 camada-----------

            elif [1,23] not in state['game'] and [2,23] not in state['game'] and [1,22] not in state['game'] and [2,22] not in state['game']:
                keys = ["a", "a", "a", "a"]
            elif [2,23] not in state['game'] and [3,23] not in state['game'] and [2,22] not in state['game'] and [3,22] not in state['game']:
                keys = ["a"]
            elif [3,23] not in state['game'] and [4,23] not in state['game'] and [3,22] not in state['game'] and [4,22] not in state['game']:
                keys = []
            elif [4,23] not in state['game'] and [5,23] not in state['game'] and [4,22] not in state['game'] and [5,22] not in state['game']:
                keys = ["d"]
            elif [5,23] not in state['game'] and [6,23] not in state['game'] and [5,22] not in state['game'] and [6,22] not in state['game']:
                keys = ["d", "d"]
            elif [6,23] not in state['game'] and [7,23] not in state['game'] and [6,22] not in state['game'] and [7,22] not in state['game']:
                keys = ["d", "d", "d"]
            elif [7,23] not in state['game'] and [8,23] not in state['game'] and [7,22] not in state['game'] and [8,22] not in state['game']:#fim quadrado 6 camada
                keys = ["d", "d", "d", "d"]

            ### 7 camada-----------

            elif [1,22] not in state['game'] and [2,22] not in state['game'] and [1,21] not in state['game'] and [2,21] not in state['game']:
                keys = ["a", "a", "a", "a"]
            elif [2,22] not in state['game'] and [3,22] not in state['game'] and [2,21] not in state['game'] and [3,21] not in state['game']:
                keys = ["a"]
            elif [3,22] not in state['game'] and [4,22] not in state['game'] and [3,21] not in state['game'] and [4,21] not in state['game']:
                keys = []
            elif [4,22] not in state['game'] and [5,22] not in state['game'] and [4,21] not in state['game'] and [5,21] not in state['game']:
                keys = ["d"]
            elif [5,22] not in state['game'] and [6,22] not in state['game'] and [5,21] not in state['game'] and [6,21] not in state['game']:
                keys = ["d", "d"]
            elif [6,22] not in state['game'] and [7,22] not in state['game'] and [6,21] not in state['game'] and [7,21] not in state['game']:
                keys = ["d", "d", "d"]
            elif [7,22] not in state['game'] and [8,22] not in state['game'] and [7,21] not in state['game'] and [8,21] not in state['game']:#fim quadrado 6 camada
                keys = ["d", "d", "d", "d"]
            else:
                keys = []
    elif peca(state) == "L":
        if state['game'] == []:
            keys = ["w", "w", "w", "a", "a"]
        else:
            if [1,29] not in state['game'] and [2,29] not in state['game'] and [3,29] not in state['game'] and [3,28] not in state['game']:
                keys = ["w","w","w", "a", "a"]
            elif [2,29] not in state['game'] and [3,29] not in state['game'] and [4,29] not in state['game'] and [4,28] not in state['game']:
                keys = ["w","w","w", "a"]
            elif [3,29] not in state['game'] and [4,29] not in state['game'] and [5,29] not in state['game'] and [5,28] not in state['game']:
                keys = ["w","w","w"]
            elif [4,29] not in state['game'] and [5,29] not in state['game'] and [6,29] not in state['game'] and [6,28] not in state['game']:
                keys = ["w","w","w", "d"]
            elif [5,29] not in state['game'] and [6,29] not in state['game'] and [7,29] not in state['game'] and [7,28] not in state['game']:
                keys = ["w","w","w", "d", "d"]
            elif [6,29] not in state['game'] and [7,29] not in state['game'] and [8,29] not in state['game'] and [8,28] not in state['game']: #fim L rodado 3 vezes
                keys = ["w","w","w", "d", "d", "d"]
            elif [1,29] not in state['game'] and [1,28] not in state['game'] and [1,27] not in state['game'] and [2,29] not in state['game'] and [2,28] not in state['game'] and [2,27] not in state['game']:
                keys = ["a", "a", "a"]
            elif [2,29] not in state['game'] and [2,28] not in state['game'] and [2,27] not in state['game'] and [3,29] not in state['game'] and [3,28] not in state['game'] and [3,27] not in state['game']:
                keys = ["a", "a"]
            elif [3,29] not in state['game'] and [3,28] not in state['game'] and [3,27] not in state['game'] and [4,29] not in state['game'] and [4,28] not in state['game'] and [4,27] not in state['game']:
                keys = ["a"]
            elif [4,29] not in state['game'] and [4,28] not in state['game'] and [4,27] not in state['game'] and [5,29] not in state['game'] and [5,28] not in state['game'] and [5,27] not in state['game']:
                keys = []
            elif [5,29] not in state['game'] and [5,28] not in state['game'] and [5,27] not in state['game'] and [6,29] not in state['game'] and [6,28] not in state['game'] and [6,27] not in state['game']:
                keys = ["d"]
            elif [6,29] not in state['game'] and [6,28] not in state['game'] and [6,27] not in state['game'] and [7,29] not in state['game'] and [7,28] not in state['game'] and [7,27] not in state['game']:
                keys = ["d","d"]
            elif [7,29] not in state['game'] and [7,28] not in state['game'] and [7,27] not in state['game'] and [8,29] not in state['game'] and [8,28] not in state['game'] and [8,27] not in state['game']: #fim L normal
                keys = ["d","d","d"]
            elif [8,28] not in state['game'] and [7,28] not in state['game'] and [6,28] not in state['game'] and [6,29] not in state['game']: 
                keys = ["w","d","d","d"]
            elif [7,28] not in state['game'] and [6,28] not in state['game'] and [5,28] not in state['game'] and [5,29] not in state['game']: 
                keys = ["w","d","d"]
            elif [6,28] not in state['game'] and [5,28] not in state['game'] and [4,28] not in state['game'] and [4,29] not in state['game']: 
                keys = ["w","d"]
            elif [5,28] not in state['game'] and [4,28] not in state['game'] and [3,28] not in state['game'] and [3,29] not in state['game']: 
                keys = ["w"]
            elif [4,28] not in state['game'] and [3,28] not in state['game'] and [2,28] not in state['game'] and [2,29] not in state['game']: 
                keys = ["w", "a"]
            elif [3,28] not in state['game'] and [2,28] not in state['game'] and [1,28] not in state['game'] and [1,29] not in state['game']: #fim L rodado 1 vez
                keys = ["w", "a", "a"]
            elif [2,29] not in state['game'] and [2,28] not in state['game'] and [2,27] not in state['game'] and [1,27] not in state['game']: 
                keys = ["w", "w", "a", "a"]
            elif [3,29] not in state['game'] and [3,28] not in state['game'] and [3,27] not in state['game'] and [2,27] not in state['game']: 
                keys = ["w", "w", "a"]
            elif [4,29] not in state['game'] and [4,28] not in state['game'] and [4,27] not in state['game'] and [3,27] not in state['game']: 
                keys = ["w", "w"]
            elif [5,29] not in state['game'] and [5,28] not in state['game'] and [5,27] not in state['game'] and [4,27] not in state['game']: 
                keys = ["w", "w", "d"]
            elif [6,29] not in state['game'] and [6,28] not in state['game'] and [6,27] not in state['game'] and [5,27] not in state['game']: 
                keys = ["w", "w", "d", "d"]
            elif [7,29] not in state['game'] and [7,28] not in state['game'] and [7,27] not in state['game'] and [6,27] not in state['game']: 
                keys = ["w", "w", "d", "d", "d"]
            elif [8,29] not in state['game'] and [8,28] not in state['game'] and [8,27] not in state['game'] and [7,27] not in state['game']: #fim L rodado 2 vezes - 1 camada
                keys = ["w", "w", "d", "d", "d", "d"]

                   #1 camada---------------------------

            elif [1,28] not in state['game'] and [2,28] not in state['game'] and [3,28] not in state['game'] and [3,27] not in state['game']:
                keys = ["w","w","w", "a", "a"]
            elif [2,28] not in state['game'] and [3,28] not in state['game'] and [4,28] not in state['game'] and [4,27] not in state['game']:
                keys = ["w","w","w", "a"]
            elif [3,28] not in state['game'] and [4,28] not in state['game'] and [5,28] not in state['game'] and [5,27] not in state['game']:
                keys = ["w","w","w"]
            elif [4,28] not in state['game'] and [5,28] not in state['game'] and [6,28] not in state['game'] and [6,27] not in state['game']:
                keys = ["w","w","w", "d"]
            elif [5,28] not in state['game'] and [6,28] not in state['game'] and [7,28] not in state['game'] and [7,27] not in state['game']:
                keys = ["w","w","w", "d", "d"]
            elif [6,28] not in state['game'] and [7,28] not in state['game'] and [8,28] not in state['game'] and [8,27] not in state['game']: #fim L rodado 3 vezes
                keys = ["w","w","w", "d", "d", "d"]
            elif [1,28] not in state['game'] and [1,27] not in state['game'] and [1,26] not in state['game'] and [2,28] not in state['game'] and [2,27] not in state['game'] and [2,26] not in state['game']:
                keys = ["a", "a", "a"]
            elif [2,28] not in state['game'] and [2,27] not in state['game'] and [2,26] not in state['game'] and [3,28] not in state['game'] and [3,27] not in state['game'] and [3,26] not in state['game']:
                keys = ["a", "a"]
            elif [3,28] not in state['game'] and [3,27] not in state['game'] and [3,26] not in state['game'] and [4,28] not in state['game'] and [4,27] not in state['game'] and [4,26] not in state['game']:
                keys = ["a"]
            elif [4,28] not in state['game'] and [4,27] not in state['game'] and [4,26] not in state['game'] and [5,28] not in state['game'] and [5,27] not in state['game'] and [5,26] not in state['game']:
                keys = []
            elif [5,28] not in state['game'] and [5,27] not in state['game'] and [5,26] not in state['game'] and [6,28] not in state['game'] and [6,27] not in state['game'] and [6,26] not in state['game']:
                keys = ["d"]
            elif [6,28] not in state['game'] and [6,27] not in state['game'] and [6,26] not in state['game'] and [7,28] not in state['game'] and [7,27] not in state['game'] and [7,26] not in state['game']:
                keys = ["d","d"]
            elif [7,28] not in state['game'] and [7,27] not in state['game'] and [7,26] not in state['game'] and [8,28] not in state['game'] and [8,27] not in state['game'] and [8,26] not in state['game']: #fim L normal
                keys = ["d","d","d"]
            elif [8,27] not in state['game'] and [7,27] not in state['game'] and [6,27] not in state['game'] and [6,28] not in state['game']: 
                keys = ["w","d","d","d"]
            elif [7,27] not in state['game'] and [6,27] not in state['game'] and [5,27] not in state['game'] and [5,28] not in state['game']: 
                keys = ["w","d","d"]
            elif [6,27] not in state['game'] and [5,27] not in state['game'] and [4,27] not in state['game'] and [4,28] not in state['game']: 
                keys = ["w","d"]
            elif [5,27] not in state['game'] and [4,27] not in state['game'] and [3,27] not in state['game'] and [3,28] not in state['game']: 
                keys = ["w"]
            elif [4,27] not in state['game'] and [3,27] not in state['game'] and [2,27] not in state['game'] and [2,28] not in state['game']: 
                keys = ["w", "a"]
            elif [3,27] not in state['game'] and [2,27] not in state['game'] and [1,27] not in state['game'] and [1,28] not in state['game']: #fim L rodado 1 vez
                keys = ["w", "a", "a"]
            elif [2,28] not in state['game'] and [2,27] not in state['game'] and [2,26] not in state['game'] and [1,26] not in state['game']: 
                keys = ["w", "w", "a", "a"]
            elif [3,28] not in state['game'] and [3,27] not in state['game'] and [3,26] not in state['game'] and [2,26] not in state['game']: 
                keys = ["w", "w", "a"]
            elif [4,28] not in state['game'] and [4,27] not in state['game'] and [4,26] not in state['game'] and [3,26] not in state['game']: 
                keys = ["w", "w"]
            elif [5,28] not in state['game'] and [5,27] not in state['game'] and [5,26] not in state['game'] and [4,26] not in state['game']: 
                keys = ["w", "w", "d"]
            elif [6,28] not in state['game'] and [6,27] not in state['game'] and [6,26] not in state['game'] and [5,26] not in state['game']: 
                keys = ["w", "w", "d", "d"]
            elif [7,28] not in state['game'] and [7,27] not in state['game'] and [7,26] not in state['game'] and [6,26] not in state['game']: 
                keys = ["w", "w", "d", "d", "d"]
            elif [8,28] not in state['game'] and [8,27] not in state['game'] and [8,26] not in state['game'] and [7,26] not in state['game']: #fim L rodado 2 vezes - 1 camada
                keys = ["w", "w", "d", "d", "d", "d"]

                       #  2camada---------------------------

            elif [1,27] not in state['game'] and [2,27] not in state['game'] and [3,27] not in state['game'] and [3,26] not in state['game']:
                keys = ["w","w","w", "a", "a"]
            elif [2,27] not in state['game'] and [3,27] not in state['game'] and [4,27] not in state['game'] and [4,26] not in state['game']:
                keys = ["w","w","w", "a"]
            elif [3,27] not in state['game'] and [4,27] not in state['game'] and [5,27] not in state['game'] and [5,26] not in state['game']:
                keys = ["w","w","w"]
            elif [4,27] not in state['game'] and [5,27] not in state['game'] and [6,27] not in state['game'] and [6,26] not in state['game']:
                keys = ["w","w","w", "d"]
            elif [5,27] not in state['game'] and [6,27] not in state['game'] and [7,27] not in state['game'] and [7,26] not in state['game']:
                keys = ["w","w","w", "d", "d"]
            elif [6,27] not in state['game'] and [7,27] not in state['game'] and [8,27] not in state['game'] and [8,26] not in state['game']: #fim L rodado 3 vezes
                keys = ["w","w","w", "d", "d", "d"]
            elif [1,27] not in state['game'] and [1,26] not in state['game'] and [1,27] not in state['game'] and [2,27] not in state['game'] and [2,26] not in state['game'] and [2,25] not in state['game']:
                keys = ["a", "a", "a"]
            elif [2,27] not in state['game'] and [2,26] not in state['game'] and [2,27] not in state['game'] and [3,27] not in state['game'] and [3,26] not in state['game'] and [3,25] not in state['game']:
                keys = ["a", "a"]
            elif [3,27] not in state['game'] and [3,26] not in state['game'] and [3,27] not in state['game'] and [4,27] not in state['game'] and [4,26] not in state['game'] and [4,25] not in state['game']:
                keys = ["a"]
            elif [4,27] not in state['game'] and [4,26] not in state['game'] and [4,27] not in state['game'] and [5,27] not in state['game'] and [5,26] not in state['game'] and [5,25] not in state['game']:
                keys = []
            elif [5,27] not in state['game'] and [5,26] not in state['game'] and [5,27] not in state['game'] and [6,27] not in state['game'] and [6,26] not in state['game'] and [6,25] not in state['game']:
                keys = ["d"]
            elif [6,27] not in state['game'] and [6,26] not in state['game'] and [6,27] not in state['game'] and [7,27] not in state['game'] and [7,26] not in state['game'] and [7,25] not in state['game']:
                keys = ["d","d"]
            elif [7,27] not in state['game'] and [7,26] not in state['game'] and [7,27] not in state['game'] and [8,27] not in state['game'] and [8,26] not in state['game'] and [8,25] not in state['game']: 
                keys = ["d","d","d"]                                                                                                          #fim L normal
            elif [8,26] not in state['game'] and [7,26] not in state['game'] and [6,26] not in state['game'] and [6,27] not in state['game']: 
                keys = ["w","d","d","d"]
            elif [7,26] not in state['game'] and [6,26] not in state['game'] and [5,26] not in state['game'] and [5,27] not in state['game']: 
                keys = ["w","d","d"]
            elif [6,26] not in state['game'] and [5,26] not in state['game'] and [4,26] not in state['game'] and [4,27] not in state['game']: 
                keys = ["w","d"]
            elif [5,26] not in state['game'] and [4,26] not in state['game'] and [3,26] not in state['game'] and [3,27] not in state['game']: 
                keys = ["w"]
            elif [4,26] not in state['game'] and [3,26] not in state['game'] and [2,26] not in state['game'] and [2,27] not in state['game']: 
                keys = ["w", "a"]
            elif [3,26] not in state['game'] and [2,26] not in state['game'] and [1,26] not in state['game'] and [1,27] not in state['game']: #fim L rodado 1 vez
                keys = ["w", "a", "a"]
            elif [2,27] not in state['game'] and [2,26] not in state['game'] and [2,25] not in state['game'] and [1,25] not in state['game']: 
                keys = ["w", "w", "a", "a"]
            elif [3,27] not in state['game'] and [3,26] not in state['game'] and [3,25] not in state['game'] and [2,25] not in state['game']: 
                keys = ["w", "w", "a"]
            elif [4,27] not in state['game'] and [4,26] not in state['game'] and [4,25] not in state['game'] and [3,25] not in state['game']: 
                keys = ["w", "w"]
            elif [5,27] not in state['game'] and [5,26] not in state['game'] and [5,25] not in state['game'] and [4,25] not in state['game']: 
                keys = ["w", "w", "d"]
            elif [6,27] not in state['game'] and [6,26] not in state['game'] and [6,25] not in state['game'] and [5,25] not in state['game']: 
                keys = ["w", "w", "d", "d"]
            elif [7,27] not in state['game'] and [7,26] not in state['game'] and [7,25] not in state['game'] and [6,25] not in state['game']: 
                keys = ["w", "w", "d", "d", "d"]
            elif [8,27] not in state['game'] and [8,26] not in state['game'] and [8,25] not in state['game'] and [7,25] not in state['game']: #fim L rodado 2 vezes - 2 camada
                keys = ["w", "w", "d", "d", "d", "d"]

            #  3camada---------------------------

            elif [1,26] not in state['game'] and [2,26] not in state['game'] and [3,26] not in state['game'] and [3,25] not in state['game']:
                keys = ["w","w","w", "a", "a"]
            elif [2,26] not in state['game'] and [3,26] not in state['game'] and [4,26] not in state['game'] and [4,25] not in state['game']:
                keys = ["w","w","w", "a"]
            elif [3,26] not in state['game'] and [4,26] not in state['game'] and [5,26] not in state['game'] and [5,25] not in state['game']:
                keys = ["w","w","w"]
            elif [4,26] not in state['game'] and [5,26] not in state['game'] and [6,26] not in state['game'] and [6,25] not in state['game']:
                keys = ["w","w","w", "d"]
            elif [5,26] not in state['game'] and [6,26] not in state['game'] and [7,26] not in state['game'] and [7,25] not in state['game']:
                keys = ["w","w","w", "d", "d"]
            elif [6,26] not in state['game'] and [7,26] not in state['game'] and [8,26] not in state['game'] and [8,25] not in state['game']: #fim L rodado 3 vezes
                keys = ["w","w","w", "d", "d", "d"]
            elif [1,26] not in state['game'] and [1,25] not in state['game'] and [1,26] not in state['game'] and [2,26] not in state['game'] and [2,25] not in state['game'] and [2,24] not in state['game']:
                keys = ["a", "a", "a"]
            elif [2,26] not in state['game'] and [2,25] not in state['game'] and [2,26] not in state['game'] and [3,26] not in state['game'] and [3,25] not in state['game'] and [3,24] not in state['game']:
                keys = ["a", "a"]
            elif [3,26] not in state['game'] and [3,25] not in state['game'] and [3,26] not in state['game'] and [4,26] not in state['game'] and [4,25] not in state['game'] and [4,24] not in state['game']:
                keys = ["a"]
            elif [4,26] not in state['game'] and [4,25] not in state['game'] and [4,26] not in state['game'] and [5,26] not in state['game'] and [5,25] not in state['game'] and [5,24] not in state['game']:
                keys = [""]
            elif [5,26] not in state['game'] and [5,25] not in state['game'] and [5,26] not in state['game'] and [6,26] not in state['game'] and [6,25] not in state['game'] and [6,24] not in state['game']:
                keys = ["d"]
            elif [6,26] not in state['game'] and [6,25] not in state['game'] and [6,26] not in state['game'] and [7,26] not in state['game'] and [7,25] not in state['game'] and [7,24] not in state['game']:
                keys = ["d","d"]
            elif [7,26] not in state['game'] and [7,25] not in state['game'] and [7,26] not in state['game'] and [8,26] not in state['game'] and [8,25] not in state['game'] and [8,24] not in state['game']: #fim L normal
                keys = ["d","d","d"]
            elif [8,25] not in state['game'] and [7,25] not in state['game'] and [6,25] not in state['game'] and [6,26] not in state['game']: 
                keys = ["w","d","d","d"]
            elif [7,25] not in state['game'] and [6,25] not in state['game'] and [5,25] not in state['game'] and [5,26] not in state['game']: 
                keys = ["w","d","d"]
            elif [6,25] not in state['game'] and [5,25] not in state['game'] and [4,25] not in state['game'] and [4,26] not in state['game']: 
                keys = ["w","d"]
            elif [5,25] not in state['game'] and [4,25] not in state['game'] and [3,25] not in state['game'] and [3,26] not in state['game']: 
                keys = ["w"]
            elif [4,25] not in state['game'] and [3,25] not in state['game'] and [2,25] not in state['game'] and [2,26] not in state['game']: 
                keys = ["w", "a"]
            elif [3,25] not in state['game'] and [2,25] not in state['game'] and [1,25] not in state['game'] and [1,26] not in state['game']: #fim L rodado 1 vez
                keys = ["w", "a", "a"]
            elif [2,26] not in state['game'] and [2,25] not in state['game'] and [2,24] not in state['game'] and [1,24] not in state['game']: 
                keys = ["w", "w", "a", "a"]
            elif [3,26] not in state['game'] and [3,25] not in state['game'] and [3,24] not in state['game'] and [2,24] not in state['game']: 
                keys = ["w", "w", "a"]
            elif [4,26] not in state['game'] and [4,25] not in state['game'] and [4,24] not in state['game'] and [3,24] not in state['game']: 
                keys = ["w", "w"]
            elif [5,26] not in state['game'] and [5,25] not in state['game'] and [5,24] not in state['game'] and [4,24] not in state['game']: 
                keys = ["w", "w", "d"]
            elif [6,26] not in state['game'] and [6,25] not in state['game'] and [6,24] not in state['game'] and [5,24] not in state['game']: 
                keys = ["w", "w", "d", "d"]
            elif [7,26] not in state['game'] and [7,25] not in state['game'] and [7,24] not in state['game'] and [6,24] not in state['game']: 
                keys = ["w", "w", "d", "d", "d"]
            elif [8,26] not in state['game'] and [8,25] not in state['game'] and [8,24] not in state['game'] and [7,24] not in state['game']: #fim L rodado 2 vezes - 3 camada
                keys = ["w", "w", "d", "d", "d", "d"]

            #  4camada---------------------------

            elif [1,25] not in state['game'] and [2,25] not in state['game'] and [3,25] not in state['game'] and [3,24] not in state['game']:
                keys = ["w","w","w", "a", "a"]
            elif [2,25] not in state['game'] and [3,25] not in state['game'] and [4,25] not in state['game'] and [4,24] not in state['game']:
                keys = ["w","w","w", "a"]
            elif [3,25] not in state['game'] and [4,25] not in state['game'] and [5,25] not in state['game'] and [5,24] not in state['game']:
                keys = ["w","w","w"]
            elif [4,25] not in state['game'] and [5,25] not in state['game'] and [6,25] not in state['game'] and [6,24] not in state['game']:
                keys = ["w","w","w", "d"]
            elif [5,25] not in state['game'] and [6,25] not in state['game'] and [7,25] not in state['game'] and [7,24] not in state['game']:
                keys = ["w","w","w", "d", "d"]
            elif [6,25] not in state['game'] and [7,25] not in state['game'] and [8,25] not in state['game'] and [8,24] not in state['game']: #fim L rodado 3 vezes
                keys = ["w","w","w", "d", "d", "d"]
            elif [1,25] not in state['game'] and [1,24] not in state['game'] and [1,25] not in state['game'] and [2,25] not in state['game'] and [2,24] not in state['game'] and [2,23] not in state['game']:
                keys = ["a", "a", "a"]
            elif [2,25] not in state['game'] and [2,24] not in state['game'] and [2,25] not in state['game'] and [3,25] not in state['game'] and [3,24] not in state['game'] and [3,23] not in state['game']:
                keys = ["a", "a"]
            elif [3,25] not in state['game'] and [3,24] not in state['game'] and [3,25] not in state['game'] and [4,25] not in state['game'] and [4,24] not in state['game'] and [4,23] not in state['game']:
                keys = ["a"]
            elif [4,25] not in state['game'] and [4,24] not in state['game'] and [4,25] not in state['game'] and [5,25] not in state['game'] and [5,24] not in state['game'] and [5,23] not in state['game']:
                keys = [""]
            elif [5,25] not in state['game'] and [5,24] not in state['game'] and [5,25] not in state['game'] and [6,25] not in state['game'] and [6,24] not in state['game'] and [6,23] not in state['game']:
                keys = ["d"]
            elif [6,25] not in state['game'] and [6,24] not in state['game'] and [6,25] not in state['game'] and [7,25] not in state['game'] and [7,24] not in state['game'] and [7,23] not in state['game']:
                keys = ["d","d"]
            elif [7,25] not in state['game'] and [7,24] not in state['game'] and [7,25] not in state['game'] and [8,25] not in state['game'] and [8,24] not in state['game'] and [8,23] not in state['game']: #fim L normal
                keys = ["d","d","d"]
            elif [8,24] not in state['game'] and [7,24] not in state['game'] and [6,24] not in state['game'] and [6,25] not in state['game']: 
                keys = ["w","d","d","d"]
            elif [7,24] not in state['game'] and [6,24] not in state['game'] and [5,24] not in state['game'] and [5,25] not in state['game']: 
                keys = ["w","d","d"]
            elif [6,24] not in state['game'] and [5,24] not in state['game'] and [4,24] not in state['game'] and [4,25] not in state['game']: 
                keys = ["w","d"]
            elif [5,24] not in state['game'] and [4,24] not in state['game'] and [3,24] not in state['game'] and [3,25] not in state['game']: 
                keys = ["w"]
            elif [4,24] not in state['game'] and [3,24] not in state['game'] and [2,24] not in state['game'] and [2,25] not in state['game']: 
                keys = ["w", "a"]
            elif [3,24] not in state['game'] and [2,24] not in state['game'] and [1,24] not in state['game'] and [1,25] not in state['game']: #fim L rodado 1 vez
                keys = ["w", "a", "a"]
            elif [2,25] not in state['game'] and [2,24] not in state['game'] and [2,23] not in state['game'] and [1,23] not in state['game']: 
                keys = ["w", "w", "a", "a"]
            elif [3,25] not in state['game'] and [3,24] not in state['game'] and [3,23] not in state['game'] and [2,23] not in state['game']: 
                keys = ["w", "w", "a"]
            elif [4,25] not in state['game'] and [4,24] not in state['game'] and [4,23] not in state['game'] and [3,23] not in state['game']: 
                keys = ["w", "w"]
            elif [5,25] not in state['game'] and [5,24] not in state['game'] and [5,23] not in state['game'] and [4,23] not in state['game']: 
                keys = ["w", "w", "d"]
            elif [6,25] not in state['game'] and [6,24] not in state['game'] and [6,23] not in state['game'] and [5,23] not in state['game']: 
                keys = ["w", "w", "d", "d"]
            elif [7,25] not in state['game'] and [7,24] not in state['game'] and [7,23] not in state['game'] and [6,23] not in state['game']: 
                keys = ["w", "w", "d", "d", "d"]
            elif [8,25] not in state['game'] and [8,24] not in state['game'] and [8,23] not in state['game'] and [7,23] not in state['game']: #fim L rodado 2 vezes - 4 camada
                keys = ["w", "w", "d", "d", "d", "d"]

            #  5camada---------------------------

            elif [1,24] not in state['game'] and [2,24] not in state['game'] and [3,24] not in state['game'] and [3,23] not in state['game']:
                keys = ["w","w","w", "a", "a"]
            elif [2,24] not in state['game'] and [3,24] not in state['game'] and [4,24] not in state['game'] and [4,23] not in state['game']:
                keys = ["w","w","w", "a"]
            elif [3,24] not in state['game'] and [4,24] not in state['game'] and [5,24] not in state['game'] and [5,23] not in state['game']:
                keys = ["w","w","w"]
            elif [4,24] not in state['game'] and [5,24] not in state['game'] and [6,24] not in state['game'] and [6,23] not in state['game']:
                keys = ["w","w","w", "d"]
            elif [5,24] not in state['game'] and [6,24] not in state['game'] and [7,24] not in state['game'] and [7,23] not in state['game']:
                keys = ["w","w","w", "d", "d"]
            elif [6,24] not in state['game'] and [7,24] not in state['game'] and [8,24] not in state['game'] and [8,23] not in state['game']: #fim L rodado 3 vezes
                keys = ["w","w","w", "d", "d", "d"]
            elif [1,24] not in state['game'] and [1,23] not in state['game'] and [1,24] not in state['game'] and [2,24] not in state['game'] and [2,23] not in state['game'] and [2,22] not in state['game']:
                keys = ["a", "a", "a"]
            elif [2,24] not in state['game'] and [2,23] not in state['game'] and [2,24] not in state['game'] and [3,24] not in state['game'] and [3,23] not in state['game'] and [3,22] not in state['game']:
                keys = ["a", "a"]
            elif [3,24] not in state['game'] and [3,23] not in state['game'] and [3,24] not in state['game'] and [4,24] not in state['game'] and [4,23] not in state['game'] and [4,22] not in state['game']:
                keys = ["a"]
            elif [4,24] not in state['game'] and [4,23] not in state['game'] and [4,24] not in state['game'] and [5,24] not in state['game'] and [5,23] not in state['game'] and [5,22] not in state['game']:
                keys = [""]
            elif [5,24] not in state['game'] and [5,23] not in state['game'] and [5,24] not in state['game'] and [6,24] not in state['game'] and [6,23] not in state['game'] and [6,22] not in state['game']:
                keys = ["d"]
            elif [6,24] not in state['game'] and [6,23] not in state['game'] and [6,24] not in state['game'] and [7,24] not in state['game'] and [7,23] not in state['game'] and [7,22] not in state['game']:
                keys = ["d","d"]
            elif [7,24] not in state['game'] and [7,23] not in state['game'] and [7,24] not in state['game'] and [8,24] not in state['game'] and [8,23] not in state['game'] and [8,22] not in state['game']: #fim L normal
                keys = ["d","d","d"]
            elif [8,23] not in state['game'] and [7,23] not in state['game'] and [6,23] not in state['game'] and [6,24] not in state['game']: 
                keys = ["w","d","d","d"]
            elif [7,23] not in state['game'] and [6,23] not in state['game'] and [5,23] not in state['game'] and [5,24] not in state['game']: 
                keys = ["w","d","d"]
            elif [6,23] not in state['game'] and [5,23] not in state['game'] and [4,23] not in state['game'] and [4,24] not in state['game']: 
                keys = ["w","d"]
            elif [5,23] not in state['game'] and [4,23] not in state['game'] and [3,23] not in state['game'] and [3,24] not in state['game']: 
                keys = ["w"]
            elif [4,23] not in state['game'] and [3,23] not in state['game'] and [2,23] not in state['game'] and [2,24] not in state['game']: 
                keys = ["w", "a"]
            elif [3,23] not in state['game'] and [2,23] not in state['game'] and [1,23] not in state['game'] and [1,24] not in state['game']: #fim L rodado 1 vez
                keys = ["w", "a", "a"]
            elif [2,24] not in state['game'] and [2,23] not in state['game'] and [2,22] not in state['game'] and [1,22] not in state['game']: 
                keys = ["w", "w", "a", "a"]
            elif [3,24] not in state['game'] and [3,23] not in state['game'] and [3,22] not in state['game'] and [2,22] not in state['game']: 
                keys = ["w", "w", "a"]
            elif [4,24] not in state['game'] and [4,23] not in state['game'] and [4,22] not in state['game'] and [3,22] not in state['game']: 
                keys = ["w", "w"]
            elif [5,24] not in state['game'] and [5,23] not in state['game'] and [5,22] not in state['game'] and [4,22] not in state['game']: 
                keys = ["w", "w", "d"]
            elif [6,24] not in state['game'] and [6,23] not in state['game'] and [6,22] not in state['game'] and [5,22] not in state['game']: 
                keys = ["w", "w", "d", "d"]
            elif [7,24] not in state['game'] and [7,23] not in state['game'] and [7,22] not in state['game'] and [6,22] not in state['game']: 
                keys = ["w", "w", "d", "d", "d"]
            elif [8,24] not in state['game'] and [8,23] not in state['game'] and [8,22] not in state['game'] and [7,22] not in state['game']: #fim L rodado 2 vezes - 4 camada
                keys = ["w", "w", "d", "d", "d", "d"]
            
            #  6camada---------------------------

            elif [1,23] not in state['game'] and [2,23] not in state['game'] and [3,23] not in state['game'] and [3,22] not in state['game']:
                keys = ["w","w","w", "a", "a"]
            elif [2,23] not in state['game'] and [3,23] not in state['game'] and [4,23] not in state['game'] and [4,22] not in state['game']:
                keys = ["w","w","w", "a"]
            elif [3,23] not in state['game'] and [4,23] not in state['game'] and [5,23] not in state['game'] and [5,22] not in state['game']:
                keys = ["w","w","w"]
            elif [4,23] not in state['game'] and [5,23] not in state['game'] and [6,23] not in state['game'] and [6,22] not in state['game']:
                keys = ["w","w","w", "d"]
            elif [5,23] not in state['game'] and [6,23] not in state['game'] and [7,23] not in state['game'] and [7,22] not in state['game']:
                keys = ["w","w","w", "d", "d"]
            elif [6,23] not in state['game'] and [7,23] not in state['game'] and [8,23] not in state['game'] and [8,22] not in state['game']: #fim L rodado 3 vezes
                keys = ["w","w","w", "d", "d", "d"]
            elif [1,23] not in state['game'] and [1,22] not in state['game'] and [1,23] not in state['game'] and [2,22] not in state['game'] and [2,22] not in state['game'] and [2,21] not in state['game']:
                keys = ["a", "a", "a"]
            elif [2,23] not in state['game'] and [2,22] not in state['game'] and [2,23] not in state['game'] and [3,22] not in state['game'] and [3,22] not in state['game'] and [3,21] not in state['game']:
                keys = ["a", "a"]
            elif [3,23] not in state['game'] and [3,22] not in state['game'] and [3,23] not in state['game'] and [4,22] not in state['game'] and [4,22] not in state['game'] and [4,21] not in state['game']:
                keys = ["a"]
            elif [4,23] not in state['game'] and [4,22] not in state['game'] and [4,23] not in state['game'] and [5,22] not in state['game'] and [5,22] not in state['game'] and [5,21] not in state['game']:
                keys = [""]
            elif [5,23] not in state['game'] and [5,22] not in state['game'] and [5,23] not in state['game'] and [6,22] not in state['game'] and [6,22] not in state['game'] and [6,21] not in state['game']:
                keys = ["d"]
            elif [6,23] not in state['game'] and [6,22] not in state['game'] and [6,23] not in state['game'] and [7,23] not in state['game'] and [7,22] not in state['game'] and [7,21] not in state['game']:
                keys = ["d","d"]
            elif [7,23] not in state['game'] and [7,22] not in state['game'] and [7,23] not in state['game'] and [8,23] not in state['game'] and [8,22] not in state['game'] and [8,21] not in state['game']: #fim L normal
                keys = ["d","d","d"]
            elif [8,22] not in state['game'] and [7,22] not in state['game'] and [6,22] not in state['game'] and [6,23] not in state['game']: 
                keys = ["w","d","d","d"]
            elif [7,22] not in state['game'] and [6,22] not in state['game'] and [5,22] not in state['game'] and [5,23] not in state['game']: 
                keys = ["w","d","d"]
            elif [6,22] not in state['game'] and [5,22] not in state['game'] and [4,22] not in state['game'] and [4,23] not in state['game']: 
                keys = ["w","d"]
            elif [5,22] not in state['game'] and [4,22] not in state['game'] and [3,22] not in state['game'] and [3,23] not in state['game']: 
                keys = ["w"]
            elif [4,22] not in state['game'] and [3,22] not in state['game'] and [2,22] not in state['game'] and [2,23] not in state['game']: 
                keys = ["w", "a"]
            elif [3,22] not in state['game'] and [2,22] not in state['game'] and [1,22] not in state['game'] and [1,23] not in state['game']: #fim L rodado 1 vez
                keys = ["w", "a", "a"]
            elif [2,23] not in state['game'] and [2,22] not in state['game'] and [2,21] not in state['game'] and [1,21] not in state['game']: 
                keys = ["w", "w", "a", "a"]
            elif [3,23] not in state['game'] and [3,22] not in state['game'] and [3,21] not in state['game'] and [2,21] not in state['game']: 
                keys = ["w", "w", "a"]
            elif [4,23] not in state['game'] and [4,22] not in state['game'] and [4,21] not in state['game'] and [3,21] not in state['game']: 
                keys = ["w", "w"]
            elif [5,23] not in state['game'] and [5,22] not in state['game'] and [5,21] not in state['game'] and [4,21] not in state['game']: 
                keys = ["w", "w", "d"]
            elif [6,23] not in state['game'] and [6,22] not in state['game'] and [6,21] not in state['game'] and [5,21] not in state['game']: 
                keys = ["w", "w", "d", "d"]
            elif [7,23] not in state['game'] and [7,22] not in state['game'] and [7,21] not in state['game'] and [6,21] not in state['game']: 
                keys = ["w", "w", "d", "d", "d"]
            elif [8,23] not in state['game'] and [8,22] not in state['game'] and [8,21] not in state['game'] and [7,21] not in state['game']: #fim L rodado 2 vezes - 4 camada
                keys = ["w", "w", "d", "d", "d", "d"]
            else:
                keys = []

    elif peca(state) == "J":
        if state['game'] == []:
            keys = ["w", "w", "w" "d", "d", "d", "d"]
        else:
            if [1,29] not in state['game'] and [1,28] not in state['game'] and [2,29] not in state['game'] and [3,29] not in state['game']: 
                keys = ["w", "w", "w", "a", "a"]
            elif [2,29] not in state['game'] and [2,28] not in state['game'] and [3,29] not in state['game'] and [4,29] not in state['game']:
                keys = ["w", "w", "w", "a"]
            elif [3,29] not in state['game'] and [3,28] not in state['game'] and [4,29] not in state['game'] and [5,29] not in state['game']: 
                keys = ["w", "w", "w"]
            elif [4,29] not in state['game'] and [4,28] not in state['game'] and [5,29] not in state['game'] and [6,29] not in state['game']: 
                keys = ["w", "w", "w", "d"]
            elif [5,29] not in state['game'] and [5,28] not in state['game'] and [6,29] not in state['game'] and [7,29] not in state['game']: 
                keys = ["w", "w", "w", "d", "d"]
            elif [6,29] not in state['game'] and [6,28] not in state['game'] and [7,29] not in state['game'] and [8,29] not in state['game']: #fim J rodado 3 vezes
                keys = ["w", "w", "w", "d", "d", "d"]
            elif [8,29] not in state['game'] and [8,28] not in state['game'] and [8,27] not in state['game'] and [7,29] not in state['game'] and [7,28] not in state['game'] and [7,27] not in state['game']: 
                keys = ["w", "w", "d", "d", "d", "d"]
            elif [7,29] not in state['game'] and [7,28] not in state['game'] and [7,27] not in state['game'] and [6,29] not in state['game'] and [6,28] not in state['game'] and [6,27] not in state['game']:
                keys = ["w", "w", "d", "d", "d"]
            elif [6,29] not in state['game'] and [6,28] not in state['game'] and [6,27] not in state['game'] and [5,29] not in state['game'] and [5,28] not in state['game'] and [5,27] not in state['game']:
                keys = ["w", "w", "d", "d"]
            elif [5,29] not in state['game'] and [5,28] not in state['game'] and [5,27] not in state['game'] and [4,29] not in state['game'] and [4,28] not in state['game'] and [4,27] not in state['game']:
                keys = ["w", "w", "d"]
            elif [4,29] not in state['game'] and [4,28] not in state['game'] and [4,27] not in state['game'] and [3,29] not in state['game'] and [3,28] not in state['game'] and [3,27] not in state['game']:
                keys = ["w", "w"]
            elif [3,29] not in state['game'] and [3,28] not in state['game'] and [3,27] not in state['game'] and [2,29] not in state['game'] and [2,28] not in state['game'] and [2,27] not in state['game']:
                keys = ["w", "w", "a"]
            elif [2,29] not in state['game'] and [2,28] not in state['game'] and [2,27] not in state['game'] and [1,29] not in state['game'] and [1,28] not in state['game'] and [1,27] not in state['game']: #fim j rodado 2 vezes
                keys = ["w", "w", "a", "a"]
            elif [1,28] not in state['game'] and [2,28] not in state['game'] and [3,28] not in state['game'] and [3,29] not in state['game']: 
                keys = ["w", "a", "a"]
            elif [2,28] not in state['game'] and [3,28] not in state['game'] and [4,28] not in state['game'] and [4,29] not in state['game']: 
                keys = ["w", "a"]
            elif [3,28] not in state['game'] and [4,28] not in state['game'] and [5,28] not in state['game'] and [5,29] not in state['game']: 
                keys = ["w"]
            elif [4,28] not in state['game'] and [5,28] not in state['game'] and [6,28] not in state['game'] and [6,29] not in state['game']: 
                keys = ["w", "d"]
            elif [5,28] not in state['game'] and [6,28] not in state['game'] and [7,28] not in state['game'] and [7,29] not in state['game']: 
                keys = ["w", "d", "d"]
            elif [6,28] not in state['game'] and [7,28] not in state['game'] and [8,28] not in state['game'] and [8,29] not in state['game']: #fim j rodado 1 vez 
                keys = ["w", "d", "d", "d"]
            elif [8,27] not in state['game'] and [7,27] not in state['game'] and [7,28] not in state['game'] and [7,29] not in state['game']: 
                keys = ["d", "d", "d"]
            elif [7,27] not in state['game'] and [6,27] not in state['game'] and [6,28] not in state['game'] and [6,29] not in state['game']: 
                keys = ["d", "d"]
            elif [6,27] not in state['game'] and [5,27] not in state['game'] and [5,28] not in state['game'] and [5,29] not in state['game']: 
                keys = ["d"]
            elif [5,27] not in state['game'] and [4,27] not in state['game'] and [4,28] not in state['game'] and [4,29] not in state['game']: 
                keys = []
            elif [4,27] not in state['game'] and [3,27] not in state['game'] and [3,28] not in state['game'] and [3,29] not in state['game']: 
                keys = ["a"]
            elif [3,27] not in state['game'] and [2,27] not in state['game'] and [2,28] not in state['game'] and [2,29] not in state['game']: 
                keys = ["a", "a"]
            elif [2,27] not in state['game'] and [1,27] not in state['game'] and [1,28] not in state['game'] and [1,29] not in state['game']: #fim j normal
                keys = ["a", "a", "a"]

                ### 1J camada

            elif [1,28] not in state['game'] and [1,27] not in state['game'] and [2,28] not in state['game'] and [3,28] not in state['game']: 
                keys = ["w", "w", "w", "a", "a"]
            elif [2,28] not in state['game'] and [2,27] not in state['game'] and [3,28] not in state['game'] and [4,28] not in state['game']:
                keys = ["w", "w", "w", "a"]
            elif [3,28] not in state['game'] and [3,27] not in state['game'] and [4,28] not in state['game'] and [5,28] not in state['game']: 
                keys = ["w", "w", "w"]
            elif [4,28] not in state['game'] and [4,27] not in state['game'] and [5,28] not in state['game'] and [6,28] not in state['game']: 
                keys = ["w", "w", "w", "d"]
            elif [5,28] not in state['game'] and [5,27] not in state['game'] and [6,28] not in state['game'] and [7,28] not in state['game']: 
                keys = ["w", "w", "w", "d", "d"]
            elif [6,28] not in state['game'] and [6,27] not in state['game'] and [7,28] not in state['game'] and [8,28] not in state['game']: #fim J rodado 3 vezes
                keys = ["w", "w", "w", "d", "d", "d"]
            elif [8,28] not in state['game'] and [8,27] not in state['game'] and [8,26] not in state['game'] and [7,28] not in state['game'] and [7,27] not in state['game'] and [7,26] not in state['game']:
                keys = ["w", "w", "d", "d", "d", "d"]
            elif [7,28] not in state['game'] and [7,27] not in state['game'] and [7,26] not in state['game'] and [6,28] not in state['game'] and [6,27] not in state['game'] and [6,26] not in state['game']:
                keys = ["w", "w", "d", "d", "d"]
            elif [6,28] not in state['game'] and [6,27] not in state['game'] and [6,26] not in state['game'] and [5,28] not in state['game'] and [5,27] not in state['game'] and [5,26] not in state['game']:
                keys = ["w", "w", "d", "d"]
            elif [5,28] not in state['game'] and [5,27] not in state['game'] and [5,26] not in state['game'] and [4,28] not in state['game'] and [4,27] not in state['game'] and [4,26] not in state['game']: 
                keys = ["w", "w", "d"]
            elif [4,28] not in state['game'] and [4,27] not in state['game'] and [4,26] not in state['game'] and [3,28] not in state['game'] and [3,27] not in state['game'] and [3,26] not in state['game']: 
                keys = ["w", "w"]
            elif [3,28] not in state['game'] and [3,27] not in state['game'] and [3,26] not in state['game'] and [2,28] not in state['game'] and [2,27] not in state['game'] and [2,26] not in state['game']: 
                keys = ["w", "w", "a"]
            elif [2,28] not in state['game'] and [2,27] not in state['game'] and [2,26] not in state['game'] and [1,28] not in state['game'] and [1,27] not in state['game'] and [1,26] not in state['game']: #fim j rodado 2 vezes
                keys = ["w", "w", "a", "a"]
            elif [1,27] not in state['game'] and [2,27] not in state['game'] and [3,27] not in state['game'] and [3,28] not in state['game']: 
                keys = ["w", "a", "a"]
            elif [2,27] not in state['game'] and [3,27] not in state['game'] and [4,27] not in state['game'] and [4,28] not in state['game']: 
                keys = ["w", "a"]
            elif [3,27] not in state['game'] and [4,27] not in state['game'] and [5,27] not in state['game'] and [5,28] not in state['game']: 
                keys = ["w"]
            elif [4,27] not in state['game'] and [5,27] not in state['game'] and [6,27] not in state['game'] and [6,28] not in state['game']: 
                keys = ["w", "d"]
            elif [5,27] not in state['game'] and [6,27] not in state['game'] and [7,27] not in state['game'] and [7,28] not in state['game']: 
                keys = ["w", "d", "d"]
            elif [6,27] not in state['game'] and [7,27] not in state['game'] and [8,27] not in state['game'] and [8,28] not in state['game']: #fim j rodado 1 vez 
                keys = ["w", "d", "d", "d"]
            elif [8,26] not in state['game'] and [7,26] not in state['game'] and [7,27] not in state['game'] and [7,28] not in state['game']: 
                keys = ["d", "d", "d"]
            elif [7,26] not in state['game'] and [6,26] not in state['game'] and [6,27] not in state['game'] and [6,28] not in state['game']: 
                keys = ["d", "d"]
            elif [6,26] not in state['game'] and [5,26] not in state['game'] and [5,27] not in state['game'] and [5,28] not in state['game']: 
                keys = ["d"]
            elif [5,26] not in state['game'] and [4,26] not in state['game'] and [4,27] not in state['game'] and [4,28] not in state['game']: 
                keys = []
            elif [4,26] not in state['game'] and [3,26] not in state['game'] and [3,27] not in state['game'] and [3,28] not in state['game']: 
                keys = ["a"]
            elif [3,26] not in state['game'] and [2,26] not in state['game'] and [2,27] not in state['game'] and [2,28] not in state['game']: 
                keys = ["a", "a"]
            elif [2,26] not in state['game'] and [1,26] not in state['game'] and [1,27] not in state['game'] and [1,28] not in state['game']: #fim j normal
                keys = ["a", "a", "a"] 

                ### 2J camada

            elif [1,27] not in state['game'] and [1,26] not in state['game'] and [2,27] not in state['game'] and [3,27] not in state['game']: 
                keys = ["w", "w", "w", "a", "a"]
            elif [2,27] not in state['game'] and [2,26] not in state['game'] and [3,27] not in state['game'] and [4,27] not in state['game']:
                keys = ["w", "w", "w", "a"]
            elif [3,27] not in state['game'] and [3,26] not in state['game'] and [4,27] not in state['game'] and [5,27] not in state['game']: 
                keys = ["w", "w", "w"]
            elif [4,27] not in state['game'] and [4,26] not in state['game'] and [5,27] not in state['game'] and [6,27] not in state['game']: 
                keys = ["w", "w", "w", "d"]
            elif [5,27] not in state['game'] and [5,26] not in state['game'] and [6,27] not in state['game'] and [7,27] not in state['game']: 
                keys = ["w", "w", "w", "d", "d"]
            elif [6,27] not in state['game'] and [6,26] not in state['game'] and [7,27] not in state['game'] and [8,27] not in state['game']: #fim J rodado 3 vezes
                keys = ["w", "w", "w", "d", "d", "d"]
            elif [8,27] not in state['game'] and [8,26] not in state['game'] and [8,25] not in state['game'] and [7,27] not in state['game'] and [7,26] not in state['game'] and [7,25] not in state['game']:
                keys = ["w", "w", "d", "d", "d", "d"]
            elif [7,27] not in state['game'] and [7,26] not in state['game'] and [7,25] not in state['game'] and [6,27] not in state['game'] and [6,26] not in state['game'] and [6,25] not in state['game']: 
                keys = ["w", "w", "d", "d", "d"]
            elif [6,27] not in state['game'] and [6,26] not in state['game'] and [6,25] not in state['game'] and [5,27] not in state['game'] and [5,26] not in state['game'] and [5,25] not in state['game']:
                keys = ["w", "w", "d", "d"]
            elif [5,27] not in state['game'] and [5,26] not in state['game'] and [5,25] not in state['game'] and [4,27] not in state['game'] and [4,26] not in state['game'] and [4,25] not in state['game']: 
                keys = ["w", "w", "d"]
            elif [4,27] not in state['game'] and [4,26] not in state['game'] and [4,25] not in state['game'] and [3,27] not in state['game'] and [3,26] not in state['game'] and [3,25] not in state['game']:
                keys = ["w", "w"]
            elif [3,27] not in state['game'] and [3,26] not in state['game'] and [3,25] not in state['game'] and [2,27] not in state['game'] and [2,26] not in state['game'] and [2,25] not in state['game']:
                keys = ["w", "w", "a"]
            elif [2,27] not in state['game'] and [2,26] not in state['game'] and [2,25] not in state['game'] and [1,27] not in state['game'] and [1,26] not in state['game'] and [1,25] not in state['game']: #fim j rodado 2 vezes
                keys = ["w", "w", "a", "a"]
            elif [1,26] not in state['game'] and [2,26] not in state['game'] and [3,26] not in state['game'] and [3,27] not in state['game']: 
                keys = ["w", "a", "a"]
            elif [2,26] not in state['game'] and [3,26] not in state['game'] and [4,26] not in state['game'] and [4,27] not in state['game']: 
                keys = ["w", "a"]
            elif [3,26] not in state['game'] and [4,26] not in state['game'] and [5,26] not in state['game'] and [5,27] not in state['game']: 
                keys = ["w"]
            elif [4,26] not in state['game'] and [5,26] not in state['game'] and [6,26] not in state['game'] and [6,27] not in state['game']: 
                keys = ["w", "d"]
            elif [5,26] not in state['game'] and [6,26] not in state['game'] and [7,26] not in state['game'] and [7,27] not in state['game']: 
                keys = ["w", "d", "d"]
            elif [6,26] not in state['game'] and [7,26] not in state['game'] and [8,26] not in state['game'] and [8,27] not in state['game']: #fim j rodado 1 vez 
                keys = ["w", "d", "d", "d"]
            elif [8,25] not in state['game'] and [7,25] not in state['game'] and [7,26] not in state['game'] and [7,27] not in state['game']: 
                keys = ["d", "d", "d"]
            elif [7,25] not in state['game'] and [6,25] not in state['game'] and [6,26] not in state['game'] and [6,27] not in state['game']: 
                keys = ["d", "d"]
            elif [6,25] not in state['game'] and [5,25] not in state['game'] and [5,26] not in state['game'] and [5,27] not in state['game']: 
                keys = ["d"]
            elif [5,25] not in state['game'] and [4,25] not in state['game'] and [4,26] not in state['game'] and [4,27] not in state['game']: 
                keys = []
            elif [4,25] not in state['game'] and [3,25] not in state['game'] and [3,26] not in state['game'] and [3,27] not in state['game']: 
                keys = ["a"]
            elif [3,25] not in state['game'] and [2,25] not in state['game'] and [2,26] not in state['game'] and [2,27] not in state['game']: 
                keys = ["a", "a"]
            elif [2,25] not in state['game'] and [1,25] not in state['game'] and [1,26] not in state['game'] and [1,27] not in state['game']: #fim j normal
                keys = ["a", "a", "a"]

             ### 3J camada -----------------

            elif [1,26] not in state['game'] and [1,25] not in state['game'] and [2,26] not in state['game'] and [3,26] not in state['game']: 
                keys = ["w", "w", "w", "a", "a"]
            elif [2,26] not in state['game'] and [2,25] not in state['game'] and [3,26] not in state['game'] and [4,26] not in state['game']:
                keys = ["w", "w", "w", "a"]
            elif [3,26] not in state['game'] and [3,25] not in state['game'] and [4,26] not in state['game'] and [5,26] not in state['game']: 
                keys = ["w", "w", "w"]
            elif [4,26] not in state['game'] and [4,25] not in state['game'] and [5,26] not in state['game'] and [6,26] not in state['game']: 
                keys = ["w", "w", "w", "d"]
            elif [5,26] not in state['game'] and [5,25] not in state['game'] and [6,26] not in state['game'] and [7,26] not in state['game']: 
                keys = ["w", "w", "w", "d", "d"]
            elif [6,26] not in state['game'] and [6,25] not in state['game'] and [7,26] not in state['game'] and [8,26] not in state['game']: #fim J rodado 3 vezes
                keys = ["w", "w", "w", "d", "d", "d"]
            elif [8,26] not in state['game'] and [8,25] not in state['game'] and [8,24] not in state['game'] and [7,26] not in state['game'] and [7,25] not in state['game'] and [7,24] not in state['game']: 
                keys = ["w", "w", "d", "d", "d", "d"]
            elif [7,26] not in state['game'] and [7,25] not in state['game'] and [7,24] not in state['game'] and [6,26] not in state['game'] and [6,25] not in state['game'] and [6,24] not in state['game']:
                keys = ["w", "w", "d", "d", "d"]
            elif [6,26] not in state['game'] and [6,25] not in state['game'] and [6,24] not in state['game'] and [5,26] not in state['game'] and [5,25] not in state['game'] and [5,24] not in state['game']: 
                keys = ["w", "w", "d", "d"]
            elif [5,26] not in state['game'] and [5,25] not in state['game'] and [5,24] not in state['game'] and [4,26] not in state['game'] and [4,25] not in state['game'] and [4,24] not in state['game']:
                keys = ["w", "w", "d"]
            elif [4,26] not in state['game'] and [4,25] not in state['game'] and [4,24] not in state['game'] and [3,26] not in state['game'] and [3,25] not in state['game'] and [3,24] not in state['game']: 
                keys = ["w", "w"]
            elif [3,26] not in state['game'] and [3,25] not in state['game'] and [3,24] not in state['game'] and [2,26] not in state['game'] and [2,25] not in state['game'] and [2,24] not in state['game']: 
                keys = ["w", "w", "a"]
            elif [2,26] not in state['game'] and [2,25] not in state['game'] and [2,24] not in state['game'] and [1,26] not in state['game'] and [1,25] not in state['game'] and [1,24] not in state['game']: #fim j rodado 2 vezes
                keys = ["w", "w", "a", "a"]
            elif [1,25] not in state['game'] and [2,25] not in state['game'] and [3,25] not in state['game'] and [3,26] not in state['game']: 
                keys = ["w", "a", "a"]
            elif [2,25] not in state['game'] and [3,25] not in state['game'] and [4,25] not in state['game'] and [4,26] not in state['game']: 
                keys = ["w", "a"]
            elif [3,25] not in state['game'] and [4,25] not in state['game'] and [5,25] not in state['game'] and [5,26] not in state['game']: 
                keys = ["w"]
            elif [4,25] not in state['game'] and [5,25] not in state['game'] and [6,25] not in state['game'] and [6,26] not in state['game']: 
                keys = ["w", "d"]
            elif [5,25] not in state['game'] and [6,25] not in state['game'] and [7,25] not in state['game'] and [7,26] not in state['game']: 
                keys = ["w", "d", "d"]
            elif [6,25] not in state['game'] and [7,25] not in state['game'] and [8,25] not in state['game'] and [8,26] not in state['game']: #fim j rodado 1 vez 
                keys = ["w", "d", "d", "d"]
            elif [8,24] not in state['game'] and [7,24] not in state['game'] and [7,25] not in state['game'] and [7,26] not in state['game']: 
                keys = ["d", "d", "d"]
            elif [7,24] not in state['game'] and [6,24] not in state['game'] and [6,25] not in state['game'] and [6,26] not in state['game']: 
                keys = ["d", "d"]
            elif [6,24] not in state['game'] and [5,24] not in state['game'] and [5,25] not in state['game'] and [5,26] not in state['game']: 
                keys = ["d"]
            elif [5,24] not in state['game'] and [4,24] not in state['game'] and [4,25] not in state['game'] and [4,26] not in state['game']: 
                keys = []
            elif [4,24] not in state['game'] and [3,24] not in state['game'] and [3,25] not in state['game'] and [3,26] not in state['game']: 
                keys = ["a"]
            elif [3,24] not in state['game'] and [2,24] not in state['game'] and [2,25] not in state['game'] and [2,26] not in state['game']: 
                keys = ["a", "a"]
            elif [2,24] not in state['game'] and [1,24] not in state['game'] and [1,25] not in state['game'] and [1,26] not in state['game']: #fim j normal
                keys = ["a", "a", "a"]

             ### 4J camada -----------------

            elif [1,25] not in state['game'] and [1,24] not in state['game'] and [2,25] not in state['game'] and [3,25] not in state['game']: 
                keys = ["w", "w", "w", "a", "a"]
            elif [2,25] not in state['game'] and [2,24] not in state['game'] and [3,25] not in state['game'] and [4,25] not in state['game']:
                keys = ["w", "w", "w", "a"]
            elif [3,25] not in state['game'] and [3,24] not in state['game'] and [4,25] not in state['game'] and [5,25] not in state['game']: 
                keys = ["w", "w", "w"]
            elif [4,25] not in state['game'] and [4,24] not in state['game'] and [5,25] not in state['game'] and [6,25] not in state['game']: 
                keys = ["w", "w", "w", "d"]
            elif [5,25] not in state['game'] and [5,24] not in state['game'] and [6,25] not in state['game'] and [7,25] not in state['game']: 
                keys = ["w", "w", "w", "d", "d"]
            elif [6,25] not in state['game'] and [6,24] not in state['game'] and [7,25] not in state['game'] and [8,25] not in state['game']: #fim J rodado 3 vezes
                keys = ["w", "w", "w", "d", "d", "d"]
            elif [8,25] not in state['game'] and [8,24] not in state['game'] and [8,23] not in state['game'] and [7,25] not in state['game'] and [7,24] not in state['game'] and [7,23] not in state['game']:
                keys = ["w", "w", "d", "d", "d", "d"]
            elif [7,25] not in state['game'] and [7,24] not in state['game'] and [7,23] not in state['game'] and [6,25] not in state['game'] and [6,24] not in state['game'] and [6,23] not in state['game']:
                keys = ["w", "w", "d", "d", "d"]
            elif [6,25] not in state['game'] and [6,24] not in state['game'] and [6,23] not in state['game'] and [5,25] not in state['game'] and [5,24] not in state['game'] and [5,23] not in state['game']: 
                keys = ["w", "w", "d", "d"]
            elif [5,25] not in state['game'] and [5,24] not in state['game'] and [5,23] not in state['game'] and [4,25] not in state['game'] and [4,24] not in state['game'] and [4,23] not in state['game']: 
                keys = ["w", "w", "d"]
            elif [4,25] not in state['game'] and [4,24] not in state['game'] and [4,23] not in state['game'] and [3,25] not in state['game'] and [3,24] not in state['game'] and [3,23] not in state['game']:
                keys = ["w", "w"]
            elif [3,25] not in state['game'] and [3,24] not in state['game'] and [3,23] not in state['game'] and [2,25] not in state['game'] and [2,24] not in state['game'] and [2,23] not in state['game']: 
                keys = ["w", "w", "a"]
            elif [2,25] not in state['game'] and [2,24] not in state['game'] and [2,23] not in state['game'] and [1,25] not in state['game'] and [1,24] not in state['game'] and [1,23] not in state['game']: #fim j rodado 2 vezes
                keys = ["w", "w", "a", "a"]
            elif [1,24] not in state['game'] and [2,24] not in state['game'] and [3,24] not in state['game'] and [3,25] not in state['game']: 
                keys = ["w", "a", "a"]
            elif [2,24] not in state['game'] and [3,24] not in state['game'] and [4,24] not in state['game'] and [4,25] not in state['game']: 
                keys = ["w", "a"]
            elif [3,24] not in state['game'] and [4,24] not in state['game'] and [5,24] not in state['game'] and [5,25] not in state['game']: 
                keys = ["w"]
            elif [4,24] not in state['game'] and [5,24] not in state['game'] and [6,24] not in state['game'] and [6,25] not in state['game']: 
                keys = ["w", "d"]
            elif [5,24] not in state['game'] and [6,24] not in state['game'] and [7,24] not in state['game'] and [7,25] not in state['game']: 
                keys = ["w", "d", "d"]
            elif [6,24] not in state['game'] and [7,24] not in state['game'] and [8,24] not in state['game'] and [8,25] not in state['game']: #fim j rodado 1 vez 
                keys = ["w", "d", "d", "d"]
            elif [8,23] not in state['game'] and [7,23] not in state['game'] and [7,24] not in state['game'] and [7,25] not in state['game']: 
                keys = ["d", "d", "d"]
            elif [7,23] not in state['game'] and [6,23] not in state['game'] and [6,24] not in state['game'] and [6,25] not in state['game']: 
                keys = ["d", "d"]
            elif [6,23] not in state['game'] and [5,23] not in state['game'] and [5,24] not in state['game'] and [5,25] not in state['game']: 
                keys = ["d"]
            elif [5,23] not in state['game'] and [4,23] not in state['game'] and [4,24] not in state['game'] and [4,25] not in state['game']: 
                keys = []
            elif [4,23] not in state['game'] and [3,23] not in state['game'] and [3,24] not in state['game'] and [3,25] not in state['game']: 
                keys = ["a"]
            elif [3,23] not in state['game'] and [2,23] not in state['game'] and [2,24] not in state['game'] and [2,25] not in state['game']: 
                keys = ["a", "a"]
            elif [2,23] not in state['game'] and [1,23] not in state['game'] and [1,24] not in state['game'] and [1,25] not in state['game']: #fim j normal
                keys = ["a", "a", "a"]
            
             ### 5J camada -----------------

            elif [1,24] not in state['game'] and [1,23] not in state['game'] and [2,24] not in state['game'] and [3,24] not in state['game']: 
                keys = ["w", "w", "w", "a", "a"]
            elif [2,24] not in state['game'] and [2,23] not in state['game'] and [3,24] not in state['game'] and [4,24] not in state['game']:
                keys = ["w", "w", "w", "a"]
            elif [3,24] not in state['game'] and [3,23] not in state['game'] and [4,24] not in state['game'] and [5,24] not in state['game']: 
                keys = ["w", "w", "w"]
            elif [4,24] not in state['game'] and [4,23] not in state['game'] and [5,24] not in state['game'] and [6,24] not in state['game']: 
                keys = ["w", "w", "w", "d"]
            elif [5,24] not in state['game'] and [5,23] not in state['game'] and [6,24] not in state['game'] and [7,24] not in state['game']: 
                keys = ["w", "w", "w", "d", "d"]
            elif [6,24] not in state['game'] and [6,23] not in state['game'] and [7,24] not in state['game'] and [8,24] not in state['game']: #fim J rodado 3 vezes
                keys = ["w", "w", "w", "d", "d", "d"]
            elif [8,24] not in state['game'] and [8,23] not in state['game'] and [8,22] not in state['game'] and [7,24] not in state['game'] and [7,23] not in state['game'] and [7,22] not in state['game']: 
                keys = ["w", "w", "d", "d", "d", "d"]
            elif [7,24] not in state['game'] and [7,23] not in state['game'] and [7,22] not in state['game'] and [6,24] not in state['game'] and [6,23] not in state['game'] and [6,22] not in state['game']:
                keys = ["w", "w", "d", "d", "d"]
            elif [6,24] not in state['game'] and [6,23] not in state['game'] and [6,22] not in state['game'] and [5,24] not in state['game'] and [5,23] not in state['game'] and [5,22] not in state['game']: 
                keys = ["w", "w", "d", "d"]
            elif [5,24] not in state['game'] and [5,23] not in state['game'] and [5,22] not in state['game'] and [4,24] not in state['game'] and [4,23] not in state['game'] and [4,22] not in state['game']: 
                keys = ["w", "w", "d"]
            elif [4,24] not in state['game'] and [4,23] not in state['game'] and [4,22] not in state['game'] and [3,24] not in state['game'] and [3,23] not in state['game'] and [3,22] not in state['game']: 
                keys = ["w", "w"]
            elif [3,24] not in state['game'] and [3,23] not in state['game'] and [3,22] not in state['game'] and [2,24] not in state['game'] and [2,23] not in state['game'] and [2,22] not in state['game']: 
                keys = ["w", "w", "a"]
            elif [2,24] not in state['game'] and [2,23] not in state['game'] and [2,22] not in state['game'] and [1,24] not in state['game'] and [1,23] not in state['game'] and [1,22] not in state['game']: #fim j rodado 2 vezes
                keys = ["w", "w", "a", "a"]
            elif [1,23] not in state['game'] and [2,23] not in state['game'] and [3,23] not in state['game'] and [3,24] not in state['game']: 
                keys = ["w", "a", "a"]
            elif [2,23] not in state['game'] and [3,23] not in state['game'] and [4,23] not in state['game'] and [4,24] not in state['game']: 
                keys = ["w", "a"]
            elif [3,23] not in state['game'] and [4,23] not in state['game'] and [5,23] not in state['game'] and [5,24] not in state['game']: 
                keys = ["w"]
            elif [4,23] not in state['game'] and [5,23] not in state['game'] and [6,23] not in state['game'] and [6,24] not in state['game']: 
                keys = ["w", "d"]
            elif [5,23] not in state['game'] and [6,23] not in state['game'] and [7,23] not in state['game'] and [7,24] not in state['game']: 
                keys = ["w", "d", "d"]
            elif [6,23] not in state['game'] and [7,23] not in state['game'] and [8,23] not in state['game'] and [8,24] not in state['game']: #fim j rodado 1 vez 
                keys = ["w", "d", "d", "d"]
            elif [8,22] not in state['game'] and [7,22] not in state['game'] and [7,23] not in state['game'] and [7,24] not in state['game']: 
                keys = ["d", "d", "d"]
            elif [7,22] not in state['game'] and [6,22] not in state['game'] and [6,23] not in state['game'] and [6,24] not in state['game']: 
                keys = ["d", "d"]
            elif [6,22] not in state['game'] and [5,22] not in state['game'] and [5,23] not in state['game'] and [5,24] not in state['game']: 
                keys = ["d"]
            elif [5,22] not in state['game'] and [4,22] not in state['game'] and [4,23] not in state['game'] and [4,24] not in state['game']: 
                keys = []
            elif [4,22] not in state['game'] and [3,22] not in state['game'] and [3,23] not in state['game'] and [3,24] not in state['game']: 
                keys = ["a"]
            elif [3,22] not in state['game'] and [2,22] not in state['game'] and [2,23] not in state['game'] and [2,24] not in state['game']: 
                keys = ["a", "a"]
            elif [2,22] not in state['game'] and [1,22] not in state['game'] and [1,23] not in state['game'] and [1,24] not in state['game']: #fim j normal
                keys = ["a", "a", "a"]

            ### 6J camada -----------------

            elif [1,23] not in state['game'] and [1,22] not in state['game'] and [2,23] not in state['game'] and [3,23] not in state['game']: 
                keys = ["w", "w", "w", "a", "a"]
            elif [2,23] not in state['game'] and [2,22] not in state['game'] and [3,23] not in state['game'] and [4,23] not in state['game']:
                keys = ["w", "w", "w", "a"]
            elif [3,23] not in state['game'] and [3,22] not in state['game'] and [4,23] not in state['game'] and [5,23] not in state['game']: 
                keys = ["w", "w", "w"]
            elif [4,23] not in state['game'] and [4,22] not in state['game'] and [5,23] not in state['game'] and [6,23] not in state['game']: 
                keys = ["w", "w", "w", "d"]
            elif [5,23] not in state['game'] and [5,22] not in state['game'] and [6,23] not in state['game'] and [7,23] not in state['game']: 
                keys = ["w", "w", "w", "d", "d"]
            elif [6,23] not in state['game'] and [6,22] not in state['game'] and [7,23] not in state['game'] and [8,23] not in state['game']: #fim J rodado 3 vezes
                keys = ["w", "w", "w", "d", "d", "d"]
            elif [8,23] not in state['game'] and [8,22] not in state['game'] and [8,21] not in state['game'] and [7,23] not in state['game'] and [7,22] not in state['game'] and [7,21] not in state['game']: 
                keys = ["w", "w", "d", "d", "d", "d"]
            elif [7,23] not in state['game'] and [7,22] not in state['game'] and [7,21] not in state['game'] and [6,23] not in state['game'] and [6,22] not in state['game'] and [6,21] not in state['game']: 
                keys = ["w", "w", "d", "d", "d"]
            elif [6,23] not in state['game'] and [6,22] not in state['game'] and [6,21] not in state['game'] and [5,23] not in state['game'] and [5,22] not in state['game'] and [5,21] not in state['game']: 
                keys = ["w", "w", "d", "d"]
            elif [5,23] not in state['game'] and [5,22] not in state['game'] and [5,21] not in state['game'] and [4,23] not in state['game'] and [4,22] not in state['game'] and [4,21] not in state['game']: 
                keys = ["w", "w", "d"]
            elif [4,23] not in state['game'] and [4,22] not in state['game'] and [4,21] not in state['game'] and [3,23] not in state['game'] and [3,22] not in state['game'] and [3,21] not in state['game']: 
                keys = ["w", "w"]
            elif [3,23] not in state['game'] and [3,22] not in state['game'] and [3,21] not in state['game'] and [2,23] not in state['game'] and [2,22] not in state['game'] and [2,21] not in state['game']:
                keys = ["w", "w", "a"]
            elif [2,23] not in state['game'] and [2,22] not in state['game'] and [2,21] not in state['game'] and [1,23] not in state['game'] and [1,22] not in state['game'] and [1,21] not in state['game']: #fim j rodado 2 vezes
                keys = ["w", "w", "a", "a"]
            elif [1,22] not in state['game'] and [2,22] not in state['game'] and [3,22] not in state['game'] and [3,23] not in state['game']: 
                keys = ["w", "a", "a"]
            elif [2,22] not in state['game'] and [3,22] not in state['game'] and [4,22] not in state['game'] and [4,23] not in state['game']: 
                keys = ["w", "a"]
            elif [3,22] not in state['game'] and [4,22] not in state['game'] and [5,22] not in state['game'] and [5,23] not in state['game']: 
                keys = ["w"]
            elif [4,22] not in state['game'] and [5,22] not in state['game'] and [6,22] not in state['game'] and [6,23] not in state['game']: 
                keys = ["w", "d"]
            elif [5,22] not in state['game'] and [6,22] not in state['game'] and [7,22] not in state['game'] and [7,23] not in state['game']: 
                keys = ["w", "d", "d"]
            elif [6,22] not in state['game'] and [7,22] not in state['game'] and [8,22] not in state['game'] and [8,23] not in state['game']: #fim j rodado 1 vez 
                keys = ["w", "d", "d", "d"]
            elif [8,21] not in state['game'] and [7,21] not in state['game'] and [7,22] not in state['game'] and [7,23] not in state['game']: 
                keys = ["d", "d", "d"]
            elif [7,21] not in state['game'] and [6,21] not in state['game'] and [6,22] not in state['game'] and [6,23] not in state['game']: 
                keys = ["d", "d"]
            elif [6,21] not in state['game'] and [5,21] not in state['game'] and [5,22] not in state['game'] and [5,23] not in state['game']: 
                keys = ["d"]
            elif [5,21] not in state['game'] and [4,21] not in state['game'] and [4,22] not in state['game'] and [4,23] not in state['game']: 
                keys = []
            elif [4,21] not in state['game'] and [3,21] not in state['game'] and [3,22] not in state['game'] and [3,23] not in state['game']: 
                keys = ["a"]
            elif [3,21] not in state['game'] and [2,21] not in state['game'] and [2,22] not in state['game'] and [2,23] not in state['game']: 
                keys = ["a", "a"]
            elif [2,21] not in state['game'] and [1,21] not in state['game'] and [1,22] not in state['game'] and [1,23] not in state['game']: #fim j normal
                keys = ["a", "a", "a"]
            else:
                keys = []
    elif peca(state) == "T":
        if state['game'] == []:
            keys = ["w", "w", "w", "a", "a", "a"] 
        else:
            if [1,29] not in state['game'] and [2,29] not in state['game'] and [3,29] not in state['game'] and [2,28] not in state['game'] and [1,28] not in state['game'] and [3,28] not in state['game']:
                keys = ["w", "w", "w", "a", "a"]
            elif [2,29] not in state['game'] and [3,29] not in state['game'] and [4,29] not in state['game'] and [3,28] not in state['game'] and [2,28] not in state['game'] and [4,28] not in state['game']: 
                keys = ["w", "w", "w", "a"]
            elif [3,29] not in state['game'] and [4,29] not in state['game'] and [5,29] not in state['game'] and [4,28] not in state['game'] and [3,28] not in state['game'] and [5,28] not in state['game']: 
                keys = ["w", "w", "w"]
            elif [4,29] not in state['game'] and [5,29] not in state['game'] and [6,29] not in state['game'] and [5,28] not in state['game'] and [4,28] not in state['game'] and [6,28] not in state['game']: 
                keys = ["w", "w", "w", "d"]
            elif [5,29] not in state['game'] and [6,29] not in state['game'] and [7,29] not in state['game'] and [6,28] not in state['game'] and [5,28] not in state['game'] and [7,28] not in state['game']: 
                keys = ["w", "w", "w", "d", "d"]
            elif [6,29] not in state['game'] and [7,29] not in state['game'] and [8,29] not in state['game'] and [7,28] not in state['game'] and [6,28] not in state['game'] and [8,28] not in state['game']: #fim T rodado 3 vezes
                keys = ["w", "w", "w", "d", "d", "d"]
            elif [1,28] not in state['game'] and [2,28] not in state['game'] and [3,28] not in state['game'] and [2,29] not in state['game']: 
                keys = ["w", "a", "a"]
            elif [2,28] not in state['game'] and [3,28] not in state['game'] and [4,28] not in state['game'] and [3,29] not in state['game']: 
                keys = ["w", "a"]
            elif [3,28] not in state['game'] and [4,28] not in state['game'] and [5,28] not in state['game'] and [4,29] not in state['game']: 
                keys = ["w"]
            elif [4,28] not in state['game'] and [5,28] not in state['game'] and [6,28] not in state['game'] and [5,29] not in state['game']: 
                keys = ["w", "d"]
            elif [5,28] not in state['game'] and [6,28] not in state['game'] and [7,28] not in state['game'] and [6,29] not in state['game']: 
                keys = ["w", "d", "d"]
            elif [6,28] not in state['game'] and [7,28] not in state['game'] and [8,28] not in state['game'] and [7,29] not in state['game']: #fim T rodado 1 vez
                keys = ["w", "d", "d", "d"]
            elif [1,29] not in state['game'] and [1,28] not in state['game'] and [1,27] not in state['game'] and [2,28] not in state['game'] and [2,27] not in state['game'] and [2,26] not in state['game']: 
                keys = ["a", "a", "a"]
            elif [2,29] not in state['game'] and [2,28] not in state['game'] and [2,27] not in state['game'] and [3,28] not in state['game'] and [3,27] not in state['game'] and [3,26] not in state['game']: 
                keys = ["a", "a"]
            elif [3,29] not in state['game'] and [3,28] not in state['game'] and [3,27] not in state['game'] and [4,28] not in state['game'] and [4,27] not in state['game'] and [4,26] not in state['game']:
                keys = ["a"]
            elif [4,29] not in state['game'] and [4,28] not in state['game'] and [4,27] not in state['game'] and [5,28] not in state['game'] and [5,27] not in state['game'] and [5,26] not in state['game']:
                keys = []
            elif [5,29] not in state['game'] and [5,28] not in state['game'] and [5,27] not in state['game'] and [6,28] not in state['game'] and [6,27] not in state['game'] and [6,26] not in state['game']:
                keys = ["d"]
            elif [6,29] not in state['game'] and [6,28] not in state['game'] and [6,27] not in state['game'] and [7,28] not in state['game'] and [7,27] not in state['game'] and [7,26] not in state['game']:
                keys = ["d", "d"]
            elif [7,29] not in state['game'] and [7,28] not in state['game'] and [7,27] not in state['game'] and [8,28] not in state['game'] and [8,27] not in state['game'] and [8,26] not in state['game']: #fim T normal
                keys = ["d", "d", "d"]
            elif [8,29] not in state['game'] and [8,28] not in state['game'] and [8,27] not in state['game'] and [7,28] not in state['game'] and [7,27] not in state['game'] and [7,26] not in state['game']: 
                keys = ["w", "w", "d", "d", "d", "d"]
            elif [7,29] not in state['game'] and [7,28] not in state['game'] and [7,27] not in state['game'] and [6,28] not in state['game'] and [6,27] not in state['game'] and [6,26] not in state['game']:
                keys = ["w", "w", "d", "d", "d"]
            elif [6,29] not in state['game'] and [6,28] not in state['game'] and [6,27] not in state['game'] and [5,28] not in state['game'] and [5,27] not in state['game'] and [5,26] not in state['game']:
                keys = ["w", "w", "d", "d"]
            elif [5,29] not in state['game'] and [5,28] not in state['game'] and [5,27] not in state['game'] and [4,28] not in state['game'] and [4,27] not in state['game'] and [4,26] not in state['game']:
                keys = ["w", "w", "d"]
            elif [4,29] not in state['game'] and [4,28] not in state['game'] and [4,27] not in state['game'] and [3,28] not in state['game'] and [3,27] not in state['game'] and [3,26] not in state['game']:
                keys = ["w", "w"]
            elif [3,29] not in state['game'] and [3,28] not in state['game'] and [3,27] not in state['game'] and [2,28] not in state['game'] and [2,27] not in state['game'] and [2,26] not in state['game']:
                keys = ["w", "w", "a"]
            elif [2,29] not in state['game'] and [2,28] not in state['game'] and [2,27] not in state['game'] and [1,28] not in state['game'] and [1,27] not in state['game'] and [1,26] not in state['game']: #fim T rodado 2 vezes
                keys = ["w", "w", "a", "a"]
            

                ### 1T camada-------------

            elif [1,28] not in state['game'] and [2,28] not in state['game'] and [3,28] not in state['game'] and [2,27] not in state['game'] and [1,27] not in state['game'] and [3,27] not in state['game']: 
                keys = ["w", "w", "w", "a", "a"]
            elif [2,28] not in state['game'] and [3,28] not in state['game'] and [4,28] not in state['game'] and [3,27] not in state['game'] and [2,27] not in state['game'] and [4,27] not in state['game']: 
                keys = ["w", "w", "w", "a"]
            elif [3,28] not in state['game'] and [4,28] not in state['game'] and [5,28] not in state['game'] and [4,27] not in state['game'] and [3,27] not in state['game'] and [5,27] not in state['game']: 
                keys = ["w", "w", "w"]
            elif [4,28] not in state['game'] and [5,28] not in state['game'] and [6,28] not in state['game'] and [5,27] not in state['game'] and [4,27] not in state['game'] and [6,27] not in state['game']:
                keys = ["w", "w", "w", "d"]
            elif [5,28] not in state['game'] and [6,28] not in state['game'] and [7,28] not in state['game'] and [6,27] not in state['game'] and [5,27] not in state['game'] and [7,27] not in state['game']: 
                keys = ["w", "w", "w", "d", "d"]
            elif [6,28] not in state['game'] and [7,28] not in state['game'] and [8,28] not in state['game'] and [7,27] not in state['game'] and [6,27] not in state['game'] and [8,27] not in state['game']: #fim T rodado 3 vezes
                keys = ["w", "w", "w", "d", "d", "d"]
            elif [1,27] not in state['game'] and [2,27] not in state['game'] and [3,27] not in state['game'] and [2,28] not in state['game']: 
                keys = ["w", "a", "a"]
            elif [2,27] not in state['game'] and [3,27] not in state['game'] and [4,27] not in state['game'] and [3,28] not in state['game']: 
                keys = ["w", "a"]
            elif [3,27] not in state['game'] and [4,27] not in state['game'] and [5,27] not in state['game'] and [4,28] not in state['game']: 
                keys = ["w"]
            elif [4,27] not in state['game'] and [5,27] not in state['game'] and [6,27] not in state['game'] and [5,28] not in state['game']: 
                keys = ["w", "d"]
            elif [5,27] not in state['game'] and [6,27] not in state['game'] and [7,27] not in state['game'] and [6,28] not in state['game']: 
                keys = ["w", "d", "d"]
            elif [6,27] not in state['game'] and [7,27] not in state['game'] and [8,27] not in state['game'] and [7,28] not in state['game']: #fim T rodado 1 vez
                keys = ["w", "d", "d", "d"]
            elif [1,28] not in state['game'] and [1,27] not in state['game'] and [1,26] not in state['game'] and [2,27] not in state['game'] and [2,26] not in state['game'] and [2,25] not in state['game']:
                keys = ["a", "a", "a"]
            elif [2,28] not in state['game'] and [2,27] not in state['game'] and [2,26] not in state['game'] and [3,27] not in state['game'] and [3,26] not in state['game'] and [3,25] not in state['game']:
                keys = ["a", "a"]
            elif [3,28] not in state['game'] and [3,27] not in state['game'] and [3,26] not in state['game'] and [4,27] not in state['game'] and [4,26] not in state['game'] and [4,25] not in state['game']:
                keys = ["a"]
            elif [4,28] not in state['game'] and [4,27] not in state['game'] and [4,26] not in state['game'] and [5,27] not in state['game'] and [5,26] not in state['game'] and [5,25] not in state['game']:
                keys = []
            elif [5,28] not in state['game'] and [5,27] not in state['game'] and [5,26] not in state['game'] and [6,27] not in state['game'] and [6,26] not in state['game'] and [6,25] not in state['game']:
                keys = ["d"]
            elif [6,28] not in state['game'] and [6,27] not in state['game'] and [6,26] not in state['game'] and [7,27] not in state['game'] and [7,26] not in state['game'] and [7,25] not in state['game']:
                keys = ["d", "d"]
            elif [7,28] not in state['game'] and [7,27] not in state['game'] and [7,26] not in state['game'] and [8,27] not in state['game'] and [8,26] not in state['game'] and [8,25] not in state['game']: #fim T normal
                keys = ["d", "d", "d"]
            elif [8,28] not in state['game'] and [8,27] not in state['game'] and [8,26] not in state['game'] and [7,27] not in state['game'] and [7,26] not in state['game'] and [7,25] not in state['game']:
                keys = ["w", "w", "d", "d", "d", "d"]
            elif [7,28] not in state['game'] and [7,27] not in state['game'] and [7,26] not in state['game'] and [6,27] not in state['game'] and [6,26] not in state['game'] and [6,25] not in state['game']:
                keys = ["w", "w", "d", "d", "d"]
            elif [6,28] not in state['game'] and [6,27] not in state['game'] and [6,26] not in state['game'] and [5,27] not in state['game'] and [5,26] not in state['game'] and [5,25] not in state['game']: 
                keys = ["w", "w", "d", "d"]
            elif [5,28] not in state['game'] and [5,27] not in state['game'] and [5,26] not in state['game'] and [4,27] not in state['game'] and [4,26] not in state['game'] and [4,25] not in state['game']:
                keys = ["w", "w", "d"]
            elif [4,28] not in state['game'] and [4,27] not in state['game'] and [4,26] not in state['game'] and [3,27] not in state['game'] and [3,26] not in state['game'] and [3,25] not in state['game']: 
                keys = ["w", "w"]
            elif [3,28] not in state['game'] and [3,27] not in state['game'] and [3,26] not in state['game'] and [2,27] not in state['game'] and [2,26] not in state['game'] and [2,25] not in state['game']: 
                keys = ["w", "w", "a"]
            elif [2,28] not in state['game'] and [2,27] not in state['game'] and [2,26] not in state['game'] and [1,27] not in state['game'] and [1,26] not in state['game'] and [1,25] not in state['game']:#fim T rodado 2 vezes
                keys = ["w", "w", "a", "a"]
            

                ### 2T camada-------------

            elif [1,27] not in state['game'] and [2,27] not in state['game'] and [3,27] not in state['game'] and [2,26] not in state['game'] and [1,26] not in state['game'] and [3,26] not in state['game']: 
                keys = ["w", "w", "w", "a", "a"]
            elif [2,27] not in state['game'] and [3,27] not in state['game'] and [4,27] not in state['game'] and [3,26] not in state['game'] and [2,26] not in state['game'] and [4,26] not in state['game']:  
                keys = ["w", "w", "w", "a"]
            elif [3,27] not in state['game'] and [4,27] not in state['game'] and [5,27] not in state['game'] and [4,26] not in state['game'] and [3,26] not in state['game'] and [5,26] not in state['game']: 
                keys = ["w", "w", "w"]
            elif [4,27] not in state['game'] and [5,27] not in state['game'] and [6,27] not in state['game'] and [5,26] not in state['game'] and [4,26] not in state['game'] and [6,26] not in state['game']:
                keys = ["w", "w", "w", "d"]
            elif [5,27] not in state['game'] and [6,27] not in state['game'] and [7,27] not in state['game'] and [6,26] not in state['game'] and [5,26] not in state['game'] and [7,26] not in state['game']: 
                keys = ["w", "w", "w", "d", "d"]
            elif [6,27] not in state['game'] and [7,27] not in state['game'] and [8,27] not in state['game'] and [7,26] not in state['game'] and [6,26] not in state['game'] and [8,26] not in state['game']: #fim T rodado 3 vezes
                keys = ["w", "w", "w", "d", "d", "d"]
            elif [1,26] not in state['game'] and [2,26] not in state['game'] and [3,26] not in state['game'] and [2,27] not in state['game']: 
                keys = ["w", "a", "a"]
            elif [2,26] not in state['game'] and [3,26] not in state['game'] and [4,26] not in state['game'] and [3,27] not in state['game']: 
                keys = ["w", "a"]
            elif [3,26] not in state['game'] and [4,26] not in state['game'] and [5,26] not in state['game'] and [4,27] not in state['game']: 
                keys = ["w"]
            elif [4,26] not in state['game'] and [5,26] not in state['game'] and [6,26] not in state['game'] and [5,27] not in state['game']: 
                keys = ["w", "d"]
            elif [5,26] not in state['game'] and [6,26] not in state['game'] and [7,26] not in state['game'] and [6,27] not in state['game']: 
                keys = ["w", "d", "d"]
            elif [6,26] not in state['game'] and [7,26] not in state['game'] and [8,26] not in state['game'] and [7,27] not in state['game']: #fim T rodado 1 vez
                keys = ["w", "d", "d", "d"]
            elif [1,27] not in state['game'] and [1,26] not in state['game'] and [1,25] not in state['game'] and [2,26] not in state['game'] and [2,25] not in state['game'] and [2,24] not in state['game']:
                keys = ["a", "a", "a"]
            elif [2,27] not in state['game'] and [2,26] not in state['game'] and [2,25] not in state['game'] and [3,26] not in state['game'] and [3,25] not in state['game'] and [3,24] not in state['game']:
                keys = ["a", "a"]
            elif [3,27] not in state['game'] and [3,26] not in state['game'] and [3,25] not in state['game'] and [4,26] not in state['game'] and [4,25] not in state['game'] and [4,24] not in state['game']:
                keys = ["a"]
            elif [4,27] not in state['game'] and [4,26] not in state['game'] and [4,25] not in state['game'] and [5,26] not in state['game'] and [5,25] not in state['game'] and [5,24] not in state['game']: 
                keys = []
            elif [5,27] not in state['game'] and [5,26] not in state['game'] and [5,25] not in state['game'] and [6,26] not in state['game'] and [6,25] not in state['game'] and [6,24] not in state['game']:
                keys = ["d"]
            elif [6,27] not in state['game'] and [6,26] not in state['game'] and [6,25] not in state['game'] and [7,26] not in state['game'] and [7,25] not in state['game'] and [7,24] not in state['game']:
                keys = ["d", "d"]
            elif [7,27] not in state['game'] and [7,26] not in state['game'] and [7,25] not in state['game'] and [8,26] not in state['game'] and [8,25] not in state['game'] and [8,24] not in state['game']: #fim T normal
                keys = ["d", "d", "d"]
            elif [8,27] not in state['game'] and [8,26] not in state['game'] and [8,25] not in state['game'] and [7,26] not in state['game'] and [7,25] not in state['game'] and [7,24] not in state['game']:
                keys = ["w", "w", "d", "d", "d", "d"]
            elif [7,27] not in state['game'] and [7,26] not in state['game'] and [7,25] not in state['game'] and [6,26] not in state['game'] and [6,25] not in state['game'] and [6,24] not in state['game']:
                keys = ["w", "w", "d", "d", "d"]
            elif [6,27] not in state['game'] and [6,26] not in state['game'] and [6,25] not in state['game'] and [5,26] not in state['game'] and [5,25] not in state['game'] and [5,24] not in state['game']:
                keys = ["w", "w", "d", "d"]
            elif [5,27] not in state['game'] and [5,26] not in state['game'] and [5,25] not in state['game'] and [4,26] not in state['game'] and [4,25] not in state['game'] and [4,24] not in state['game']: 
                keys = ["w", "w", "d"]
            elif [4,27] not in state['game'] and [4,26] not in state['game'] and [4,25] not in state['game'] and [3,26] not in state['game'] and [3,25] not in state['game'] and [3,24] not in state['game']: 
                keys = ["w", "w"]
            elif [3,27] not in state['game'] and [3,26] not in state['game'] and [3,25] not in state['game'] and [2,26] not in state['game'] and [2,25] not in state['game'] and [2,24] not in state['game']: 
                keys = ["w", "w", "a"]
            elif [2,27] not in state['game'] and [2,26] not in state['game'] and [2,25] not in state['game'] and [1,26] not in state['game'] and [1,25] not in state['game'] and [1,24] not in state['game']: #fim T rodado 2 vezes
                keys = ["w", "w", "a", "a"]

            ### 3T camada-------------

            elif [1,26] not in state['game'] and [2,26] not in state['game'] and [3,26] not in state['game'] and [2,25] not in state['game'] and [1,25] not in state['game'] and [3,25] not in state['game']: 
                keys = ["w", "w", "w", "a", "a"]
            elif [2,26] not in state['game'] and [3,26] not in state['game'] and [4,26] not in state['game'] and [3,25] not in state['game'] and [2,25] not in state['game'] and [4,25] not in state['game']:
                keys = ["w", "w", "w", "a"]
            elif [3,26] not in state['game'] and [4,26] not in state['game'] and [5,26] not in state['game'] and [4,25] not in state['game'] and [3,25] not in state['game'] and [5,25] not in state['game']:
                keys = ["w", "w", "w"]
            elif [4,26] not in state['game'] and [5,26] not in state['game'] and [6,26] not in state['game'] and [5,25] not in state['game'] and [4,25] not in state['game'] and [6,25] not in state['game']: 
                keys = ["w", "w", "w", "d"]
            elif [5,26] not in state['game'] and [6,26] not in state['game'] and [7,26] not in state['game'] and [6,25] not in state['game'] and [5,25] not in state['game'] and [7,25] not in state['game']: 
                keys = ["w", "w", "w", "d", "d"]
            elif [6,26] not in state['game'] and [7,26] not in state['game'] and [8,26] not in state['game'] and [7,25] not in state['game'] and [6,25] not in state['game'] and [8,25] not in state['game']: #fim T rodado 3 vezes
                keys = ["w", "w", "w", "d", "d", "d"]
            elif [1,25] not in state['game'] and [2,25] not in state['game'] and [3,25] not in state['game'] and [2,26] not in state['game']: 
                keys = ["w", "a", "a"]
            elif [2,25] not in state['game'] and [3,25] not in state['game'] and [4,25] not in state['game'] and [3,26] not in state['game']: 
                keys = ["w", "a"]
            elif [3,25] not in state['game'] and [4,25] not in state['game'] and [5,25] not in state['game'] and [4,26] not in state['game']: 
                keys = ["w"]
            elif [4,25] not in state['game'] and [5,25] not in state['game'] and [6,25] not in state['game'] and [5,26] not in state['game']: 
                keys = ["w", "d"]
            elif [5,25] not in state['game'] and [6,25] not in state['game'] and [7,25] not in state['game'] and [6,26] not in state['game']: 
                keys = ["w", "d", "d"]
            elif [6,25] not in state['game'] and [7,25] not in state['game'] and [8,25] not in state['game'] and [7,26] not in state['game']: #fim T rodado 1 vez
                keys = ["w", "d", "d", "d"]
            elif [1,26] not in state['game'] and [1,25] not in state['game'] and [1,24] not in state['game'] and [2,25] not in state['game'] and [2,24] not in state['game'] and [2,23] not in state['game']: 
                keys = ["a", "a", "a"]
            elif [2,26] not in state['game'] and [2,25] not in state['game'] and [2,24] not in state['game'] and [3,25] not in state['game'] and [3,24] not in state['game'] and [3,23] not in state['game']:
                keys = ["a", "a"]
            elif [3,26] not in state['game'] and [3,25] not in state['game'] and [3,24] not in state['game'] and [4,25] not in state['game'] and [4,24] not in state['game'] and [4,23] not in state['game']:
                keys = ["a"]
            elif [4,26] not in state['game'] and [4,25] not in state['game'] and [4,24] not in state['game'] and [5,25] not in state['game'] and [5,24] not in state['game'] and [5,23] not in state['game']:
                keys = []
            elif [5,26] not in state['game'] and [5,25] not in state['game'] and [5,24] not in state['game'] and [6,25] not in state['game'] and [6,24] not in state['game'] and [6,23] not in state['game']: 
                keys = ["d"]
            elif [6,26] not in state['game'] and [6,25] not in state['game'] and [6,24] not in state['game'] and [7,25] not in state['game'] and [7,24] not in state['game'] and [7,23] not in state['game']:
                keys = ["d", "d"]
            elif [7,26] not in state['game'] and [7,25] not in state['game'] and [7,24] not in state['game'] and [8,25] not in state['game'] and [8,24] not in state['game'] and [8,23] not in state['game']:#fim T normal
                keys = ["d", "d", "d"]
            elif [8,26] not in state['game'] and [8,25] not in state['game'] and [8,24] not in state['game'] and [7,25] not in state['game'] and [7,24] not in state['game'] and [7,23] not in state['game']:
                keys = ["w", "w", "d", "d", "d", "d"]
            elif [7,26] not in state['game'] and [7,25] not in state['game'] and [7,24] not in state['game'] and [6,25] not in state['game'] and [6,24] not in state['game'] and [6,23] not in state['game']:
                keys = ["w", "w", "d", "d", "d"]
            elif [6,26] not in state['game'] and [6,25] not in state['game'] and [6,24] not in state['game'] and [5,25] not in state['game'] and [5,24] not in state['game'] and [5,23] not in state['game']:
                keys = ["w", "w", "d", "d"]
            elif [5,26] not in state['game'] and [5,25] not in state['game'] and [5,24] not in state['game'] and [4,25] not in state['game'] and [4,24] not in state['game'] and [4,23] not in state['game']:
                keys = ["w", "w", "d"]
            elif [4,26] not in state['game'] and [4,25] not in state['game'] and [4,24] not in state['game'] and [3,25] not in state['game'] and [3,24] not in state['game'] and [3,23] not in state['game']:
                keys = ["w", "w"]
            elif [3,26] not in state['game'] and [3,25] not in state['game'] and [3,24] not in state['game'] and [2,25] not in state['game'] and [2,24] not in state['game'] and [2,23] not in state['game']:
                keys = ["w", "w", "a"]
            elif [2,26] not in state['game'] and [2,25] not in state['game'] and [2,24] not in state['game'] and [1,25] not in state['game'] and [1,24] not in state['game'] and [1,23] not in state['game']: #fim T rodado 2 vezes
                keys = ["w", "w", "a", "a"]
            
            ### 4T camada-------------

            elif [1,25] not in state['game'] and [2,25] not in state['game'] and [3,25] not in state['game'] and [2,24] not in state['game'] and [1,24] not in state['game'] and [3,24] not in state['game']: 
                keys = ["w", "w", "w", "a", "a"]
            elif [2,25] not in state['game'] and [3,25] not in state['game'] and [4,25] not in state['game'] and [3,24] not in state['game'] and [2,24] not in state['game'] and [4,24] not in state['game']: 
                keys = ["w", "w", "w", "a"]
            elif [3,25] not in state['game'] and [4,25] not in state['game'] and [5,25] not in state['game'] and [4,24] not in state['game'] and [3,24] not in state['game'] and [5,24] not in state['game']: 
                keys = ["w", "w", "w"]
            elif [4,25] not in state['game'] and [5,25] not in state['game'] and [6,25] not in state['game'] and [5,24] not in state['game'] and [4,24] not in state['game'] and [6,24] not in state['game']: 
                keys = ["w", "w", "w", "d"]
            elif [5,25] not in state['game'] and [6,25] not in state['game'] and [7,25] not in state['game'] and [6,24] not in state['game'] and [5,24] not in state['game'] and [7,24] not in state['game']:
                keys = ["w", "w", "w", "d", "d"]
            elif [6,25] not in state['game'] and [7,25] not in state['game'] and [8,25] not in state['game'] and [7,24] not in state['game'] and [6,24] not in state['game'] and [8,24] not in state['game']: #fim T rodado 3 vezes
                keys = ["w", "w", "w", "d", "d", "d"]
            elif [1,24] not in state['game'] and [2,24] not in state['game'] and [3,24] not in state['game'] and [2,25] not in state['game']: 
                keys = ["w", "a", "a"]
            elif [2,24] not in state['game'] and [3,24] not in state['game'] and [4,24] not in state['game'] and [3,25] not in state['game']: 
                keys = ["w", "a"]
            elif [3,24] not in state['game'] and [4,24] not in state['game'] and [5,24] not in state['game'] and [4,25] not in state['game']: 
                keys = ["w"]
            elif [4,24] not in state['game'] and [5,24] not in state['game'] and [6,24] not in state['game'] and [5,25] not in state['game']: 
                keys = ["w", "d"]
            elif [5,24] not in state['game'] and [6,24] not in state['game'] and [7,24] not in state['game'] and [6,25] not in state['game']: 
                keys = ["w", "d", "d"]
            elif [6,24] not in state['game'] and [7,24] not in state['game'] and [8,24] not in state['game'] and [7,25] not in state['game']: #fim T rodado 1 vez
                keys = ["w", "d", "d", "d"]
            elif [1,25] not in state['game'] and [1,24] not in state['game'] and [1,23] not in state['game'] and [2,24] not in state['game'] and [2,23] not in state['game'] and [2,22] not in state['game']:
                keys = ["a", "a", "a"]
            elif [2,25] not in state['game'] and [2,24] not in state['game'] and [2,23] not in state['game'] and [3,24] not in state['game'] and [3,23] not in state['game'] and [3,22] not in state['game']: 
                keys = ["a", "a"]
            elif [3,25] not in state['game'] and [3,24] not in state['game'] and [3,23] not in state['game'] and [4,24] not in state['game'] and [4,23] not in state['game'] and [4,22] not in state['game']: 
                keys = ["a"]
            elif [4,25] not in state['game'] and [4,24] not in state['game'] and [4,23] not in state['game'] and [5,24] not in state['game'] and [5,23] not in state['game'] and [5,22] not in state['game']: 
                keys = []
            elif [5,25] not in state['game'] and [5,24] not in state['game'] and [5,23] not in state['game'] and [6,24] not in state['game'] and [6,23] not in state['game'] and [6,22] not in state['game']:
                keys = ["d"]
            elif [6,25] not in state['game'] and [6,24] not in state['game'] and [6,23] not in state['game'] and [7,24] not in state['game'] and [7,23] not in state['game'] and [7,22] not in state['game']: 
                keys = ["d", "d"]
            elif [7,25] not in state['game'] and [7,24] not in state['game'] and [7,23] not in state['game'] and [8,24] not in state['game'] and [8,23] not in state['game'] and [8,22] not in state['game']: #fim T normal
                keys = ["d", "d", "d"]
            elif [8,25] not in state['game'] and [8,24] not in state['game'] and [8,23] not in state['game'] and [7,24] not in state['game'] and [7,23] not in state['game'] and [7,22] not in state['game']:
                keys = ["w", "w", "d", "d", "d", "d"]
            elif [7,25] not in state['game'] and [7,24] not in state['game'] and [7,23] not in state['game'] and [6,24] not in state['game'] and [6,23] not in state['game'] and [6,22] not in state['game']:
                keys = ["w", "w", "d", "d", "d"]
            elif [6,25] not in state['game'] and [6,24] not in state['game'] and [6,23] not in state['game'] and [5,24] not in state['game'] and [5,23] not in state['game'] and [5,22] not in state['game']:
                keys = ["w", "w", "d", "d"]
            elif [5,25] not in state['game'] and [5,24] not in state['game'] and [5,23] not in state['game'] and [4,24] not in state['game'] and [4,23] not in state['game'] and [4,22] not in state['game']:
                keys = ["w", "w", "d"]
            elif [4,25] not in state['game'] and [4,24] not in state['game'] and [4,23] not in state['game'] and [3,24] not in state['game'] and [3,23] not in state['game'] and [3,22] not in state['game']:
                keys = ["w", "w"]
            elif [3,25] not in state['game'] and [3,24] not in state['game'] and [3,23] not in state['game'] and [2,24] not in state['game'] and [2,23] not in state['game'] and [2,22] not in state['game']:
                keys = ["w", "w", "a"]
            elif [2,25] not in state['game'] and [2,24] not in state['game'] and [2,23] not in state['game'] and [1,24] not in state['game'] and [1,23] not in state['game'] and [1,22] not in state['game']:#fim T rodado 2 vezes
                keys = ["w", "w", "a", "a"]
            
            ### 5T camada-------------

            elif [1,24] not in state['game'] and [2,24] not in state['game'] and [3,24] not in state['game'] and [2,23] not in state['game'] and [1,23] not in state['game'] and [3,23] not in state['game']:
                keys = ["w", "w", "w", "a", "a"]
            elif [2,24] not in state['game'] and [3,24] not in state['game'] and [4,24] not in state['game'] and [3,23] not in state['game'] and [2,23] not in state['game'] and [4,23] not in state['game']: 
                keys = ["w", "w", "w", "a"]
            elif [3,24] not in state['game'] and [4,24] not in state['game'] and [5,24] not in state['game'] and [4,23] not in state['game'] and [3,23] not in state['game'] and [5,23] not in state['game']: 
                keys = ["w", "w", "w"]
            elif [4,24] not in state['game'] and [5,24] not in state['game'] and [6,24] not in state['game'] and [5,23] not in state['game'] and [4,23] not in state['game'] and [6,23] not in state['game']: 
                keys = ["w", "w", "w", "d"]
            elif [5,24] not in state['game'] and [6,24] not in state['game'] and [7,24] not in state['game'] and [6,23] not in state['game'] and [5,23] not in state['game'] and [7,23] not in state['game']:
                keys = ["w", "w", "w", "d", "d"]
            elif [6,24] not in state['game'] and [7,24] not in state['game'] and [8,24] not in state['game'] and [7,23] not in state['game'] and [6,23] not in state['game'] and [8,23] not in state['game']: #fim T rodado 3 vezes
                keys = ["w", "w", "w", "d", "d", "d"]
            elif [1,23] not in state['game'] and [2,23] not in state['game'] and [3,23] not in state['game'] and [2,24] not in state['game']: 
                keys = ["w", "a", "a"]
            elif [2,23] not in state['game'] and [3,23] not in state['game'] and [4,23] not in state['game'] and [3,24] not in state['game']: 
                keys = ["w", "a"]
            elif [3,23] not in state['game'] and [4,23] not in state['game'] and [5,23] not in state['game'] and [4,24] not in state['game']: 
                keys = ["w"]
            elif [4,23] not in state['game'] and [5,23] not in state['game'] and [6,23] not in state['game'] and [5,24] not in state['game']: 
                keys = ["w", "d"]
            elif [5,23] not in state['game'] and [6,23] not in state['game'] and [7,23] not in state['game'] and [6,24] not in state['game']: 
                keys = ["w", "d", "d"]
            elif [6,23] not in state['game'] and [7,23] not in state['game'] and [8,23] not in state['game'] and [7,24] not in state['game']: #fim T rodado 1 vez
                keys = ["w", "d", "d", "d"]
            elif [1,24] not in state['game'] and [1,23] not in state['game'] and [1,22] not in state['game'] and [2,23] not in state['game'] and [2,22] not in state['game'] and [2,21] not in state['game']:
                keys = ["a", "a", "a"]
            elif [2,24] not in state['game'] and [2,23] not in state['game'] and [2,22] not in state['game'] and [3,23] not in state['game'] and [3,22] not in state['game'] and [3,21] not in state['game']: 
                keys = ["a", "a"]
            elif [3,24] not in state['game'] and [3,23] not in state['game'] and [3,22] not in state['game'] and [4,23] not in state['game'] and [4,22] not in state['game'] and [4,21] not in state['game']: 
                keys = ["a"]
            elif [4,24] not in state['game'] and [4,23] not in state['game'] and [4,22] not in state['game'] and [5,23] not in state['game'] and [5,22] not in state['game'] and [5,21] not in state['game']:
                keys = []
            elif [5,24] not in state['game'] and [5,23] not in state['game'] and [5,22] not in state['game'] and [6,23] not in state['game'] and [6,22] not in state['game'] and [6,21] not in state['game']: 
                keys = ["d"]
            elif [6,24] not in state['game'] and [6,23] not in state['game'] and [6,22] not in state['game'] and [7,23] not in state['game'] and [7,22] not in state['game'] and [7,21] not in state['game']:
                keys = ["d", "d"]
            elif [7,24] not in state['game'] and [7,23] not in state['game'] and [7,22] not in state['game'] and [8,23] not in state['game'] and [8,22] not in state['game'] and [8,21] not in state['game']:#fim T normal
                keys = ["d", "d", "d"]
            elif [8,24] not in state['game'] and [8,23] not in state['game'] and [8,22] not in state['game'] and [7,23] not in state['game'] and [7,22] not in state['game'] and [7,21] not in state['game']: 
                keys = ["w", "w", "d", "d", "d", "d"]
            elif [7,24] not in state['game'] and [7,23] not in state['game'] and [7,22] not in state['game'] and [6,23] not in state['game'] and [6,22] not in state['game'] and [6,21] not in state['game']: 
                keys = ["w", "w", "d", "d", "d"]
            elif [6,24] not in state['game'] and [6,23] not in state['game'] and [6,22] not in state['game'] and [5,23] not in state['game'] and [5,22] not in state['game'] and [5,21] not in state['game']: 
                keys = ["w", "w", "d", "d"]
            elif [5,24] not in state['game'] and [5,23] not in state['game'] and [5,22] not in state['game'] and [4,23] not in state['game'] and [4,22] not in state['game'] and [4,21] not in state['game']:
                keys = ["w", "w", "d"]
            elif [4,24] not in state['game'] and [4,23] not in state['game'] and [4,22] not in state['game'] and [3,23] not in state['game'] and [3,22] not in state['game'] and [3,21] not in state['game']: 
                keys = ["w", "w"]
            elif [3,24] not in state['game'] and [3,23] not in state['game'] and [3,22] not in state['game'] and [2,23] not in state['game'] and [2,22] not in state['game'] and [2,21] not in state['game']: 
                keys = ["w", "w", "a"]
            elif [2,24] not in state['game'] and [2,23] not in state['game'] and [2,22] not in state['game'] and [1,23] not in state['game'] and [1,22] not in state['game'] and [1,21] not in state['game']: #fim T rodado 2 vezes
                keys = ["w", "w", "a", "a"]
             
            ### 6T camada-------------

            elif [1,23] not in state['game'] and [2,23] not in state['game'] and [3,23] not in state['game'] and [2,22] not in state['game'] and [1,22] not in state['game'] and [3,22] not in state['game']: 
                keys = ["w", "w", "w", "a", "a"]
            elif [2,23] not in state['game'] and [3,23] not in state['game'] and [4,23] not in state['game'] and [3,22] not in state['game'] and [2,22] not in state['game'] and [4,22] not in state['game']:
                keys = ["w", "w", "w", "a"]
            elif [3,23] not in state['game'] and [4,23] not in state['game'] and [5,23] not in state['game'] and [4,22] not in state['game'] and [3,22] not in state['game'] and [5,22] not in state['game']: 
                keys = ["w", "w", "w"]
            elif [4,23] not in state['game'] and [5,23] not in state['game'] and [6,23] not in state['game'] and [5,22] not in state['game'] and [4,22] not in state['game'] and [6,22] not in state['game']: 
                keys = ["w", "w", "w", "d"]
            elif [5,23] not in state['game'] and [6,23] not in state['game'] and [7,23] not in state['game'] and [6,22] not in state['game'] and [5,22] not in state['game'] and [7,22] not in state['game']: 
                keys = ["w", "w", "w", "d", "d"]
            elif [6,23] not in state['game'] and [7,23] not in state['game'] and [8,23] not in state['game'] and [7,22] not in state['game'] and [6,22] not in state['game'] and [8,22] not in state['game']: #fim T rodado 3 vezes
                keys = ["w", "w", "w", "d", "d", "d"]
            elif [1,22] not in state['game'] and [2,22] not in state['game'] and [3,22] not in state['game'] and [2,23] not in state['game']: 
                keys = ["w", "a", "a"]
            elif [2,22] not in state['game'] and [3,22] not in state['game'] and [4,22] not in state['game'] and [3,23] not in state['game']: 
                keys = ["w", "a"]
            elif [3,22] not in state['game'] and [4,22] not in state['game'] and [5,22] not in state['game'] and [4,23] not in state['game']: 
                keys = ["w"]
            elif [4,22] not in state['game'] and [5,22] not in state['game'] and [6,22] not in state['game'] and [5,23] not in state['game']: 
                keys = ["w", "d"]
            elif [5,22] not in state['game'] and [6,22] not in state['game'] and [7,22] not in state['game'] and [6,23] not in state['game']: 
                keys = ["w", "d", "d"]
            elif [6,22] not in state['game'] and [7,22] not in state['game'] and [8,22] not in state['game'] and [7,23] not in state['game']: #fim T rodado 1 vez
                keys = ["w", "d", "d", "d"]
            elif [1,23] not in state['game'] and [1,22] not in state['game'] and [1,21] not in state['game'] and [2,22] not in state['game'] and [2,21] not in state['game'] and [2,20] not in state['game']:
                keys = ["a", "a", "a"]
            elif [2,23] not in state['game'] and [2,22] not in state['game'] and [2,21] not in state['game'] and [3,22] not in state['game'] and [3,21] not in state['game'] and [3,20] not in state['game']: 
                keys = ["a", "a"]
            elif [3,23] not in state['game'] and [3,22] not in state['game'] and [3,21] not in state['game'] and [4,22] not in state['game'] and [4,21] not in state['game'] and [4,20] not in state['game']: 
                keys = ["a"]
            elif [4,23] not in state['game'] and [4,22] not in state['game'] and [4,21] not in state['game'] and [5,22] not in state['game'] and [5,21] not in state['game'] and [5,20] not in state['game']:
                keys = []
            elif [5,23] not in state['game'] and [5,22] not in state['game'] and [5,21] not in state['game'] and [6,22] not in state['game'] and [6,21] not in state['game'] and [6,20] not in state['game']: 
                keys = ["d"]
            elif [6,23] not in state['game'] and [6,22] not in state['game'] and [6,21] not in state['game'] and [7,22] not in state['game'] and [7,21] not in state['game'] and [7,20] not in state['game']:
                keys = ["d", "d"]
            elif [7,23] not in state['game'] and [7,22] not in state['game'] and [7,21] not in state['game'] and [8,22] not in state['game'] and [8,21] not in state['game'] and [8,20] not in state['game']:#fim T normal
                keys = ["d", "d", "d"]
            elif [8,23] not in state['game'] and [8,22] not in state['game'] and [8,21] not in state['game'] and [7,22] not in state['game'] and [7,21] not in state['game'] and [7,20] not in state['game']: 
                keys = ["w", "w", "d", "d", "d", "d"]
            elif [7,23] not in state['game'] and [7,22] not in state['game'] and [7,21] not in state['game'] and [6,22] not in state['game'] and [6,21] not in state['game'] and [6,20] not in state['game']: 
                keys = ["w", "w", "d", "d", "d"]
            elif [6,23] not in state['game'] and [6,22] not in state['game'] and [6,21] not in state['game'] and [5,22] not in state['game'] and [5,21] not in state['game'] and [5,20] not in state['game']: 
                keys = ["w", "w", "d", "d"]
            elif [5,23] not in state['game'] and [5,22] not in state['game'] and [5,21] not in state['game'] and [4,22] not in state['game'] and [4,21] not in state['game'] and [4,20] not in state['game']:
                keys = ["w", "w", "d"]
            elif [4,23] not in state['game'] and [4,22] not in state['game'] and [4,21] not in state['game'] and [3,22] not in state['game'] and [3,21] not in state['game'] and [3,20] not in state['game']: 
                keys = ["w", "w"]
            elif [3,23] not in state['game'] and [3,22] not in state['game'] and [3,21] not in state['game'] and [2,22] not in state['game'] and [2,21] not in state['game'] and [2,20] not in state['game']: 
                keys = ["w", "w", "a"]
            elif [2,23] not in state['game'] and [2,22] not in state['game'] and [2,21] not in state['game'] and [1,22] not in state['game'] and [1,21] not in state['game'] and [1,20] not in state['game']: #fim T rodado 2 vezes
                keys = ["w", "w", "a", "a"]
    
            else:
                keys = []
    elif peca(state) == "I":
        if state['game'] == []:
            keys = ["a", "a"]
        else:
            if [1,29] not in state['game'] and [2,29] not in state['game'] and [3,29] not in state['game'] and [4,29] not in state['game'] and [1,28] not in state['game'] and [4,28] not in state['game']:
                keys = ["a", "a", "a", "a"]
            elif [2,29] not in state['game'] and [3,29] not in state['game'] and [4,29] not in state['game'] and [5,29] not in state['game'] and [2,28] not in state['game'] and [5,28] not in state['game']:
                keys = []
            elif [3,29] not in state['game'] and [4,29] not in state['game'] and [5,29] not in state['game'] and [6,29] not in state['game'] and [3,28] not in state['game'] and [6,28] not in state['game']:
                keys = ["d"]
            elif [4,29] not in state['game'] and [5,29] not in state['game'] and [6,29] not in state['game'] and [7,29] not in state['game'] and [4,28] not in state['game'] and [7,28] not in state['game']:
                keys = ["d","d"]
            elif [5,29] not in state['game'] and [6,29] not in state['game'] and [7,29] not in state['game'] and [8,29] not in state['game'] and [5,28] not in state['game'] and [8,28] not in state['game']:#FIM I NORMAL 
                keys = ["d", "d","d"] 
            elif [1,29] not in state['game'] and [1,28] not in state['game'] and [1,27] not in state['game'] and [1,26] not in state['game']:
                keys = ["w", "a", "a", "a"]
            elif [2,29] not in state['game'] and [2,28] not in state['game'] and [2,27] not in state['game'] and [2,26] not in state['game']:
                keys = ["w", "a", "a"]
            elif [3,29] not in state['game'] and [3,28] not in state['game'] and [3,27] not in state['game'] and [3,26] not in state['game']:
                keys = ["w", "a"]
            elif [4,29] not in state['game'] and [4,28] not in state['game'] and [4,27] not in state['game'] and [4,26] not in state['game']:
                keys = ["w"]
            elif [5,29] not in state['game'] and [5,28] not in state['game'] and [5,27] not in state['game'] and [5,26] not in state['game']:
                keys = ["w", "d",]
            elif [6,29] not in state['game'] and [6,28] not in state['game'] and [6,27] not in state['game'] and [6,26] not in state['game']:
                keys = ["w", "d", "d"]
            elif [7,29] not in state['game'] and [7,28] not in state['game'] and [7,27] not in state['game'] and [7,26] not in state['game']:
                keys = ["w", "d", "d", "d"]
            elif [8,29] not in state['game'] and [8,28] not in state['game'] and [8,27] not in state['game'] and [8,26] not in state['game']: #fim I primeira camada
                keys = ["w", "d", "d" ,"d" ,"d"]

                #### 1I camada -------------


            elif [1,28] not in state['game'] and [2,28] not in state['game'] and [3,28] not in state['game'] and [4,28] not in state['game'] and [1,27] not in state['game'] and [4,27] not in state['game']:
                keys = ["a", "a", "a", "a"]
            elif [2,28] not in state['game'] and [3,28] not in state['game'] and [4,28] not in state['game'] and [5,28] not in state['game'] and [2,27] not in state['game'] and [5,27] not in state['game']:
                keys = []
            elif [3,28] not in state['game'] and [4,28] not in state['game'] and [5,28] not in state['game'] and [6,28] not in state['game'] and [3,27] not in state['game'] and [6,27] not in state['game']:
                keys = ["d"]
            elif [4,28] not in state['game'] and [5,28] not in state['game'] and [6,28] not in state['game'] and [7,28] not in state['game'] and [4,27] not in state['game'] and [7,27] not in state['game']:
                keys = ["d","d"]
            elif [5,28] not in state['game'] and [6,28] not in state['game'] and [7,28] not in state['game'] and [8,28] not in state['game'] and [5,27] not in state['game'] and [8,27] not in state['game']:  #fim  I normal
                keys = ["d", "d","d"] 
            elif [1,28] not in state['game'] and [1,27] not in state['game'] and [1,26] not in state['game'] and [1,25] not in state['game']:
                keys = ["w", "a", "a", "a"]
            elif [2,28] not in state['game'] and [2,27] not in state['game'] and [2,26] not in state['game'] and [2,25] not in state['game']:
                keys = ["w", "a", "a"]
            elif [3,28] not in state['game'] and [3,27] not in state['game'] and [3,26] not in state['game'] and [3,25] not in state['game']:
                keys = ["w", "a"]
            elif [4,28] not in state['game'] and [4,27] not in state['game'] and [4,26] not in state['game'] and [4,25] not in state['game']:
                keys = ["w"]
            elif [5,28] not in state['game'] and [5,27] not in state['game'] and [5,26] not in state['game'] and [5,25] not in state['game']:
                keys = ["w", "d",]
            elif [6,28] not in state['game'] and [6,27] not in state['game'] and [6,26] not in state['game'] and [6,25] not in state['game']:
                keys = ["w", "d", "d"]
            elif [7,28] not in state['game'] and [7,27] not in state['game'] and [7,26] not in state['game'] and [7,25] not in state['game']:
                keys = ["w", "d", "d", "d"]
            elif [8,28] not in state['game'] and [8,27] not in state['game'] and [8,26] not in state['game'] and [8,25] not in state['game']: #fim I 2 camada
                keys = ["w", "d", "d" ,"d" ,"d"]

                #### 2I camada -------------


            elif [1,27] not in state['game'] and [2,27] not in state['game'] and [3,27] not in state['game'] and [4,27] not in state['game'] and [1,26] not in state['game'] and [4,26] not in state['game']:
                keys = ["a", "a", "a", "a"]
            elif [2,27] not in state['game'] and [3,27] not in state['game'] and [4,27] not in state['game'] and [5,27] not in state['game'] and [2,26] not in state['game'] and [5,26] not in state['game']:
                keys = []
            elif [3,27] not in state['game'] and [4,27] not in state['game'] and [5,27] not in state['game'] and [6,27] not in state['game'] and [3,26] not in state['game'] and [6,26] not in state['game']:
                keys = ["d"]
            elif [4,27] not in state['game'] and [5,27] not in state['game'] and [6,27] not in state['game'] and [7,27] not in state['game'] and [4,26] not in state['game'] and [7,26] not in state['game']:
                keys = ["d","d"]
            elif [5,27] not in state['game'] and [6,27] not in state['game'] and [7,27] not in state['game'] and [8,27] not in state['game'] and [5,26] not in state['game'] and [8,26] not in state['game']: #fim I normal 
                keys = ["d", "d","d"] 
            elif [1,27] not in state['game'] and [1,26] not in state['game'] and [1,25] not in state['game'] and [1,24] not in state['game']:
                keys = ["w", "a", "a", "a"]
            elif [2,27] not in state['game'] and [2,26] not in state['game'] and [2,25] not in state['game'] and [2,24] not in state['game']:
                keys = ["w", "a", "a"]
            elif [3,27] not in state['game'] and [3,26] not in state['game'] and [3,25] not in state['game'] and [3,24] not in state['game']:
                keys = ["w", "a"]
            elif [4,27] not in state['game'] and [4,26] not in state['game'] and [4,25] not in state['game'] and [4,24] not in state['game']:
                keys = ["w"]
            elif [5,27] not in state['game'] and [5,26] not in state['game'] and [5,25] not in state['game'] and [5,24] not in state['game']:
                keys = ["w", "d",]
            elif [6,27] not in state['game'] and [6,26] not in state['game'] and [6,25] not in state['game'] and [6,24] not in state['game']:
                keys = ["w", "d", "d"]
            elif [7,27] not in state['game'] and [7,26] not in state['game'] and [7,25] not in state['game'] and [7,24] not in state['game']:
                keys = ["w", "d", "d", "d"]
            elif [8,27] not in state['game'] and [8,26] not in state['game'] and [8,25] not in state['game'] and [8,24] not in state['game']: #fim I 3 camada
                keys = ["w", "d", "d" ,"d" ,"d"]

             #### 3I camada -------------


            elif [1,26] not in state['game'] and [2,26] not in state['game'] and [3,26] not in state['game'] and [4,26] not in state['game'] and [1,25] not in state['game'] and [4,25] not in state['game']:
                keys = ["a", "a", "a", "a"]
            elif [2,26] not in state['game'] and [3,26] not in state['game'] and [4,26] not in state['game'] and [5,26] not in state['game'] and [2,25] not in state['game'] and [5,25] not in state['game']:
                keys = []
            elif [3,26] not in state['game'] and [4,26] not in state['game'] and [5,26] not in state['game'] and [6,26] not in state['game'] and [3,25] not in state['game'] and [6,25] not in state['game']:
                keys = ["d"]
            elif [4,26] not in state['game'] and [5,26] not in state['game'] and [6,26] not in state['game'] and [7,26] not in state['game'] and [4,25] not in state['game'] and [7,25] not in state['game']:
                keys = ["d","d"]
            elif [5,26] not in state['game'] and [6,26] not in state['game'] and [7,26] not in state['game'] and [8,26] not in state['game'] and [5,25] not in state['game'] and [8,25] not in state['game']: #fim I normal 
                keys = ["d", "d","d"] 
            elif [1,26] not in state['game'] and [1,25] not in state['game'] and [1,24] not in state['game'] and [1,23] not in state['game']:
                keys = ["w", "a", "a", "a"]
            elif [2,26] not in state['game'] and [2,25] not in state['game'] and [2,24] not in state['game'] and [2,23] not in state['game']:
                keys = ["w", "a", "a"]
            elif [3,26] not in state['game'] and [3,25] not in state['game'] and [3,24] not in state['game'] and [3,23] not in state['game']:
                keys = ["w", "a"]
            elif [4,26] not in state['game'] and [4,25] not in state['game'] and [4,24] not in state['game'] and [4,23] not in state['game']:
                keys = ["w"]
            elif [5,26] not in state['game'] and [5,25] not in state['game'] and [5,24] not in state['game'] and [5,23] not in state['game']:
                keys = ["w", "d",]
            elif [6,26] not in state['game'] and [6,25] not in state['game'] and [6,24] not in state['game'] and [6,23] not in state['game']:
                keys = ["w", "d", "d"]
            elif [7,26] not in state['game'] and [7,25] not in state['game'] and [7,24] not in state['game'] and [7,23] not in state['game']:
                keys = ["w", "d", "d", "d"]
            elif [8,26] not in state['game'] and [8,25] not in state['game'] and [8,24] not in state['game'] and [8,23] not in state['game']: #fim I 3 camada
                keys = ["w", "d", "d" ,"d" ,"d"]
            
             #### 4I camada -------------


            elif [1,25] not in state['game'] and [2,25] not in state['game'] and [3,25] not in state['game'] and [4,25] not in state['game'] and [1,24] not in state['game'] and [4,24] not in state['game']:
                keys = ["a", "a", "a", "a"]
            elif [2,25] not in state['game'] and [3,25] not in state['game'] and [4,25] not in state['game'] and [5,25] not in state['game'] and [2,24] not in state['game'] and [5,24] not in state['game']:
                keys = []
            elif [3,25] not in state['game'] and [4,25] not in state['game'] and [5,25] not in state['game'] and [6,25] not in state['game'] and [3,24] not in state['game'] and [6,24] not in state['game']:
                keys = ["d"]
            elif [4,25] not in state['game'] and [5,25] not in state['game'] and [6,25] not in state['game'] and [7,25] not in state['game'] and [4,24] not in state['game'] and [7,24] not in state['game']:
                keys = ["d","d"]
            elif [5,25] not in state['game'] and [6,25] not in state['game'] and [7,25] not in state['game'] and [8,25] not in state['game'] and [5,24] not in state['game'] and [8,24] not in state['game']: #fim I normal 
                keys = ["d", "d","d"] 
            elif [1,25] not in state['game'] and [1,24] not in state['game'] and [1,23] not in state['game'] and [1,22] not in state['game']:
                keys = ["w", "a", "a", "a"]
            elif [2,25] not in state['game'] and [2,24] not in state['game'] and [2,23] not in state['game'] and [2,22] not in state['game']:
                keys = ["w", "a", "a"]
            elif [3,25] not in state['game'] and [3,24] not in state['game'] and [3,23] not in state['game'] and [3,22] not in state['game']:
                keys = ["w", "a"]
            elif [4,25] not in state['game'] and [4,24] not in state['game'] and [4,23] not in state['game'] and [4,22] not in state['game']:
                keys = ["w"]
            elif [5,25] not in state['game'] and [5,24] not in state['game'] and [5,23] not in state['game'] and [5,22] not in state['game']:
                keys = ["w", "d",]
            elif [6,25] not in state['game'] and [6,24] not in state['game'] and [6,23] not in state['game'] and [6,22] not in state['game']:
                keys = ["w", "d", "d"]
            elif [7,25] not in state['game'] and [7,24] not in state['game'] and [7,23] not in state['game'] and [7,22] not in state['game']:
                keys = ["w", "d", "d", "d"]
            elif [8,25] not in state['game'] and [8,24] not in state['game'] and [8,23] not in state['game'] and [8,22] not in state['game']: #fim I 3 camada
                keys = ["w", "d", "d" ,"d" ,"d"]
            
             #### 5I camada -------------


            elif [1,24] not in state['game'] and [2,24] not in state['game'] and [3,24] not in state['game'] and [4,24] not in state['game'] and [1,23] not in state['game'] and [4,23] not in state['game']:
                keys = ["a", "a", "a", "a"]
            elif [2,24] not in state['game'] and [3,24] not in state['game'] and [4,24] not in state['game'] and [5,24] not in state['game'] and [2,23] not in state['game'] and [5,23] not in state['game']:
                keys = []
            elif [3,24] not in state['game'] and [4,24] not in state['game'] and [5,24] not in state['game'] and [6,24] not in state['game'] and [3,23] not in state['game'] and [6,23] not in state['game']:
                keys = ["d"]
            elif [4,24] not in state['game'] and [5,24] not in state['game'] and [6,24] not in state['game'] and [7,24] not in state['game'] and [4,23] not in state['game'] and [7,23] not in state['game']:
                keys = ["d","d"]
            elif [5,24] not in state['game'] and [6,24] not in state['game'] and [7,24] not in state['game'] and [8,24] not in state['game'] and [5,23] not in state['game'] and [8,23] not in state['game']: #fim I normal 
                keys = ["d", "d","d"] 
            elif [1,24] not in state['game'] and [1,23] not in state['game'] and [1,22] not in state['game'] and [1,21] not in state['game']:
                keys = ["w", "a", "a", "a"]
            elif [2,24] not in state['game'] and [2,23] not in state['game'] and [2,22] not in state['game'] and [2,21] not in state['game']:
                keys = ["w", "a", "a"]
            elif [3,24] not in state['game'] and [3,23] not in state['game'] and [3,22] not in state['game'] and [3,21] not in state['game']:
                keys = ["w", "a"]
            elif [4,24] not in state['game'] and [4,23] not in state['game'] and [4,22] not in state['game'] and [4,21] not in state['game']:
                keys = ["w"]
            elif [5,24] not in state['game'] and [5,23] not in state['game'] and [5,22] not in state['game'] and [5,21] not in state['game']:
                keys = ["w", "d",]
            elif [6,24] not in state['game'] and [6,23] not in state['game'] and [6,22] not in state['game'] and [6,21] not in state['game']:
                keys = ["w", "d", "d"]
            elif [7,24] not in state['game'] and [7,23] not in state['game'] and [7,22] not in state['game'] and [7,21] not in state['game']:
                keys = ["w", "d", "d", "d"]
            elif [8,24] not in state['game'] and [8,23] not in state['game'] and [8,22] not in state['game'] and [8,21] not in state['game']: #fim I 3 camada
                keys = ["w", "d", "d" ,"d" ,"d"]
            
             #### 6I camada -------------


            elif [1,23] not in state['game'] and [2,23] not in state['game'] and [3,23] not in state['game'] and [4,23] not in state['game'] and [1,22] not in state['game'] and [4,22] not in state['game']:
                keys = ["a", "a", "a", "a"]
            elif [2,23] not in state['game'] and [3,23] not in state['game'] and [4,23] not in state['game'] and [5,23] not in state['game'] and [2,22] not in state['game'] and [5,22] not in state['game']:
                keys = []
            elif [3,23] not in state['game'] and [4,23] not in state['game'] and [5,23] not in state['game'] and [6,23] not in state['game'] and [3,22] not in state['game'] and [6,22] not in state['game']:
                keys = ["d"]
            elif [4,23] not in state['game'] and [5,23] not in state['game'] and [6,23] not in state['game'] and [7,23] not in state['game'] and [4,22] not in state['game'] and [7,22] not in state['game']:
                keys = ["d","d"]
            elif [5,23] not in state['game'] and [6,23] not in state['game'] and [7,23] not in state['game'] and [8,23] not in state['game'] and [5,22] not in state['game'] and [8,22] not in state['game']: #fim I normal 
                keys = ["d", "d","d"] 
            elif [1,23] not in state['game'] and [1,22] not in state['game'] and [1,21] not in state['game'] and [1,20] not in state['game']:
                keys = ["w", "a", "a", "a"]
            elif [2,23] not in state['game'] and [2,22] not in state['game'] and [2,21] not in state['game'] and [2,20] not in state['game']:
                keys = ["w", "a", "a"]
            elif [3,23] not in state['game'] and [3,22] not in state['game'] and [3,21] not in state['game'] and [3,20] not in state['game']:
                keys = ["w", "a"]
            elif [4,23] not in state['game'] and [4,22] not in state['game'] and [4,21] not in state['game'] and [4,20] not in state['game']:
                keys = ["w"]
            elif [5,23] not in state['game'] and [5,22] not in state['game'] and [5,21] not in state['game'] and [5,20] not in state['game']:
                keys = ["w", "d",]
            elif [6,23] not in state['game'] and [6,22] not in state['game'] and [6,21] not in state['game'] and [6,20] not in state['game']:
                keys = ["w", "d", "d"]
            elif [7,23] not in state['game'] and [7,22] not in state['game'] and [7,21] not in state['game'] and [7,20] not in state['game']:
                keys = ["w", "d", "d", "d"]
            elif [8,23] not in state['game'] and [8,22] not in state['game'] and [8,21] not in state['game'] and [8,20] not in state['game']: #fim I 3 camada
                keys = ["w", "d", "d" ,"d" ,"d"]
            else:
                keys = []
    elif peca(state) == "S":
        if state['game'] == []:
            keys = ["w", "d", "d", "d"]
        else:
            if [8,28] not in state['game'] and [7,28] not in state['game'] and [7,29] not in state['game'] and [6,29] not in state['game'] and [6,28] not in state['game'] and [8,27] not in state['game']:
                keys = ["w", "d", "d", "d"]
            elif [7,28] not in state['game'] and [6,28] not in state['game'] and [6,29] not in state['game'] and [5,29] not in state['game'] and [5,28] not in state['game'] and [7,27] not in state['game']: 
                keys = ["w","d", "d"]
            elif [6,28] not in state['game'] and [5,28] not in state['game'] and [5,29] not in state['game'] and [4,29] not in state['game'] and [4,28] not in state['game'] and [6,27] not in state['game']: 
                keys = ["w","d"]
            elif [5,28] not in state['game'] and [4,28] not in state['game'] and [4,29] not in state['game'] and [3,29] not in state['game'] and [3,28] not in state['game'] and [5,27] not in state['game']:
                keys = ["w"]
            elif [4,28] not in state['game'] and [3,28] not in state['game'] and [3,29] not in state['game'] and [2,29] not in state['game'] and [2,28] not in state['game'] and [4,27] not in state['game']:
                keys = ["w", "a"]
            elif [3,28] not in state['game'] and [2,28] not in state['game'] and [2,29] not in state['game'] and [1,29] not in state['game'] and [1,28] not in state['game'] and [3,27] not in state['game']:#fim S rodado
                keys = ["w", "a", "a"]
            elif [1,28] not in state['game'] and [1,27] not in state['game'] and [2,28] not in state['game'] and [2,29] not in state['game'] and [2,27] not in state['game'] and [2,26] not in state['game']:
                keys = ["a", "a", "a"]
            elif [2,28] not in state['game'] and [2,27] not in state['game'] and [3,28] not in state['game'] and [3,29] not in state['game'] and [3,27] not in state['game'] and [3,26] not in state['game']: 
                keys = ["a", "a"]
            elif [3,28] not in state['game'] and [3,27] not in state['game'] and [4,28] not in state['game'] and [4,29] not in state['game'] and [4,27] not in state['game'] and [4,26] not in state['game']:
                keys = ["a"]
            elif [4,28] not in state['game'] and [4,27] not in state['game'] and [5,28] not in state['game'] and [5,29] not in state['game'] and [5,27] not in state['game'] and [5,26] not in state['game']: 
                keys = []
            elif [5,28] not in state['game'] and [5,27] not in state['game'] and [6,28] not in state['game'] and [6,29] not in state['game'] and [6,27] not in state['game'] and [6,26] not in state['game']: 
                keys = ["d"]
            elif [6,28] not in state['game'] and [6,27] not in state['game'] and [7,28] not in state['game'] and [7,29] not in state['game'] and [7,27] not in state['game'] and [7,26] not in state['game']: 
                keys = ["d", "d"]
            elif [7,28] not in state['game'] and [7,27] not in state['game'] and [8,28] not in state['game'] and [8,29] not in state['game'] and [8,27] not in state['game'] and [8,26] not in state['game']:#fim S normal
                keys = ["d", "d", "d"]

                ## 1S camada----------

            elif [8,27] not in state['game'] and [7,27] not in state['game'] and [7,28] not in state['game'] and [6,28] not in state['game'] and [6,27] not in state['game'] and [8,26] not in state['game']:
                keys = ["w", "d", "d", "d"]
            elif [7,27] not in state['game'] and [6,27] not in state['game'] and [6,28] not in state['game'] and [5,28] not in state['game'] and [5,27] not in state['game'] and [7,26] not in state['game']:
                keys = ["w","d", "d"]
            elif [6,27] not in state['game'] and [5,27] not in state['game'] and [5,28] not in state['game'] and [4,28] not in state['game'] and [4,27] not in state['game'] and [6,26] not in state['game']: 
                keys = ["w","d"]
            elif [5,27] not in state['game'] and [4,27] not in state['game'] and [4,28] not in state['game'] and [3,28] not in state['game'] and [3,27] not in state['game'] and [5,26] not in state['game']:
                keys = ["w"]
            elif [4,27] not in state['game'] and [3,27] not in state['game'] and [3,28] not in state['game'] and [2,28] not in state['game'] and [2,27] not in state['game'] and [4,26] not in state['game']:
                keys = ["w", "a"]
            elif [3,27] not in state['game'] and [2,27] not in state['game'] and [2,28] not in state['game'] and [1,28] not in state['game'] and [1,27] not in state['game'] and [3,26] not in state['game']: #fim S normal
                keys = ["w", "a", "a"]
            elif [1,27] not in state['game'] and [1,26] not in state['game'] and [2,27] not in state['game'] and [2,28] not in state['game'] and [2,26] not in state['game'] and [2,25] not in state['game']: 
                keys = ["a", "a", "a"]
            elif [2,27] not in state['game'] and [2,26] not in state['game'] and [3,27] not in state['game'] and [3,28] not in state['game'] and [3,26] not in state['game'] and [3,25] not in state['game']: 
                keys = ["a", "a"]
            elif [3,27] not in state['game'] and [3,26] not in state['game'] and [4,27] not in state['game'] and [4,28] not in state['game'] and [4,26] not in state['game'] and [4,25] not in state['game']:
                keys = ["a"]
            elif [4,27] not in state['game'] and [4,26] not in state['game'] and [5,27] not in state['game'] and [5,28] not in state['game'] and [5,26] not in state['game'] and [5,25] not in state['game']:
                keys = []
            elif [5,27] not in state['game'] and [5,26] not in state['game'] and [6,27] not in state['game'] and [6,28] not in state['game'] and [6,26] not in state['game'] and [6,25] not in state['game']:
                keys = ["d"]
            elif [6,27] not in state['game'] and [6,26] not in state['game'] and [7,27] not in state['game'] and [7,28] not in state['game'] and [7,26] not in state['game'] and [7,25] not in state['game']:
                keys = ["d", "d"]
            elif [7,27] not in state['game'] and [7,26] not in state['game'] and [8,27] not in state['game'] and [8,28] not in state['game'] and [8,26] not in state['game'] and [8,25] not in state['game']:#fim S rodado
                keys = ["d", "d", "d"]

                ## 2S camada----------

            elif [8,26] not in state['game'] and [7,26] not in state['game'] and [7,27] not in state['game'] and [6,27] not in state['game'] and [6,26] not in state['game'] and [8,25] not in state['game']: 
                keys = ["w", "d", "d", "d"]
            elif [7,26] not in state['game'] and [6,26] not in state['game'] and [6,27] not in state['game'] and [5,27] not in state['game'] and [5,26] not in state['game'] and [7,25] not in state['game']: 
                keys = ["w","d", "d"]
            elif [6,26] not in state['game'] and [5,26] not in state['game'] and [5,27] not in state['game'] and [4,27] not in state['game'] and [4,26] not in state['game'] and [6,25] not in state['game']:
                keys = ["w","d"]
            elif [5,26] not in state['game'] and [4,26] not in state['game'] and [4,27] not in state['game'] and [3,27] not in state['game'] and [3,26] not in state['game'] and [5,25] not in state['game']:
                keys = ["w"]
            elif [4,26] not in state['game'] and [3,26] not in state['game'] and [3,27] not in state['game'] and [2,27] not in state['game'] and [2,26] not in state['game'] and [4,25] not in state['game']:
                keys = ["w", "a"]
            elif [3,26] not in state['game'] and [2,26] not in state['game'] and [2,27] not in state['game'] and [1,27] not in state['game'] and [1,26] not in state['game'] and [3,25] not in state['game']: #fim S normal
                keys = ["w", "a", "a"]
            elif [1,26] not in state['game'] and [1,25] not in state['game'] and [2,26] not in state['game'] and [2,27] not in state['game'] and [2,25] not in state['game'] and [2,24] not in state['game']:
                keys = ["a", "a", "a"]
            elif [2,26] not in state['game'] and [2,25] not in state['game'] and [3,26] not in state['game'] and [3,27] not in state['game'] and [3,25] not in state['game'] and [3,24] not in state['game']: 
                keys = ["a", "a"]
            elif [3,26] not in state['game'] and [3,25] not in state['game'] and [4,26] not in state['game'] and [4,27] not in state['game'] and [4,25] not in state['game'] and [4,24] not in state['game']: 
                keys = ["a"]
            elif [4,26] not in state['game'] and [4,25] not in state['game'] and [5,26] not in state['game'] and [5,27] not in state['game'] and [5,25] not in state['game'] and [5,24] not in state['game']: 
                keys = []
            elif [5,26] not in state['game'] and [5,25] not in state['game'] and [6,26] not in state['game'] and [6,27] not in state['game'] and [6,25] not in state['game'] and [6,24] not in state['game']: 
                keys = ["d"]
            elif [6,26] not in state['game'] and [6,25] not in state['game'] and [7,26] not in state['game'] and [7,27] not in state['game'] and [7,25] not in state['game'] and [7,24] not in state['game']: 
                keys = ["d", "d"]
            elif [7,26] not in state['game'] and [7,25] not in state['game'] and [8,26] not in state['game'] and [8,27] not in state['game'] and [8,25] not in state['game'] and [8,24] not in state['game']: #fim S rodado
                keys = ["d", "d", "d"]

            ## 3S camada----------

            elif [8,25] not in state['game'] and [7,25] not in state['game'] and [7,26] not in state['game'] and [6,26] not in state['game'] and [6,25] not in state['game'] and [8,24] not in state['game']:
                keys = ["w", "d", "d", "d"]
            elif [7,25] not in state['game'] and [6,25] not in state['game'] and [6,26] not in state['game'] and [5,26] not in state['game'] and [5,25] not in state['game'] and [7,24] not in state['game']: 
                keys = ["w","d", "d"]
            elif [6,25] not in state['game'] and [5,25] not in state['game'] and [5,26] not in state['game'] and [4,26] not in state['game'] and [4,25] not in state['game'] and [6,24] not in state['game']:
                keys = ["w","d"]
            elif [5,25] not in state['game'] and [4,25] not in state['game'] and [4,26] not in state['game'] and [3,26] not in state['game'] and [3,25] not in state['game'] and [5,24] not in state['game']:
                keys = ["w"]
            elif [4,25] not in state['game'] and [3,25] not in state['game'] and [3,26] not in state['game'] and [2,26] not in state['game'] and [2,25] not in state['game'] and [4,24] not in state['game']:
                keys = ["w", "a"]
            elif [3,25] not in state['game'] and [2,25] not in state['game'] and [2,26] not in state['game'] and [1,26] not in state['game'] and [1,25] not in state['game'] and [3,24] not in state['game']: #fim S normal
                keys = ["w", "a", "a"]
            elif [1,25] not in state['game'] and [1,24] not in state['game'] and [2,25] not in state['game'] and [2,26] not in state['game'] and [2,24] not in state['game'] and [2,23] not in state['game']: 
                keys = ["a", "a", "a"]
            elif [2,25] not in state['game'] and [2,24] not in state['game'] and [3,25] not in state['game'] and [3,26] not in state['game'] and [3,24] not in state['game'] and [3,23] not in state['game']: 
                keys = ["a", "a"]
            elif [3,25] not in state['game'] and [3,24] not in state['game'] and [4,25] not in state['game'] and [4,26] not in state['game'] and [4,24] not in state['game'] and [4,23] not in state['game']: 
                keys = ["a"]
            elif [4,25] not in state['game'] and [4,24] not in state['game'] and [5,25] not in state['game'] and [5,26] not in state['game'] and [5,24] not in state['game'] and [5,23] not in state['game']: 
                keys = []
            elif [5,25] not in state['game'] and [5,24] not in state['game'] and [6,25] not in state['game'] and [6,26] not in state['game'] and [6,24] not in state['game'] and [6,23] not in state['game']: 
                keys = ["d"]
            elif [6,25] not in state['game'] and [6,24] not in state['game'] and [7,25] not in state['game'] and [7,26] not in state['game'] and [7,24] not in state['game'] and [7,23] not in state['game']: 
                keys = ["d", "d"]
            elif [7,25] not in state['game'] and [7,24] not in state['game'] and [8,25] not in state['game'] and [8,26] not in state['game'] and [8,24] not in state['game'] and [8,23] not in state['game']: #fim S rodado
                keys = ["d", "d", "d"]
            
            ## 4S camada----------

            elif [8,24] not in state['game'] and [7,24] not in state['game'] and [7,25] not in state['game'] and [6,25] not in state['game'] and [6,24] not in state['game'] and [8,23] not in state['game']: 
                keys = ["w", "d", "d", "d"]
            elif [7,24] not in state['game'] and [6,24] not in state['game'] and [6,25] not in state['game'] and [5,25] not in state['game'] and [5,24] not in state['game'] and [7,23] not in state['game']: 
                keys = ["w","d", "d"]
            elif [6,24] not in state['game'] and [5,24] not in state['game'] and [5,25] not in state['game'] and [4,25] not in state['game'] and [4,24] not in state['game'] and [6,23] not in state['game']:
                keys = ["w","d"]
            elif [5,24] not in state['game'] and [4,24] not in state['game'] and [4,25] not in state['game'] and [3,25] not in state['game'] and [3,24] not in state['game'] and [5,23] not in state['game']:
                keys = ["w"]
            elif [4,24] not in state['game'] and [3,24] not in state['game'] and [3,25] not in state['game'] and [2,25] not in state['game'] and [2,24] not in state['game'] and [4,23] not in state['game']:
                keys = ["w", "a"]
            elif [3,24] not in state['game'] and [2,24] not in state['game'] and [2,25] not in state['game'] and [1,25] not in state['game'] and [1,24] not in state['game'] and [3,23] not in state['game']: #fim S normal
                keys = ["w", "a", "a"]
            elif [1,24] not in state['game'] and [1,23] not in state['game'] and [2,24] not in state['game'] and [2,25] not in state['game'] and [2,23] not in state['game'] and [2,22] not in state['game']: 
                keys = ["a", "a", "a"]
            elif [2,24] not in state['game'] and [2,23] not in state['game'] and [3,24] not in state['game'] and [3,25] not in state['game'] and [3,23] not in state['game'] and [3,22] not in state['game']:
                keys = ["a", "a"]
            elif [3,24] not in state['game'] and [3,23] not in state['game'] and [4,24] not in state['game'] and [4,25] not in state['game'] and [4,23] not in state['game'] and [4,22] not in state['game']: 
                keys = ["a"]
            elif [4,24] not in state['game'] and [4,23] not in state['game'] and [5,24] not in state['game'] and [5,25] not in state['game'] and [5,23] not in state['game'] and [5,22] not in state['game']: 
                keys = []
            elif [5,24] not in state['game'] and [5,23] not in state['game'] and [6,24] not in state['game'] and [6,25] not in state['game'] and [6,23] not in state['game'] and [6,22] not in state['game']:
                keys = ["d"]
            elif [6,24] not in state['game'] and [6,23] not in state['game'] and [7,24] not in state['game'] and [7,25] not in state['game'] and [7,23] not in state['game'] and [7,22] not in state['game']:
                keys = ["d", "d"]
            elif [7,24] not in state['game'] and [7,23] not in state['game'] and [8,24] not in state['game'] and [8,25] not in state['game'] and [8,23] not in state['game'] and [8,22] not in state['game']: #fim S rodado
                keys = ["d", "d", "d"]
            
            ## 5S camada----------

            elif [8,23] not in state['game'] and [7,23] not in state['game'] and [7,24] not in state['game'] and [6,24] not in state['game'] and [6,23] not in state['game'] and [8,22] not in state['game']:
                keys = ["w", "d", "d", "d"]
            elif [7,23] not in state['game'] and [6,23] not in state['game'] and [6,24] not in state['game'] and [5,24] not in state['game'] and [5,23] not in state['game'] and [7,22] not in state['game']:
                keys = ["w","d", "d"]
            elif [6,23] not in state['game'] and [5,23] not in state['game'] and [5,24] not in state['game'] and [4,24] not in state['game'] and [4,23] not in state['game'] and [6,22] not in state['game']: 
                keys = ["w","d"]
            elif [5,23] not in state['game'] and [4,23] not in state['game'] and [4,24] not in state['game'] and [3,24] not in state['game'] and [3,23] not in state['game'] and [5,22] not in state['game']:
                keys = ["w"]
            elif [4,23] not in state['game'] and [3,23] not in state['game'] and [3,24] not in state['game'] and [2,24] not in state['game'] and [2,23] not in state['game'] and [4,22] not in state['game']:
                keys = ["w", "a"]
            elif [3,23] not in state['game'] and [2,23] not in state['game'] and [2,24] not in state['game'] and [1,24] not in state['game'] and [1,23] not in state['game'] and [3,22] not in state['game']: #fim S normal
                keys = ["w", "a", "a"]
            elif [1,23] not in state['game'] and [1,22] not in state['game'] and [2,23] not in state['game'] and [2,24] not in state['game'] and [2,22] not in state['game'] and [2,21] not in state['game']: 
                keys = ["a", "a", "a"]
            elif [2,23] not in state['game'] and [2,22] not in state['game'] and [3,23] not in state['game'] and [3,24] not in state['game'] and [3,22] not in state['game'] and [3,21] not in state['game']: 
                keys = ["a", "a"]
            elif [3,23] not in state['game'] and [3,22] not in state['game'] and [4,23] not in state['game'] and [4,24] not in state['game'] and [4,22] not in state['game'] and [4,21] not in state['game']: 
                keys = ["a"]
            elif [4,23] not in state['game'] and [4,22] not in state['game'] and [5,23] not in state['game'] and [5,24] not in state['game'] and [5,22] not in state['game'] and [5,21] not in state['game']:
                keys = []
            elif [5,23] not in state['game'] and [5,22] not in state['game'] and [6,23] not in state['game'] and [6,24] not in state['game'] and [6,22] not in state['game'] and [6,21] not in state['game']: 
                keys = ["d"]
            elif [6,23] not in state['game'] and [6,22] not in state['game'] and [7,23] not in state['game'] and [7,24] not in state['game'] and [7,22] not in state['game'] and [7,21] not in state['game']: 
                keys = ["d", "d"]
            elif [7,23] not in state['game'] and [7,22] not in state['game'] and [8,23] not in state['game'] and [8,24] not in state['game'] and [8,22] not in state['game'] and [8,21] not in state['game']: #fim S rodado
                keys = ["d", "d", "d"]

            ## 6S camada----------

            elif [8,22] not in state['game'] and [7,22] not in state['game'] and [7,23] not in state['game'] and [6,23] not in state['game'] and [6,22] not in state['game'] and [8,21] not in state['game']: 
                keys = ["w", "d", "d", "d"]
            elif [7,22] not in state['game'] and [6,22] not in state['game'] and [6,23] not in state['game'] and [5,23] not in state['game'] and [5,22] not in state['game'] and [7,21] not in state['game']: 
                keys = ["w","d", "d"]
            elif [6,22] not in state['game'] and [5,22] not in state['game'] and [5,23] not in state['game'] and [4,23] not in state['game'] and [4,22] not in state['game'] and [6,21] not in state['game']: 
                keys = ["w","d"]
            elif [5,22] not in state['game'] and [4,22] not in state['game'] and [4,23] not in state['game'] and [3,23] not in state['game'] and [3,22] not in state['game'] and [5,21] not in state['game']:
                keys = ["w"]
            elif [4,22] not in state['game'] and [3,22] not in state['game'] and [3,23] not in state['game'] and [2,23] not in state['game'] and [2,22] not in state['game'] and [4,21] not in state['game']:
                keys = ["w", "a"]
            elif [3,22] not in state['game'] and [2,22] not in state['game'] and [2,23] not in state['game'] and [1,23] not in state['game'] and [1,22] not in state['game'] and [3,21] not in state['game']: #fim S normal
                keys = ["w", "a", "a"]
            elif [1,22] not in state['game'] and [1,21] not in state['game'] and [2,22] not in state['game'] and [2,23] not in state['game'] and [2,21] not in state['game'] and [2,20] not in state['game']: 
                keys = ["a", "a", "a"]
            elif [2,22] not in state['game'] and [2,21] not in state['game'] and [3,22] not in state['game'] and [3,23] not in state['game'] and [3,21] not in state['game'] and [3,20] not in state['game']: 
                keys = ["a", "a"]
            elif [3,22] not in state['game'] and [3,21] not in state['game'] and [4,22] not in state['game'] and [4,23] not in state['game'] and [4,21] not in state['game'] and [4,20] not in state['game']: 
                keys = ["a"]
            elif [4,22] not in state['game'] and [4,21] not in state['game'] and [5,22] not in state['game'] and [5,23] not in state['game'] and [5,21] not in state['game'] and [5,20] not in state['game']:
                keys = []
            elif [5,22] not in state['game'] and [5,21] not in state['game'] and [6,22] not in state['game'] and [6,23] not in state['game'] and [6,21] not in state['game'] and [6,20] not in state['game']: 
                keys = ["d"]
            elif [6,22] not in state['game'] and [6,21] not in state['game'] and [7,22] not in state['game'] and [7,23] not in state['game'] and [7,21] not in state['game'] and [7,20] not in state['game']: 
                keys = ["d", "d"]
            elif [7,22] not in state['game'] and [7,21] not in state['game'] and [8,22] not in state['game'] and [8,23] not in state['game'] and [8,21] not in state['game'] and [8,20] not in state['game']: #fim S rodado
                keys = ["d", "d", "d"]

            else:
                keys = []
    elif peca(state) == "Z":
        if state['game'] == []:
            keys = ["w", "a", "a", "a"]
        else:
            if [1,28] not in state['game'] and [2,28] not in state['game'] and [2,29] not in state['game'] and [3,29] not in state['game']:
                keys = ["w", "a", "a"]
            elif [2,28] not in state['game'] and [3,28] not in state['game'] and [3,29] not in state['game'] and [4,29] not in state['game']:
                keys = ["w", "a"]
            elif [3,28] not in state['game'] and [4,28] not in state['game'] and [4,29] not in state['game'] and [5,29] not in state['game']:
                keys = ["w"]
            elif [4,28] not in state['game'] and [5,28] not in state['game'] and [5,29] not in state['game'] and [6,29] not in state['game']:
                keys = ["w", "d"]
            elif [5,28] not in state['game'] and [6,28] not in state['game'] and [6,29] not in state['game'] and [7,29] not in state['game']:
                keys = ["w", "d", "d"]
            elif [6,28] not in state['game'] and [7,28] not in state['game'] and [7,29] not in state['game'] and [8,29] not in state['game']: #fim z rodado 1 vez
                keys = ["w", "d", "d", "d"]
            elif [8,28] not in state['game'] and [8,27] not in state['game'] and [7,28] not in state['game'] and [7,29] not in state['game']: 
                keys = ["d", "d", "d", "d"]
            elif [7,28] not in state['game'] and [7,27] not in state['game'] and [6,28] not in state['game'] and [6,29] not in state['game']: 
                keys = ["d", "d", "d"]
            elif [6,28] not in state['game'] and [6,27] not in state['game'] and [5,28] not in state['game'] and [5,29] not in state['game']: 
                keys = ["d", "d"]
            elif [5,28] not in state['game'] and [5,27] not in state['game'] and [4,28] not in state['game'] and [4,29] not in state['game']: 
                keys = ["d"]
            elif [4,28] not in state['game'] and [4,27] not in state['game'] and [3,28] not in state['game'] and [3,29] not in state['game']: 
                keys = []
            elif [3,28] not in state['game'] and [3,27] not in state['game'] and [2,28] not in state['game'] and [2,29] not in state['game']: 
                keys = ["a"]
            elif [2,28] not in state['game'] and [2,27] not in state['game'] and [1,28] not in state['game'] and [1,29] not in state['game']: #fim z normal
                keys = ["a", "a"]

                ## 1Z camada ----------

            elif [1,27] not in state['game'] and [2,27] not in state['game'] and [2,28] not in state['game'] and [3,28] not in state['game']:
                keys = ["w", "a", "a"]
            elif [2,27] not in state['game'] and [3,27] not in state['game'] and [3,28] not in state['game'] and [4,28] not in state['game']:
                keys = ["w", "a"]
            elif [3,27] not in state['game'] and [4,27] not in state['game'] and [4,28] not in state['game'] and [5,28] not in state['game']:
                keys = ["w"]
            elif [4,27] not in state['game'] and [5,27] not in state['game'] and [5,28] not in state['game'] and [6,28] not in state['game']:
                keys = ["w", "d"]
            elif [5,27] not in state['game'] and [6,27] not in state['game'] and [6,28] not in state['game'] and [7,28] not in state['game']:
                keys = ["w", "d", "d"]
            elif [6,27] not in state['game'] and [7,27] not in state['game'] and [7,28] not in state['game'] and [8,28] not in state['game']: #fim z rodado 1 vez
                keys = ["w", "d", "d", "d"]
            elif [8,27] not in state['game'] and [8,26] not in state['game'] and [7,27] not in state['game'] and [7,28] not in state['game']: 
                keys = ["d", "d", "d", "d"]
            elif [7,27] not in state['game'] and [7,26] not in state['game'] and [6,27] not in state['game'] and [6,28] not in state['game']: 
                keys = ["d", "d", "d"]
            elif [6,27] not in state['game'] and [6,26] not in state['game'] and [5,27] not in state['game'] and [5,28] not in state['game']: 
                keys = ["d", "d"]
            elif [5,27] not in state['game'] and [5,26] not in state['game'] and [4,27] not in state['game'] and [4,28] not in state['game']: 
                keys = ["d"]
            elif [4,27] not in state['game'] and [4,26] not in state['game'] and [3,27] not in state['game'] and [3,28] not in state['game']: 
                keys = []
            elif [3,27] not in state['game'] and [3,26] not in state['game'] and [2,27] not in state['game'] and [2,28] not in state['game']: 
                keys = ["a"]
            elif [2,27] not in state['game'] and [2,26] not in state['game'] and [1,27] not in state['game'] and [1,28] not in state['game']: #fim z normal
                keys = ["a", "a"]

                ## 2Z camada ----------

            elif [1,26] not in state['game'] and [2,26] not in state['game'] and [2,27] not in state['game'] and [3,27] not in state['game']:
                keys = ["w", "a", "a"]
            elif [2,26] not in state['game'] and [3,26] not in state['game'] and [3,27] not in state['game'] and [4,27] not in state['game']:
                keys = ["w", "a"]
            elif [3,26] not in state['game'] and [4,26] not in state['game'] and [4,27] not in state['game'] and [5,27] not in state['game']:
                keys = ["w"]
            elif [4,26] not in state['game'] and [5,26] not in state['game'] and [5,27] not in state['game'] and [6,27] not in state['game']:
                keys = ["w", "d"]
            elif [5,26] not in state['game'] and [6,26] not in state['game'] and [6,27] not in state['game'] and [7,27] not in state['game']:
                keys = ["w", "d", "d"]
            elif [6,26] not in state['game'] and [7,26] not in state['game'] and [7,27] not in state['game'] and [8,27] not in state['game']: #fim z rodado 1 vez
                keys = ["w", "d", "d", "d"]
            elif [8,26] not in state['game'] and [8,25] not in state['game'] and [7,26] not in state['game'] and [7,27] not in state['game']: 
                keys = ["d", "d", "d", "d"]
            elif [7,26] not in state['game'] and [7,25] not in state['game'] and [6,26] not in state['game'] and [6,27] not in state['game']: 
                keys = ["d", "d", "d"]
            elif [6,26] not in state['game'] and [6,25] not in state['game'] and [5,26] not in state['game'] and [5,27] not in state['game']: 
                keys = ["d", "d"]
            elif [5,26] not in state['game'] and [5,25] not in state['game'] and [4,26] not in state['game'] and [4,27] not in state['game']: 
                keys = ["d"]
            elif [4,26] not in state['game'] and [4,25] not in state['game'] and [3,26] not in state['game'] and [3,27] not in state['game']: 
                keys = []
            elif [3,26] not in state['game'] and [3,25] not in state['game'] and [2,26] not in state['game'] and [2,27] not in state['game']: 
                keys = ["a"]
            elif [2,26] not in state['game'] and [2,25] not in state['game'] and [1,26] not in state['game'] and [1,27] not in state['game']: #fim z normal
                keys = ["a", "a"]
                
            ## 3Z camada ----------

            elif [1,25] not in state['game'] and [2,25] not in state['game'] and [2,26] not in state['game'] and [3,26] not in state['game']:
                keys = ["w", "a", "a"]
            elif [2,25] not in state['game'] and [3,25] not in state['game'] and [3,26] not in state['game'] and [4,26] not in state['game']:
                keys = ["w", "a"]
            elif [3,25] not in state['game'] and [4,25] not in state['game'] and [4,26] not in state['game'] and [5,26] not in state['game']:
                keys = ["w"]
            elif [4,25] not in state['game'] and [5,25] not in state['game'] and [5,26] not in state['game'] and [6,26] not in state['game']:
                keys = ["w", "d"]
            elif [5,25] not in state['game'] and [6,25] not in state['game'] and [6,26] not in state['game'] and [7,26] not in state['game']:
                keys = ["w", "d", "d"]
            elif [6,25] not in state['game'] and [7,25] not in state['game'] and [7,26] not in state['game'] and [8,26] not in state['game']: #fim z rodado 1 vez
                keys = ["w", "d", "d", "d"]
            elif [8,25] not in state['game'] and [8,24] not in state['game'] and [7,25] not in state['game'] and [7,26] not in state['game']: 
                keys = ["d", "d", "d", "d"]
            elif [7,25] not in state['game'] and [7,24] not in state['game'] and [6,25] not in state['game'] and [6,26] not in state['game']: 
                keys = ["d", "d", "d"]
            elif [6,25] not in state['game'] and [6,24] not in state['game'] and [5,25] not in state['game'] and [5,26] not in state['game']: 
                keys = ["d", "d"]
            elif [5,25] not in state['game'] and [5,24] not in state['game'] and [4,25] not in state['game'] and [4,26] not in state['game']: 
                keys = ["d"]
            elif [4,25] not in state['game'] and [4,24] not in state['game'] and [3,25] not in state['game'] and [3,26] not in state['game']: 
                keys = []
            elif [3,25] not in state['game'] and [3,24] not in state['game'] and [2,25] not in state['game'] and [2,26] not in state['game']: 
                keys = ["a"]
            elif [2,25] not in state['game'] and [2,24] not in state['game'] and [1,25] not in state['game'] and [1,26] not in state['game']: #fim z normal
                keys = ["a", "a"]
                
            ## 4Z camada ----------

            elif [1,24] not in state['game'] and [2,24] not in state['game'] and [2,25] not in state['game'] and [3,25] not in state['game']:
                keys = ["w", "a", "a"]
            elif [2,24] not in state['game'] and [3,24] not in state['game'] and [3,25] not in state['game'] and [4,25] not in state['game']:
                keys = ["w", "a"]
            elif [3,24] not in state['game'] and [4,24] not in state['game'] and [4,25] not in state['game'] and [5,25] not in state['game']:
                keys = ["w"]
            elif [4,24] not in state['game'] and [5,24] not in state['game'] and [5,25] not in state['game'] and [6,25] not in state['game']:
                keys = ["w", "d"]
            elif [5,24] not in state['game'] and [6,24] not in state['game'] and [6,25] not in state['game'] and [7,25] not in state['game']:
                keys = ["w", "d", "d"]
            elif [6,24] not in state['game'] and [7,24] not in state['game'] and [7,25] not in state['game'] and [8,25] not in state['game']: #fim z rodado 1 vez
                keys = ["w", "d", "d", "d"]
            elif [8,24] not in state['game'] and [8,23] not in state['game'] and [7,24] not in state['game'] and [7,25] not in state['game']: 
                keys = ["d", "d", "d", "d"]
            elif [7,24] not in state['game'] and [7,23] not in state['game'] and [6,24] not in state['game'] and [6,25] not in state['game']: 
                keys = ["d", "d", "d"]
            elif [6,24] not in state['game'] and [6,23] not in state['game'] and [5,24] not in state['game'] and [5,25] not in state['game']: 
                keys = ["d", "d"]
            elif [5,24] not in state['game'] and [5,23] not in state['game'] and [4,24] not in state['game'] and [4,25] not in state['game']: 
                keys = ["d"]
            elif [4,24] not in state['game'] and [4,23] not in state['game'] and [3,24] not in state['game'] and [3,25] not in state['game']: 
                keys = []
            elif [3,24] not in state['game'] and [3,23] not in state['game'] and [2,24] not in state['game'] and [2,25] not in state['game']: 
                keys = ["a"]
            elif [2,24] not in state['game'] and [2,23] not in state['game'] and [1,24] not in state['game'] and [1,25] not in state['game']: #fim z normal
                keys = ["a", "a"]
                  
            ## 5Z camada ----------

            elif [1,23] not in state['game'] and [2,23] not in state['game'] and [2,24] not in state['game'] and [3,24] not in state['game']:
                keys = ["w", "a", "a"]
            elif [2,23] not in state['game'] and [3,23] not in state['game'] and [3,24] not in state['game'] and [4,24] not in state['game']:
                keys = ["w", "a"]
            elif [3,23] not in state['game'] and [4,23] not in state['game'] and [4,24] not in state['game'] and [5,24] not in state['game']:
                keys = ["w"]
            elif [4,23] not in state['game'] and [5,23] not in state['game'] and [5,24] not in state['game'] and [6,24] not in state['game']:
                keys = ["w", "d"]
            elif [5,23] not in state['game'] and [6,23] not in state['game'] and [6,24] not in state['game'] and [7,24] not in state['game']:
                keys = ["w", "d", "d"]
            elif [6,23] not in state['game'] and [7,23] not in state['game'] and [7,24] not in state['game'] and [8,24] not in state['game']: #fim z rodado 1 vez
                keys = ["w", "d", "d", "d"]
            elif [8,23] not in state['game'] and [8,22] not in state['game'] and [7,23] not in state['game'] and [7,24] not in state['game']: 
                keys = ["d", "d", "d", "d"]
            elif [7,23] not in state['game'] and [7,22] not in state['game'] and [6,23] not in state['game'] and [6,24] not in state['game']: 
                keys = ["d", "d", "d"]
            elif [6,23] not in state['game'] and [6,22] not in state['game'] and [5,23] not in state['game'] and [5,24] not in state['game']: 
                keys = ["d", "d"]
            elif [5,23] not in state['game'] and [5,22] not in state['game'] and [4,23] not in state['game'] and [4,24] not in state['game']: 
                keys = ["d"]
            elif [4,23] not in state['game'] and [4,22] not in state['game'] and [3,23] not in state['game'] and [3,24] not in state['game']: 
                keys = []
            elif [3,23] not in state['game'] and [3,22] not in state['game'] and [2,23] not in state['game'] and [2,24] not in state['game']: 
                keys = ["a"]
            elif [2,23] not in state['game'] and [2,22] not in state['game'] and [1,23] not in state['game'] and [1,24] not in state['game']: #fim z normal
                keys = ["a", "a"]
                  
            ## 6Z camada ----------

            elif [1,22] not in state['game'] and [2,22] not in state['game'] and [2,23] not in state['game'] and [3,23] not in state['game']:
                keys = ["w", "a", "a"]
            elif [2,22] not in state['game'] and [3,22] not in state['game'] and [3,23] not in state['game'] and [4,23] not in state['game']:
                keys = ["w", "a"]
            elif [3,22] not in state['game'] and [4,22] not in state['game'] and [4,23] not in state['game'] and [5,23] not in state['game']:
                keys = ["w"]
            elif [4,22] not in state['game'] and [5,22] not in state['game'] and [5,23] not in state['game'] and [6,23] not in state['game']:
                keys = ["w", "d"]
            elif [5,22] not in state['game'] and [6,22] not in state['game'] and [6,23] not in state['game'] and [7,23] not in state['game']:
                keys = ["w", "d", "d"]
            elif [6,22] not in state['game'] and [7,22] not in state['game'] and [7,23] not in state['game'] and [8,23] not in state['game']: #fim z rodado 1 vez
                keys = ["w", "d", "d", "d"]
            elif [8,22] not in state['game'] and [8,21] not in state['game'] and [7,22] not in state['game'] and [7,23] not in state['game']: 
                keys = ["d", "d", "d", "d"]
            elif [7,22] not in state['game'] and [7,21] not in state['game'] and [6,22] not in state['game'] and [6,23] not in state['game']: 
                keys = ["d", "d", "d"]
            elif [6,22] not in state['game'] and [6,21] not in state['game'] and [5,22] not in state['game'] and [5,23] not in state['game']: 
                keys = ["d", "d"]
            elif [5,22] not in state['game'] and [5,21] not in state['game'] and [4,22] not in state['game'] and [4,23] not in state['game']: 
                keys = ["d"]
            elif [4,22] not in state['game'] and [4,21] not in state['game'] and [3,22] not in state['game'] and [3,23] not in state['game']: 
                keys = []
            elif [3,22] not in state['game'] and [3,21] not in state['game'] and [2,22] not in state['game'] and [2,23] not in state['game']: 
                keys = ["a"]
            elif [2,22] not in state['game'] and [2,21] not in state['game'] and [1,22] not in state['game'] and [1,23] not in state['game']: #fim z normal
                keys = ["a", "a"]

            else:
                keys = []
    else:
        keys = []
    return keys

def peca(state):
    if state['piece'] == [[3,3], [4,3], [3,4], [4,4]]:  #quadrado
        return "quadrado"
    elif state['piece'] == [[4,2], [4,3], [4,4], [5,4]]:  #L
        return "L"
    elif state['piece'] == [[4,2], [5,2], [4,3], [4,4]]:
        return "J"
    elif state['piece'] == [[4,2], [4,3], [5,3], [4,4]]:  #T
        return "T"
    elif state['piece'] == [[2,2], [3,2], [4,2], [5,2]]:  #I
        return "I"
    elif state['piece'] == [[4,2], [4,3], [5,3], [5,4]]:  #S
        return "S"
    elif state['piece'] == [[4, 2], [3, 3], [4, 3], [3, 4]]: #Z 
        return "Z"

def calculate_total_height(state):  
    
    columnHeights = []

    for column in range(0, 8):
        for row in range(0, 29):
            if state['game'][column][row] != []:
                columnHeights.append(30 - row)
                break
            elif row == 29:
                columnHeights.append(0)

    return columnHeights



         

        