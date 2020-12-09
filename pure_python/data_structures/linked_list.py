class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        else:
            current = self.head
            for i in range(self.index):
                current = current.next
            self.index += 1
            return current.value

    def __repr__(self):
        current = self.head
        repr_str = "["
        while current is not None:
            repr_str += str(current.value) + ", "
            current = current.next
        if self.length > 0:
            # remove trailing comma
            repr_str = repr_str[:-2]
        repr_str += "]"
        return repr_str

    def __str__(self):
        return repr(self)

    def __len__(self):
        return self.length

    def append(self, element):
        if self.head is None:
            self.head = Node(element)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(element)
        self.length += 1

    # Returns regular python list
    def get_list(self):
        return eval(repr(self))


linked_list = LinkedList()
for i in range(100):
    linked_list.append(i)

print(linked_list)
print(len(linked_list))

for element in linked_list:
    print(element)

iterator = iter(linked_list)
print(next(iterator))

