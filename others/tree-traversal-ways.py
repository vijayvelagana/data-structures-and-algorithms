class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    def bfs(self):
        q = []
        q.append(self)
        while q:
            curr = q[0]
            q.pop(0)
            print(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
                
    def preorder(self): # rLR
        if self:
            print(self.val)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
            
    def inorder(self): # LrR
        if self.left:
            self.left.inorder()
        print(self.val)
        if self.right:
            self.right.inorder()
            
    def postorder(self): # LRr
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        if self:
            print(self.val)
        
        
r = Tree(0)
a = Tree(1)
b = Tree(2)
c = Tree(3)
d = Tree(4)
e = Tree(5)
f = Tree(6)
g = Tree(7)

r.left = a
r.right = b

a.left = c
a.right = d

b.left = e
b.right = f

f.left = g

print("Breadth First Search (BFS)")
r.bfs()

print("#################")
print("Depth First Search (DFS) -- Preorder Traversal (rLR)")
r.preorder()

print("#################")
print("Depth First Search (DFS) -- Inorder Traversal (LrR)")
r.inorder()

print("#################")
print("Depth First Search (DFS) -- Postorder Traversal (LRr)")
r.postorder()


'''
Breadth First Search (BFS)
0
1
2
3
4
5
6
7
#################
Depth First Search (DFS) -- Preorder Traversal (rLR)
0
1
3
4
2
5
6
7
#################
Depth First Search (DFS) -- Inorder Traversal (LrR)
3
1
4
0
5
2
7
6
#################
Depth First Search (DFS) -- Postorder Traversal (LRr)
3
4
1
5
7
6
2
0

=== Code Execution Successful ===
'''
