arr=['d5','a8','a3','c7','c3','d8','e6','e3','f7','f3','g6','g3','h8','a1']
n=8
taxtak=[]
syuner='abcdefgh'
a=[[syuner.index(i), n-int(j)] for i, j in arr]
taxtak = [[0 for i in range(n)] for j in range(n)]

taxtak[a[0][1]][a[0][0]]=1
for i in a[1:-1]:
    taxtak[i[1]][i[0]]=5
taxtak[a[-1][1]][a[-1][0]]=7

print(*taxtak, sep='\n')
c=1 #count

def getpositions(k):
    arr=[]
    for i in range(n):
        for j in range(n):
            if taxtak[i][j]==k:
                arr.append((i,j))
    return arr
            
def hasanq():
    print()
    print(*taxtak, sep='\n')
    arr=getpositions(7)
    for x,y in arr:
        for i in range(x-1, x+2):
            if i>7 or i<0: continue
            for j in range(y-1, y+2):
                if j>7 or j<0: continue
                if taxtak[i][j]==1:
                    return True
    return False

def addlayer(x,y, k=1):
    global taxtak
    for i in range(x-1, x+2):
        if i>7 or i<0: continue
        for j in range(y-1, y+2):
            if j>7 or j<0: continue
            if not taxtak[i][j]:
                taxtak[i][j]=k
    taxtak[x][y]+=1

def addlayers(k=1):
    add=[]
    for i in range(n):
        for j in range(n):
            if taxtak[i][j]==k:
                add.append((i,j))
    for i,j in add:
        addlayer(i,j,k)

while not hasanq():
    addlayers()
    c+=1
    if not hasanq():
        addlayers(7)
        c+=1

print(c)
print(*taxtak, sep='\n')