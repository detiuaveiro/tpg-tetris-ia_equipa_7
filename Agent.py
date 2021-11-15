from shape import Shape
import common


def next_key(state):

    
    if state["piece"] == [[3,3], [4,3], [3,4], [4,4]]:  #quadrado
        key = "a"
        quadrado_state = state["piece"]
        for i in range(len(quadrado_state)):   
            quadrado_state[i][0] -= 1
        for j in range(len(quadrado_state)):   
            quadrado_state[j][1] += 1
    # elif state["piece"] == quadrado_state:
    #     key = "a"
    else:
        key = ""
    return key

        