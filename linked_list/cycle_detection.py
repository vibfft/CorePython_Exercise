class ListNode():
    
    def __init__(self, data: str, next: str = None) -> None:
        self.data = data
        self.next = next
        
class LinkedList():
    
    def __init__(self):
        self.head = None
        
    def push_node(self, data) -> ListNode:
        
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node
        
        return new_node  
        
    def print_list(self):
        
        current = self.head
        index = 0
        while current:
            if index > 7:
                break
            if current.next:
                print(f"{current.data} => ", end="")
            else:
                print(f"{current.data}")
                
            current = current.next
            index += 1
            
def build_cycle(llst: LinkedList ) -> LinkedList:
    
    node_five = llst.push_node("5")
    node_four = llst.push_node("4")
    node_three = llst.push_node("3")
    node_two = llst.push_node("2")
    node_one = llst.push_node("1")
    
    node_five.next = node_three
    
    return llst

def detect_cycle(llst: LinkedList) -> bool:
    
    cycle_dict = {}
    current = llst.head
    while current:
        # print(f"current data: {current.data}")
        if current.data not in cycle_dict:
            cycle_dict[current.data] = False
        elif current.data in cycle_dict:
            return True   
        current = current.next
    return False 
        
def main() -> None:
    
    llst = LinkedList()
    llst.push_node("5")
    llst.push_node("4")
    llst.push_node("3")
    llst.push_node("2")
    llst.push_node("1")
    llst.print_list()
    
    cycle = build_cycle(LinkedList())
    print(type(cycle))
    cycle.print_list()
    
    print(f"\nis 'llst' linked-list cycle: {detect_cycle(llst)}")
    print(f"is 'cycle' linked-list cycle: {detect_cycle(cycle)}")
    
if __name__ == '__main__':
    main()
            