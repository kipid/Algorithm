"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNewMap = dict()
        oldToNewMap[node] = Node(node.val)
        q = deque([node])
        while q:
            cur = q.popleft()
            curClone = oldToNewMap[cur]
            neighbors = []
            for neighbor in cur.neighbors:
                if neighbor not in oldToNewMap:
                    oldToNewMap[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                neighbors.append(oldToNewMap[neighbor])
            curClone.neighbors = neighbors

        return oldToNewMap[node]