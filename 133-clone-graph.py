def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node):
            if node in hashmap:
                return hashmap[node]
            copy = Node(node.val)
            hashmap[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        hashmap = {}
        return dfs(node) if node else None
