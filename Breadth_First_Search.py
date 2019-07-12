from queue import Queue

Max=100
v=None
e=None
visited=[False for i in range(Max)]
path=[0 for i in range(Max)]
graph=[[] for i in range(Max)]

def BFS(s,v):     
    for i in range(v):
        visited[i]=False
        path[i]=-1

    q=Queue()
    visited[s]=True
    q.put(s)
    while q.empty()==False :
            u=q.get()
            for v in graph[u]:
                    if visited[v]==False:
                            visited[v]=True
                            q.put(v)
                            path[v]=u
def printPathRecursion(s,f):
        if s==f:
                print(f,end='')
        else:
                if path[f]==-1:
                        print("No path")
                else:
                        printPathRecursion(s,path[f])
                        print(f,end='')
if __name__ == '__main__':
    v,e=map(int,input().split())
    for i in range(e):
            u,v=map(int,input().split())
            graph[u].append(v)
            graph[v].append(u)
    s=0
    f=5
    BFS(s,v)
    printPathRecursion(s,f)       
# import collections
# def bfs(graph, root): 
#     visited, queue = set(), collections.deque([root])
#     visited.add(root)
#     while queue: 
#         vertex = queue.popleft()
#         for neighbour in graph[vertex]: 
#             if neighbour not in visited: 
#                 visited.add(neighbour) 
#                 queue.append(neighbour) 
#         return queue
# if __name__ == '__main__':
#     graph = {0: [1, 2], 1: [2], 2: [3], 3: [1,2]} 
#     a=bfs(graph, 0)
#     print(a)

# 6 8
# 0 1
# 0 3
# 1 2
# 1 3
# 1 5
# 2 5
# 3 4
# 3 5