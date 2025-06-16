class Node:
    def __init__(self, key = None, value = None, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.head = Node()
        self.tail = Node()
        self.tail.prev = self.head
        self.head.next = self.tail
        self.keys_dict = dict()

    def add(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
    
    def move_to_end(self, node):
        # handling connections at existing spot
        node.next.prev = node.prev
        node.prev.next = node.next

        # handling connections at the end
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def delete(self, node):
        self.keys_dict.pop(node.key)
        node.next.prev = self.head
        self.head.next = node.next
    
    def get(self, key):
        if key in self.keys_dict:
            self.move_to_end(self.keys_dict[key])
            return self.keys_dict[key].value
        else:
            return -1
    
    def put(self, key, value):
        if key in self.keys_dict:
            self.keys_dict[key].value = value
            self.move_to_end(self.keys_dict[key])
        else:
            if len(self.keys_dict) == self.cap:
                self.delete(self.head.next)
                node = Node()
                node.key = key
                node.value = value
                self.add(node)
                self.move_to_end(node)
                self.keys_dict[key] = node
            else:
                node = Node()
                node.key = key
                node.value = value
                self.add(node)
                self.move_to_end(node)
                self.keys_dict[key] = node


