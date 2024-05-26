class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
    
    def sorted_merge(self, a, b):
        if not a:
            return b
        if not b:
            return a
        
        if a.value <= b.value:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result

    def get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge_sort(self, h):
        if not h or not h.next:
            return h

        middle = self.get_middle(h)
        next_to_middle = middle.next

        middle.next = None

        left = self.merge_sort(h)
        right = self.merge_sort(next_to_middle)

        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    def sort(self):
        self.head = self.merge_sort(self.head)


# 1. Реверсування однозв'язного списку
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.print_list()  # Виведе: 1 -> 2 -> 3 -> 4 -> None
ll.reverse()
ll.print_list()  # Виведе: 4 -> 3 -> 2 -> 1 -> None

# 2. Алгоритм сортування для однозв'язного списку (сортування злиттям)
ll = LinkedList()
ll.append(4)
ll.append(2)
ll.append(1)
ll.append(3)
ll.print_list()  # Виведе: 4 -> 2 -> 1 -> 3 -> None
ll.sort()
ll.print_list()  # Виведе: 1 -> 2 -> 3 -> 4 -> None

# 3. Функція, що об'єднує два відсортовані однозв'язні списки
def merge_sorted_lists(l1, l2):
    dummy = Node()
    tail = dummy

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return dummy.next

ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)

ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)

merged_head = merge_sorted_lists(ll1.head, ll2.head)

current = merged_head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")  # Виведе: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
