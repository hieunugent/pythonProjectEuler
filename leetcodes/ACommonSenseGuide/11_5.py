from logging import root
from multiprocessing.sharedctypes import Value
from turtle import left


def func(row,col):
    if row ==1 or col == 1:
        return 1
    return func(row-1, col) + func(row, col-1)

def max(array):
    if len(array)== 1:
        return array[0]
    numMax = max(array[1:(len(array)-1)])
    if array[0] > numMax:
        return array[0]
    else:
        return numMax
def unique_paths(row, col):
    if row == 1 or col == 1:
        return 1
    return unique_paths(row-1, col) + unique_paths(row, col-1)

class BST:
    def __init__(self,left,right ) -> None:
        self.root = root
        self.left = left
        self.right = right
        
    def insert(node):
        if node < root:
            
        