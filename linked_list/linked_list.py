class Node():
    # 20 => 7 => 13
    def __init__(self, data: str, next:str) -> None:
        self.data = data
        self.next = None
        

class LinkedList():
    
    def __init__(self, data: str, next: str) -> None:
        self.head = data
        self.tail = self.head
        self.next = None
        
    def __str__(self):
        return self.head
        
    def append(self, data: str) -> list:
        pass
        
    
    def prepend(self) -> None:
        pass
    
    def insert(self) -> None:
        pass
    
    def remove(self) -> None:
        pass
    
def main() -> None:
    llst = LinkedList(20)
    print(f"llst: {llst}")    
    llst.append(7)
    
    
if __name__ == '__main__':
    main() 