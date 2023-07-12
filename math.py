#GrayCode, Gaussian distribution(properties)
##################

# bits=4
# n=2**bits
# #normal
# print('Normal')
# for i in range(n):
#     bin_i=bin(i).replace('0b', '')
#     print((bits-len(bin_i))*'0'+bin_i)
# #Hamiltonian loop
# lst=['0','1']
# for i in range(bits-1):
#     lst=list(map(lambda x: '0'+x, lst))+list(map(lambda x: '1'+x, lst[-1::-1]))
# print('After Gray Code algorithm. This is the Hamiltonian loop.')
# print(*lst, sep='\n')

#####################

x = [12, 15, 25, 20, 18]
y = [31, 21, 25, 30, 40]


def E(a): #Expectation
    return sum(a)/len(a)

def D(a): #Dispersion, SD^2
    a2=list(map(lambda x:x**2, a))
    return E(a2)-E(a)**2

def cov(a,b):
    n=len(a)
    summa=0
    for i in range(n):
        summa+=(a[i]-E(a))*(b[i]-E(b))
    return summa/n

def corr(a,b):
    return cov(a,b)/(D(a)*D(b))**0.5

print(corr(x,y), cov(x,y), E(x), E(y), D(x), D(y))

#####################
