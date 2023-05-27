#arabic to roman
def torom(n: int) -> str: #>3999
    if n>=4000:
        return 0
    syms={1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    result=''
    s=0
    for i in range(len(syms)-1,-1,-1):
        arabic=list(syms.keys())[i]
        c=0
        while c<3 and s+arabic<=n:
            s+=arabic
            result+=syms[arabic]
            c+=1
        if s+arabic<=n:
            s+=arabic
            if syms[arabic*5] in result:
                result=result[:-4] + syms[arabic] + syms[arabic*10]
            else:
                result=result[:-2] + syms[arabic*5]
    return result

#roman to arbic
def toar(rom: str) -> int:
    nums={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    length=len(rom)
    if length==1:
        return nums[rom]
    s=0
    i=0
    while i < length:
        sym=rom[i]
        if not i==length-1:
            if nums[sym]<nums[rom[i+1]]:
                s+=nums[rom[i+1]]-nums[sym]
                i+=2
                continue
        s+=nums[sym]
        i+=1
    return s