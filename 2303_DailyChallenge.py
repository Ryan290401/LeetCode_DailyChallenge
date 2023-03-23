class Solution(object):
    def makeConnected(self, n, connections):

        if len(connections) < n - 1:
            return -1

        conn = [i for i in range(n)]

        for connection in connections:
            conn1 = self.findPath(conn, connection[0])
            conn2 = self.findPath(conn, connection[1])

            if conn1 != conn2:
                conn[conn1] = conn2

        num_of_sets = 0
        for i in range(n):
            if conn[i] == i:
                num_of_sets += 1

        return num_of_sets - 1

    def findPath(self, conn, node):
        if conn[node] != node:
            conn[node] = self.findPath(conn, conn[node])
        return conn[node]