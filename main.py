import sys
sys.setrecursionlimit(200000)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    components = []
    
    for vertex in range(1, n + 1):
        if not visited[vertex]:
            component = []
            stack = [vertex]
            visited[vertex] = True
            
            while stack:
                v = stack.pop()
                component.append(v)
                
                for neighbor in graph[v]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
            
            components.append(component)

    print(len(components))
    for comp in components:
        print(len(comp))
        print(' '.join(map(str, comp)))

if __name__ == "__main__":
    main()
