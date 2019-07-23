class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    legth = 0
    
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.legth += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.legth +=1
    
    def insert_at(self, data, position):
        if position < 1 or position > self.legth:
            print('Invalid position')
            return

        if not self.head:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.legth += 1
            return
        
        current = self.head
        
        for i in range(1, position - 1):
            if not current.next:
                break
            current = current.next
        
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node    
        self.legth += 1   
    
    def get_size(self):
        return self.legth
    
    def remove_first(self):
        if not self.head:
            print('List is empty')
            return
        
        self.head = self.head.next         
    
    def remove_last(self):
        if not self.head:
            print('List is empty')
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        
        current.next = None
        self.legth -= 1

    def remove_at(self, position):
        print('remove at position {}'.format(position))
        if not self.head:
            print('List is empty')
            return
        
        if position < 1 or position > self.legth:
            print('Invalid position')
            return
        
        if position == 1:
            self.head = self.head.next
            
        current = self.head
        for i in range(1, position - 1):
            current = current.next
            
        current.next = current.next.next
        self.legth -= 1
        self.display()
    
    def display(self):
        if not self.head:
            print('List is empty')
            return
        
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print('\n')
        
if __name__ == '__main__':
    ll = LinkedList()
    # import unittest
    # class TestLinkedList(unittest.TestCase):
    #     def test_insert_at_start(ll.insert_at_start((10))
    ll.insert_at_end(11)
    ll.display()
    ll.insert_at(22, 1)
    ll.display()
    ll.insert_at(33, 1)
    ll.display()
    ll.insert_at(44, 2)
    ll.display()
    ll.insert_at(55, 2)
    ll.display()
    ll.insert_at(33, 2)
    # ll.display()
    # ll.insert_at_end(22)
    # ll.insert_at_end(33)
    # ll.insert_at_start(44)
    # ll.insert_at_start(55)
    # ll.insert_at_start(66)
    # ll.insert_at_end(77)
    # ll.insert_at_start(88)
    # print(ll.get_size())
    # ll.display()
    # # ll.remove_first()
    # # ll.display()
    # # ll.remove_last()
    # # ll.display()
    # # ll.remove_last()
    # # ll.display()
    # ll.remove_at(4)
    # # ll.display()
    # ll.remove_at(7)
    # print(ll.legth)

    # ll.remove_at(6)
    # print(ll.legth)

    # ll.insert_at(99, 5)