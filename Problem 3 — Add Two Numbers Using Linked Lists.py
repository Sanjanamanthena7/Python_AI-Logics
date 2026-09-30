class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_list(arr):
    head = None
    tail = None

    for x in arr:
        new_node = Node(x)

        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    return head


def add_numbers(l1, l2):
    dummy = Node(0)
    current = dummy
    carry = 0

    while l1 or l2:

        a = l1.data if l1 else 0
        b = l2.data if l2 else 0

        total = a + b + carry

        carry = total // 10
        digit = total % 10

        current.next = Node(digit)
        current = current.next

        if l1:
            l1 = l1.next

        if l2:
            l2 = l2.next

    if carry:
        current.next = Node(carry)

    return dummy.next


def print_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next


n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

l1 = create_list(a)
l2 = create_list(b)

answer = add_numbers(l1, l2)

print_list(answer)
