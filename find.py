# linear, binary, ternary search algorithms

lst=[2,5,8,12,16,23,38,56,72,91]

def linear(lst, n):
    for i in range(len(lst)):
        if lst[i]==n:
            return i
    return -1

def binary(_lst, _n):
    _starti = 0
    _endi = len(_lst)-1
    def bin(lst, n, a, b):
        if a==b and not lst[a] == n: return -1
        mid_i=(a+b)//2
        if n < lst[mid_i]:
            return bin(lst, n, a, mid_i)
        elif n > lst[mid_i]:
            return bin(lst, n, mid_i +1, b)
        else:
            return mid_i
    return bin(_lst, _n, _starti, _endi)

def ternary(lst, n):
    firsti=0
    lasti=len(lst)-1
    def tern(lst, n, a,b):
        indpoint1=a+(b-a)//3
        indpoint2=b-(b-a)//3
        if b-a<3:
            if n==lst[a]:return a
            elif n==lst[b]:return b
            else: return -1
        if n<=lst[indpoint1]:
            return tern(lst, n, a, indpoint1)
        elif n>=lst[indpoint2]:
            return tern(lst, n, indpoint2, b)
        else:
            return tern(lst, n, indpoint1+1, indpoint2-1)
    return tern(lst, n, firsti, lasti)
