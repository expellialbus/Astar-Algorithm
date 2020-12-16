# Astar Algorithm

## This repository contain the implementation of Astar Algorithm.

> AstarAlgorithm.py file is the main file of the program.

You can run this file following command on your command line :

```
python3 AstarAlgorithm.py
```

Node.py file contain both node methods and control methods

**Such as :**

> calculateWeight

This method calculates the heuristic value of the table.

> checkMoves

This method checks the movable way on the table and it is also use **checkIndex** method to check whether this position of value which at the possible way its own position.

> createTable

This method create a table for each child of the node.
The table which has created by **createTable** method is represent one possible move from parent table.

> generateConnect

This method generate relation between parent and its childs.
