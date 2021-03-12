# author : sai suresh mv
n = 5 # n -> no. of rows
for i in range(n,0,-1):
    for j in range(1,n+1):
        if j < i:
            print(' ',end=' ')
        else:
            print('*',end = ' ')
    print()
ch = 65 # 'A' ascii = 65
for i in range(n+1):
    for j in range(i):
        print(chr(ch),end = ' ')
        ch+=1
    print()
    
        