#merge, selection, bubble
def merge(d):
    n=len(d)
    if n==1:
        return d
    else:
        a=merge(d[:int(n/2)])
        b=merge(d[int(n/2):])
        c=[]
        p,q=0,0
        for i in range(n):
            if p==len(a):
                c.extend(b[q:])
                break
            else:
                if q==len(b):
                    c.extend(a[p:])
                    break
            if a[p]>b[q]:
                c.append(b[q])
                q+=1
            else:
                c.append(a[p])
                p+=1
        return c
    
def selection(arr):
    n=len(arr)
    for k in range(n):
        ind=k
        for i in range(ind +1, n):
            if arr[i]<arr[ind]:
                ind=i
        arr[k],arr[ind]=arr[ind], arr[k]
    return arr

def bubble(arr):
    n=len(arr)
    for _ in range(n):
        for i in range(n-1):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr







arr=[2,3,2,5,1,6,4,20,5]
print(merge(arr))
print(selection(arr))
print(bubble(arr))

