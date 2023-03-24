class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        route = set()
        count = 0
        incomming = collections.defaultdict(list)
        outgoing = collections.defaultdict(list)
        for con1, con2 in connections:
            incomming[con2].append(con1)
            outgoing[con1].append(con2)

        stack = [0]
        while stack:
            next_stack = []
            for node in stack:
                route.add(node)
                for child in incomming[node]:
                    if child not in route:
                        next_stack.append(child)
                for child in outgoing[node]:
                    if child not in route:
                        next_stack.append(child)
                        count += 1
            stack = next_stack

        return count