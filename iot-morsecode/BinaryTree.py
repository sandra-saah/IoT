#The binary tree structure implemented by Sandra S

class BinaryTree():
    def __init__(self, root):
        self.root = root
        self.dot = None
        self.dash = None

    def get_left_child(self):
        return self.dot

    def get_right_child(self):
        return self.dash

    def set_node(self, value):
        self.root = value

    def get_node(self):
        return self.root

    def print_tree(tree, nest):
        if tree != None:
            for i in range(nest):
                print(" ", end="")
            print(tree.root)
            BinaryTree.print_tree(tree.dot, nest+1)
            BinaryTree.print_tree(tree.dash, nest+1)

    def insert_search(tree, letter, morse):
        if tree == None:
            return BinaryTree((letter, morse))
        else:
            if letter < tree.root[0]:
                tree.dot = BinaryTree.insert_search(tree.dot, letter, morse)
                return tree
            elif letter > tree.root[0]:
                tree.dash = BinaryTree.insert_search(tree.dash, letter, morse)
                return tree
            else:
                tree.root = (letter, morse)
                return tree

    
    def find_search(tree, letter):
        if tree == None:
            raise Exception("None Existant Letter.")
        else:
            if letter < tree.root[0]:
                return BinaryTree.find_search(tree.dot, letter)
            elif letter > tree.root[0]:
                return BinaryTree.find_search(tree.dash, letter)
            else:
                return tree.root[1]
    
    # two function to check if the binary tree is empty or not 
    
    def isTreeEmpty(self):
        if self.dot == None and self.dash == None:
            return True
        else:
            return False
    
    def isTreeNotEmpty(self):
        if self.dot != None or self.dash != None:
            return True
        else:
            return False


