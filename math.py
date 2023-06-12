#GrayCode, 
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