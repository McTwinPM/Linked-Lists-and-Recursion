
class Node:
    

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
   
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        
        def recursive_sum_helper(node):
            if node is None:
                return 0
            return node.data + recursive_sum_helper(node.next)
        return recursive_sum_helper(self.head)


    def recursive_reverse(self):
        
        def recursive_reverse_helper(prev, current):
            if current is None:
                return prev
            next_node = current.next
            current.next = prev
            return recursive_reverse_helper(current, next_node)
        self.head = recursive_reverse_helper(None, self.head)

    def recursive_search(self, target):
        
        def recursive_search_helper(node, target):
            if node is None:
                return False
            if node.data == target:
                return True
            return recursive_search_helper(node.next, target)

        return recursive_search_helper(self.head, target)

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
