from Node import Node

def main (table) :
    node = Node (table)

    return AstarAlgorithm (node)

def AstarAlgorithm (root_node , index = -1) :
    moves = root_node.checkMoves ()
    length = len (moves)

    if moves == dict () :
         if root_node.getWeight () == 8 :
             return root_node.getTable ()

         else :
            if root_node.getParent () != None :
                return root_node.getParent ()

    elif index < (-1 * length) :
        return root_node.getParent ()

    else :
        sorted_list = sorted (moves)
        state = AstarAlgorithm (root_node = moves [sorted_list [index]])

        if state == root_node :
           state = AstarAlgorithm (root_node = root_node , index = index - 1)

        if state == None :
            state = "There is no solution.!"

    return state

if __name__ == "__main__" :
    print (main ([4 , 1 , 3 , 2 , 8 , 5 , 7 , '*', 6]))