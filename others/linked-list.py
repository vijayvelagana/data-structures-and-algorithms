class LinkedListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def traverseLinkedList(self):
        currnode = self
        while currnode:
            print(currnode.val)
            currnode = currnode.next
        
node_a = LinkedListNode(1)
node_b = LinkedListNode(2)
node_c = LinkedListNode(3)

print(node_a, type(node_a) == LinkedListNode)
print(node_b, type(node_b))
print(node_c, type(node_c))

node_a.next = node_b
node_b.next = node_c

node_a.traverseLinkedList()
print("+++")
node_b.traverseLinkedList()
print("+++")
node_c.traverseLinkedList()











