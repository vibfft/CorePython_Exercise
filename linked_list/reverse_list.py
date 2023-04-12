class ListNode():

    def __init__(self, data: str, next: str = None) -> None:
        self.data = data
        self.next = next


class LinkedList():

    def __init__(self) -> None:
        self.head = None

    def push(self, data: str) -> ListNode:
        new_node = ListNode(data)

        new_node.next = self.head
        self.head = new_node
        
        return self.head

    def show_nodes(self) -> None:

        current = self.head
        while current != None:
            if current.next != None:
                print(f"{current.data} => ", end="")
            else:
                print(f"{current.data}")
                
            current = current.next
            
def reverse_list(head_of_list: LinkedList) -> LinkedList:
        
    prev = None  # points to the new reversed list
    curr = head_of_list.head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        
    head_of_list.head = prev
    return head_of_list

def main() -> None:
    node = LinkedList()

    lst = node.push("3")
    print(f"lst: {type(lst)}")
    node.show_nodes()
    node.push("2")
    node.show_nodes()
    node.push("1")
    node.show_nodes()
    
    reversed_list = reverse_list(node)
    reversed_list.show_nodes()
    


if __name__ == '__main__':
    main()
