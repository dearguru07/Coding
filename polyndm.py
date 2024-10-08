# def Poly(n):
#     rev=0
#     while n!=0:
#         rem=n%10
#         rev=rev*10+rem
#         n//=10
#     return rev
# n=int(input('enter a number'))    
# res=Poly(n)
# if res==n:
#     print('polyndrom')
# else:
#     print('not a plumdrom')    



def Poly(n):
    rev=0
    while n!=0:
        rem=n%10
        rev=rev*10+rem
        n//=10
    return rev
sr=int(input('enter a numebr'))    
er=int(input('enter a numebr'))    
for i in range(sr,er+1):
    res=Poly(i)
    if res==i:
        print(i)