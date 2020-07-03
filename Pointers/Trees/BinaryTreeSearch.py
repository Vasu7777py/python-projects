
class Node:
    def __init__(self, Value):
        self.Right = None
        self.Left = None
        self.Value = Value
    
    def __repr__(self):
        return str(f"{self.Value}")

class Binary_Search_Tree:
    @classmethod
    def Create_BST(cls, root, List:list):
        for Value in List:
            if (root == None):
                root = Node(Value)
            else:
                cls.Insert_node(root, Value)
        return root
    
    @classmethod
    def Insert_node(cls, node, Value):
        if (Value <= node.Value):
            if (node.Left == None):
                node.Left = Node(Value)
            else:
                cls.Insert_node(node.Left, Value)
        else:
            if (node.Right == None):
                node.Right = Node(Value)
            else:
                cls.Insert_node(node.Right, Value)

    @classmethod
    def Display(cls, node:Node):
        if (node == None):
            return
        else:
            if (node.Left != None):
                cls.Display(node.Left)
            print(node, end = ", ")
            if (node.Right != None):
                cls.Display(node.Right)

def main():
    List = []
    for Index in range(int(input("Enter the sizr of the list : "))):
        List.append(float(input(f"Enter the value of the index {Index +1} : ")))

    root = Binary_Search_Tree.Create_BST(None, List)
    Binary_Search_Tree.Display(root)

if (__name__ == "__main__"):
    main()
