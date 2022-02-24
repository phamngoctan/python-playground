import collections

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    """To be reimplementation
    using also DFS with stack, DFS with recursion
    """
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        m = {node: Node(node.val)}
        deque = collections.deque([node])
        while deque:
            n = deque.popleft()
            for neigh in n.neighbors:
                if neigh not in m:
                    deque.append(neigh)
                    m[neigh] = Node(neigh.val)
                m[n].neighbors.append(m[neigh])
        return m[node]
        
    def cloneGraph_wrongthinking(self, node: 'Node') -> 'Node':
        """
        Using the set will not help, because we clone a new node, idea is that 
        we keep the previous clone node in the dict
        so we point to it later (circular)
        """
        def bfs(root):
            if not root:
                return
            visited = set()
            visited.add(root)
            newRoot = clone(root)
            queue = [[root, newRoot]]
            while queue:
                # for i in range(totalItem):
                cur, parent = queue.pop(0)
                cloneCur = clone(cur)
                for neighbor in cur.neighbors:
                    cloneNeighbor = clone(neighbor)
                    parent.neighbors.append(cloneNeighbor)
                    if not neighbor in visited:
                        queue.append([neighbor, cloneNeighbor])
                        visited.add(neighbor)
            # for neighbor in root.neighbors:
            #     print(f'{neighbor.val}')
            # for neighbor in newRoot.neighbors:
            #     print(f'{neighbor.val}')
            return newRoot
        def clone(aNode):
            return Node(aNode.val)
        return bfs(node)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors.append(node2)
node1.neighbors.append(node4)

node2.neighbors.append(node1)
node2.neighbors.append(node3)

node3.neighbors.append(node2)
node3.neighbors.append(node4)

node4.neighbors.append(node1)
node4.neighbors.append(node3)
sol = Solution()
ans = sol.cloneGraph(node1)
