class Node () :
    def __init__ (self , table , index = None) :
        self.__table = table
        self.__index = index
        self.__weight = self.__calculateWeight ()
        self.__left_child = None
        self.__forward_child = None
        self.__right_child = None
        self.__parent = None

    def getTable (self) :
        return self.__table

    def getWeight (self) :
        return self.__weight

    def setWeight (self , weight) :
        self.__weight = weight

    def getLeftChild (self) :
        return self.__left_child

    def setLeftChild (self , left_child) :
        self.__left_child = left_child

    def getForwardChild (self) :
        return self.__forward_child

    def setForwardChild (self , forward_child) :
        self.__forward_child = forward_child

    def getRightChild (self) :
        return self.__right_child

    def setRightChild (self , right_child) :
        self.__right_child = right_child

    def getParent (self) :
        return self.__parent

    def setParent (self , parent) :
        self.__parent = parent

    def __calculateWeight (self) :
        count = 0

        for i in range (9) :
            if self.__table [i] == (i + 1) :
                count += 1

        return count

    def checkMoves (self) :
        index = self.__table.index ('*')
        nodes = dict ()
        left = None
        right = None
        forward = None

        if (index - 1) < len (self.__table) and (index - 1) > -1 and (index - 1) != self.__index and self.__checkIndex (index - 1) :
            left = Node (self.__createTable (index , (index - 1)) , index)
            nodes [left.getWeight ()] = left

            self.__generateConnect (left , "left")

        if (index + 1) < len (self.__table) and (index + 1) > -1 and (index + 1) != self.__index and self.__checkIndex (index + 1):
            right = Node (self.__createTable (index , (index + 1)) , index)
            nodes [right.getWeight ()] = right

            self.__generateConnect (right , "right")

        if (index + 3) < len (self.__table) and (index + 3) > -1 and (index + 3) != self.__index and self.__checkIndex (index + 3) :
            forward = Node (self.__createTable (index , (index + 3)) , index)
            nodes [forward.getWeight ()] = forward

            self.__generateConnect (forward , "forward")

        if (index - 3) < len (self.__table) and (index - 3) > -1 and (index - 3) != self.__index and self.__checkIndex (index - 3) :
            if left == None :
                left = Node (self.__createTable (index , (index - 3)) , index)
                nodes [left.getWeight ()] = left

                self.__generateConnect (left , "left")

            elif right == None :
                right = Node (self.__createTable (index , (index - 3)) , index)
                nodes [right.getWeight ()] = right

                self.__generateConnect (right , "right")

            elif forward == None :
                forward = Node (self.__createTable (index , (index - 3)) , index)
                nodes [forward.getWeight ()] = forward

                self.__generateConnect (forward , "forward")
        return nodes

    def __createTable (self , from_index , to_index) :
        table = [i for i in self.__table]

        table [from_index] , table [to_index] = table [to_index] , table [from_index]

        return table

    def __checkIndex (self , index) :
        if self.__table [index] == (index + 1) :
            return False

        else :
            return True

    def __generateConnect (self , child , name) :
        if name == "left" :
            self.__left_child = child
            child.setParent (self)

        elif name == "right" :
            self.__right_child = child
            child.setParent (self)

        else :
            self.__forward_child = child
            child.setParent (self)