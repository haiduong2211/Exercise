import sys


def reach(adj, x, y):
    visited = [0] * len(adj)
    return explore(adj,x,y,visited)
    
#xuất ra 1 nếu có đường
def explore(adj, x, y, visited):
    if (x == y): 
        return 1
    visited[x] = 1 #visit checked!
    for i in range(len(adj[x])):
        if not visited[adj[x][i]]:
            if explore(adj, adj[x][i], y, visited):
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)] #list trong list
    x, y = x - 1, y - 1 #trả về index
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
#Có: Các cạnh, các đỉnh và các cạnh liền kề
    print(reach(adj, x, y))