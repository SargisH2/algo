lst=[2,5,8,12,16,23,38,56,72,91]

def linear(lst, n):
    for i in range(len(lst)):
        if lst[i]==n:
            return i
    return -1
# for i in lst:
#     print(linear(lst, i))

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
# for i in lst:
#     print(binary(lst, i))
