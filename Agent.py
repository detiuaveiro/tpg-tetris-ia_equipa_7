from shape import Shape
import common


    
   

def next_key(state):

    pecas_sup = []
    pecas_sup.append(state['game'])
    print(pecas_sup)
    
    current_piece = peca(state)
    next_piece = prox_peca(state)


    superf_ocup = pecas_sup.pop(0)
    
    if current_piece == "quadrado": 
        key = "a"
    elif current_piece == "I":
        key = "d"
    else:
        key = ""
    return key

def prox_peca(state):
    peca = state['next_pieces'][0]
    if peca == [[3,3], [4,3], [3,4], [4,4]]:
        return "quadrado"
    elif peca == [[2,4], [3,4], [2,5], [3,5]]:
        return "L"
    elif peca == [[4,4], [5,4], [6,4], [7,4]]:
        return "I"

def peca(state):
    if state['piece'] == [[3,3], [4,3], [3,4], [4,4]]:  #quadrado
        return "quadrado"
    elif state['piece'] == [[2,4], [3,4], [2,5], [3,5]]:
        return "quadrado"
    elif state['piece'] == [[4,4], [5,4], [4,5], [5,5]]:
        return "quadrado"
    elif state['piece'] == [[4,2], [4,3], [4,4], [5,4]]:  #L
        return "L"
    elif state['piece'] == [[3,3], [3,4], [3,5], [4,5]]:
        return "L"
    elif state['piece'] == [[5,3], [5,4], [5,5], [6,5]]:
        return "L"
    elif state['piece'] == [[2,2], [3,2], [4,2], [5,2]]:  #I
        return "I"
    elif state['piece'] == [[3,3], [4,3], [5,3], [6,3]]:  #I
        return "I"
    elif state['piece'] == [[4,4], [5,4], [6,4], [7,4]]:  #I
        return "I"



        