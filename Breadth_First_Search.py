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
                print(f,end=" ")
        else:
                if path[f]==-1:
                        print("No path")
                else:
                        printPathRecursion(s,path[f])
                        print(f,end=" ")
if __name__ == '__main__':
    v,e=map(int,input("Nhap vao so dinh va so canh cua do thi : \n").split())
    for i in range(e):
            u,v=map(int,input().split())
            graph[u].append(v)
            graph[v].append(u)
    s=0
    f=5
    BFS(s,v)
    print("Output :")
    printPathRecursion(s,f)       

#input  ----> Output : 0 1 5
# 6 8
# 0 1
# 0 3
# 1 2
# 1 3
# 1 5
# 2 5
# 3 4
# 3 5