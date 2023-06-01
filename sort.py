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
    

arr=[1,3,2,5,6,6,4,20,5]
print(merge(arr))

