#from dataclasses import dataclass


class Snode:
    def __init__(self ,data):
        self.data = data
        self.next = None

class Slinklist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append_node(self ,data):
         if self.head == None:
             self.head = Snode(data)
             self.tail = self.head
         else:
             self.tail.next = Snode(data)
             self.tail = self.tail.next
         self.count += 1
    
    def search_node(self ,data):
        flag = False
        if self.head == None:
            print("the link list is empty.. ")
            return None
        else:
            temp = self.head
            while (temp != None) and (flag != True):
                if temp.data == data:
                    flag = True
                else:
                    temp = temp.next
            if flag == True:
                print("Found the node..")
                return temp
            else:
                print("The link list doesnt have the data : " + str(data))
                return None

    def delete_node(self ,data):
        del_node = self.search_node(data)
        if del_node != None:
            temp = self.head
            while temp.next != del_node:
                temp = temp.next
            temp.next = temp.next.next
            del(del_node)
            self.count -= 1
    
    def print_linklist(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
    
    def insert_node(self ,data ,index):
        temp = self.head
        if (index + 1) > self.count:
            print("The index is out of range ")
            print("Number of nodes present is " + str(self.count) + "Enter 1 if u want to append to the list" )
            check = input()
            if check == "1":
                self.append_node(data)
            else:
                print("could not able to add the data ")
        else:
            before = temp
            for i in range(index):
                before = temp
                temp = temp.next
            before.next = Snode(data)
            before.next.next = temp 

class Dnode:
    def __init__(self ,data):
        self.data = data
        self.before = None
        self.next = None

class Dlinklist(Slinklist):
    def __init__(self ,data):
        self.head = None
        self.tail = None
        self.count = 0

    def append_node(self ,data):
        if self.head == None:
            self.head = Dnode(data)
            self.tail = self.head
        else:
            self.tail.next = Dnode(data)
            self.tail.next.before = self.tail
            self.tail = self.tail.next
        self.count += 1
    
    def insert_node(self ,data ,index):
        temp = self.head
        if (index + 1) > self.count:
            print("The index is out of range ")
            print("Number of nodes present is " + str(self.count) + "Enter 1 if u want to append to the list" )
            check = input()
            if check == "1":
                self.append_node(data)
            else:
                print("could not able to add the data ")
        else:
            for i in range(index):
                temp = temp.next
            temp.before.next = Dnode(data)
            temp.before.next.before = temp.before
            temp.before = temp.before.next
            temp.before.next = temp
    
    def delete_node(self ,data):
        del_node = self.search_node(data)
        if del_node != None:
            del(del_node)
            self.count -= 1
