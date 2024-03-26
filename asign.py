a=b=10
print(f"{a=}, {b=}")

class Node:
    def __init__(self, val: int=0, left: 'Node'=None, right: 'Node'=None, next: 'Node'=None):
        self.val=val
        self.left=left
        self.right=right
        self.next=next

c=Node(0, Node(2), Node(3), Node(4))
d=Node(1)
d = d.next = c.left
print(f"{c.left.val=},\n{d.val=}\n{c.next.val=}")
