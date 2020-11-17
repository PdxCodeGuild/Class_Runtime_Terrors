

# https://www.programiz.com/python-programming/iterator

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
    
    def __str__(self):
        return f'({self.value},{self.next})'


# node_a = Node('a', None)
# print(node_a)

# node_b = Node('b', None)
# node_a.next = node_b

# node_c = Node('c', None)
# node_b.next = node_c

# node_d = Node('d', None)
# node_c.next = node_d

# node = node_a
# while node is not None:
#     print(node.value)
#     node = node.next

# class Stack:
#     def __init__(self):
#         self.elements = []
    
#     def push(self, value):
#         self.elements.append(value)
    
#     def pop(self):
#         if len(self.elements) == 0:
#             return None
#         element = self.elements.pop(len(self.elements)-1)
#         return element
    
#     def peek(self):
#         return self.elements[len(self.elements)-1]


# stack = Stack()
# stack.push('a')
# stack.push('b')
# stack.push('c')
# print(stack.peek()) # c
# print(stack.pop()) # c
# print(stack.pop()) # b
# print(stack.pop()) # a
# print(stack.pop()) # None

    




class Stack:
    def __init__(self):
        self.root = None
    
    def push(self, value):
        self.root = Node(value, self.root)
    
    def pop(self):
        if self.root is None:
            return None
        value = self.root.value
        self.root = self.root.next
        return value
    
    def peek(self):
        if self.root is None:
            return None
        return self.root.value
    
    def __str__(self):
        return str(self.root)
    
    def __len__(self):
        
        # node = node_a
        # while node is not None:
        #     print(node.value)
        #     node = node.next

        counter = 0
        node = self.root
        while node is not None:
            counter += 1
            node = node.next
        return counter
    
    def __getitem__(self, i):
        counter = 0
        node = self.root
        while node is not None:
            if counter == i:
                return node.value
            counter += 1
            node = node.next
        return None
    
    # def __iter__(self):
    #     elements = []
    #     node = self.root
    #     while node is not None:
    #         elements.append(node.value)
    #         node = node.next
    #     return iter(elements)

    def __iter__(self):
        self.current_node = self.root
        return self
    
    def __next__(self):
        if self.current_node is None:
            raise StopIteration
        value = self.current_node.value
        self.current_node = self.current_node.next
        return value
    
    def __contains__(self, value):
        node = self.root
        while node is not None:
            if node.value == value:
                return True
            node = node.next
        return False


stack = Stack()
stack.push('a')
stack.push('b')
stack.push('c')
print(stack)
print(len(stack)) # 3
print(stack[0]) # c
print(stack[1]) # b

print('c' in stack)


# string, list, tuple, dictionary, range, dict_values, dict_keys, dict_items

for i in range(len(stack)):
    print(stack[i])

for element in stack:
    print(element)



