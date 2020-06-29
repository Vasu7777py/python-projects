
class Node:
    def __init__(self, Value = None, before = None):
        self.Value = Value
        self.next = None
        self.before = before
    
    def __repr__(self):
        RESULT = {"Value" : self.Value}
        return str(RESULT)

class LinkedList:
    def __init__(self, Name):
        self.Name = Name
        self.Size = 0
        self.Root = None
        
        self.creat_ll()
    
    def __repr__(self):
        RESULT = {
            "Name" : self.Name,
            "Size" : self.Size,
            "LinkList" : self.display()
        }
        return str(RESULT)

    def creat_ll(self):
        size = int(input("Enter the size of the LinkList : "))
        print("Enter the elements : ")
        for Index in range(size):
            Value = float(input(f"Enter the element of index {Index +1} : "))
            if (self.Root == None):
                self.Root = Node(Value)
            else:
                self.append(Value)
            self.Size += 1

    def append(self, Value):
        if (self.Root == None):
            return
        else:
            ptr = self.Root
        
        while (ptr.next != None):
            ptr = ptr.next
        
        ptr = Node(Value, ptr)
        ptr.before.next = ptr

    def display(self):
        List = []
        if (self.Root != None):
            ptr = self.Root
        else:
            return None
        
        while (ptr.next != None):
            List.append(ptr.Value)
            ptr = ptr.next
        
        return List
    
def main():
    ll = LinkedList("test")
    print(ll)

if (__name__ == "__main__"):
    main()
