arr=['d5','a8','a3','c7','c3','d8','e6','e3','f7','f3','g6','g3','h8','a6']
n=8
taxtak=[]
syuner='abcdefgh'
a=[[syuner.index(i), n-int(j)] for i, j in arr]
taxtak = [[0 for i in range(n)] for j in range(n)]

taxtak[a[0][1]][a[0][0]]=1
for i in a[1:-1]:
    taxtak[i[1]][i[0]]=8
taxtak[a[-1][1]][a[-1][0]]=7
 
print(*taxtak, sep='\n')
c=1 #count

def hasanq():
    x=a[-1][1]
    y=a[-1][0]
    for i in range(x-1, x+2):
        if i>7 or i<0: continue
        for j in range(y-1, y+2):
            if j>7 or j<0: continue
            if taxtak[i][j]==1:
                return True
    return False

def addlayer(x,y):
    global taxtak
    for i in range(x-1, x+2):
        if i>7 or i<0: continue
        for j in range(y-1, y+2):
            if j>7 or j<0: continue
            if not taxtak[i][j]:
                taxtak[i][j]+=1
    taxtak[x][y]+=1

def addlayers():
    add=[]
    for i in range(n):
        for j in range(n):
            if taxtak[i][j]==1:
                add.append((i,j))
    for i,j in add:
        addlayer(i,j)

while not hasanq():
    addlayers()
    c+=1

print(c)
print(*taxtak, sep='\n')