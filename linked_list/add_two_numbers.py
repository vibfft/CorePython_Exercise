# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class AddTwoNumbers:
    @staticmethod
    def add_two_numbers(l1: list[ListNode], l2: list[ListNode]) -> list[ListNode]:
        head = ListNode(0)
        curr = head
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            column_sum = l1_val + l2_val + carry
            print(f"L1: {l1_val}, L2: {l2_val}, sum: {column_sum}, carry: {carry}")

            carry = column_sum // 10  # only returns quotient
            print(f"carry: {carry}")

            new_node = ListNode(column_sum % 10)
            curr.next = new_node
            curr = new_node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next


def push(data, head):
    new_node = ListNode(data)

    if head:
        current = head
        while current.next:
            current = current.next
        current.next = new_node
    else:
        head = new_node


def main() -> None:
    head = ListNode(0)
    push(3, head)
    push(4, head)
    push(2, head)
    print(head.next)
    L1 = head.next

    head2 = ListNode(0)
    push(4, head2)
    push(6, head2)
    push(5, head2)
    L2 = head2.next

    a = AddTwoNumbers()
    head_next = a.add_two_numbers(L1, L2)
    while head_next:
        if head_next.next is not None:
            print(f"{head_next.val} => ", end='')
        else:
            print(f"{head_next.val}")
        head_next = head_next.next


if __name__ == '__main__':
    main()
