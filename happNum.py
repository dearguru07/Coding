def Prime(n):
    tem=True
    er=n//2
    for i in range(2,er+1):
        if n%i==0:
            tem=False
            break
    if tem==True and n>1:
        print('prime')
    else:
        print('not a prime')        
n=int(input('emter'))        
Prime(n)