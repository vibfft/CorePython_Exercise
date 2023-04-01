class Node():
    # 20 => 7 => 13
    def __init__(self, data: str, next:str = None) -> None:
        self.data = data
        self.next = next
        

class LinkedList():
    
    def __init__(self) -> None:
        self.head = None
        
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head  # have new_node.next point to None
        self.head = new_node       # have self.head point to new_node
        
    def insert_after(self, prev_node, new_data):
        
        if prev_node is None:
            return "list has no previous node"
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def append(self, new_data):
        new_node = Node(new_data)
        
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            return
        
        tail = self.head
        while(tail.next):
            tail = tail.next
            
        print(f"data: {tail.data}")
        tail.next = new_node
        
    def print_list(self):
        
        temp = self.head
        while(temp):
            print(temp.data, end = " ")
            temp = temp.next
        print()
            
                
def main() -> None:
    
    llst = LinkedList()
  
    # Insert 6.  So linked list becomes 6->None
    llst.append(6)
  
    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llst.push(7)
  
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llst.push(1)
    
    llst.append(4)
    
    llst.push(10)
  
    llst.print_list()
    
if __name__ == '__main__':
    main() 