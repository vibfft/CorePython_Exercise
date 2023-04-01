# Definition for singly-linked list.
# L1: ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}}, 
# L2: ListNode{val: 5, next: ListNode{val: 6, next: ListNode{val: 4, next: None}}}
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class AddTwoNumbers:
#     def addTwoNumbers(self, L1: list, L2: list) -> list:
        
#         dummyHead = ListNode(0)
#         curr = dummyHead
        
#         carry = 0
#         while L1 != None or L2 != None or carry != 0:
#             l1Val = l1.val if l1 else 0
#             l2Val = l2.val if l2 else 0
#             columnSum = l1Val + l2Val + carry
#             carry = columnSum // 10
#             newNode = ListNode(columnSum % 10)
#             curr.next = newNode
#             curr = newNode
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#         return dummyHead.next
class AddTwoNumbers:
    def addTwoNumbers(self, l1:list, l2:list) -> list:
        pass

def push(new_data, head):
    new_node = ListNode(new_data)
    new_node.next = head
    head = new_node
                
def main():
    
    head = ListNode(0)
    current = head
    for node in [3,4,2]:
        push(node,head)
    print(f"L1: {head}")    
    
if __name__ == '__main__':
    main()
            
            