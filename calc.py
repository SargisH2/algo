#Calculate math expression
#Without function eval()
#Example: str_="-53 / 40 / 29 * 79 * (9 - 4 )/ 82 - 40"
str_=input("N ")
def calc(txt: str) -> float:
    txt_=txt.replace('.', '')
    if txt[0]=='-':
        if txt_.replace('-', '').isalnum():
            return float(txt)
    if '(' in txt:
        txt2=txt
        pakox=0
        for i in range(txt2.index('('),len(txt2)):
            if txt2[i]==')':
                pakox+=1
                if pakox==txt2[:i].count('('):
                    txt2=txt[txt.index('(')+1:i]
                    skizb=txt[:txt.index('(')]
                    verj=txt[i+1:]
                    return calc(skizb+str(calc(txt2))+verj)
                
    txt=txt.replace(' ', "")
    txt=txt.replace('--', "+")
    for i in '-+*/':
        txt=txt.replace(i, f" {i} ")
    for i in '-+*/':
        txt=txt.replace(f'{i}  - ', f"{i} -")
    
    lst=txt.strip().split(" ")
    if lst[0]=='+':
        lst.pop(0)
    for i in range(len(lst)-1):
        if lst[i] in '/*-+' and lst[i+1]=='+':
            lst.pop(i+1)
    if lst[0]=='-':
        lst[1]='-'+lst[1]
        lst.pop(0)

    while '*' in lst:
        i=lst.index('*')

        hamarich=0
        if i>1:
            for j in range(i-2, -1, -2):
                if not(lst[j]=='/'):
                    hamarich=j+1
                    break
        else: hamarich=i-1
        
        lst[hamarich]=str(float(lst[hamarich])*float(lst[i+1]))
        lst.pop(i)
        lst.pop(i)

    while '/' in lst:
        i=lst.index('/')
        lst[i-1]= str(float(lst[i-1])/float(lst[i+1]))
        lst.pop(i)
        lst.pop(i)
    while '-' in lst:
        i=lst.index('-')
        lst[i-1]= str(float(lst[i-1])-float(lst[i+1]))
        lst.pop(i)
        lst.pop(i)
    while '+' in lst:
        i=lst.index('+')
        lst[i-1]= str(float(lst[i-1])+float(lst[i+1]))
        lst.pop(i)
        lst.pop(i)
    
    return(float(lst[0]))

print(calc(str_))