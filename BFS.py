Max=100
v=None
e=None
graph=[[] for i in range(Max)]
visited=[False]*Max
path=[0]*Max
def printPath(s,f):
	b=[]
	if f==s:
		print(f)
		return
	if path[f]=-1:
		print("No path")
		return
	while True:

