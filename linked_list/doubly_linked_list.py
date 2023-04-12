class Node():
    
    def __init__(self, data: str, next: str = None, prev: str = None) -> None:
        self.data = data
        self.next = next
        self.prev = prev
        
        
class DoublyLinkedList():
    
    def __init__(self):
        self.next = None
        self.prev = None
        self.head = None
        
    def append_at_tail(self, data):
        
        if self.head is None:
            new_node = Node(data)
            self.next = None
            self.prev = None
            
        tail = self.head
        
        
    
    def insert_at_head(self, node):
        pass
    
    def remove_at_tail(self):
        pass
    
    def remove_at_head(self):
        pass
    
    def print_list_from_head(self):
        pass
    
    def print_list_from_tail(self):
        pass
        
        
        
        
        