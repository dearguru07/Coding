# def Reverese(n):
#     rev=0
#     while n!=0:
#         rem=n%10
#         rev=(rev*10)+rem
#         n=n//10
#     return rev
# n=int(input('enter number'))    
# res=Reverese(n)
# print(res)



def Reverese(n):
    rev=0
    while n!=0:
        rem=n%10
        rev=rev*10+rem
        n//=10
    return rev
sr=int(input('entera numebr'))    
er=int(input('entera numebr'))
for i in range(sr,er+1):
    res=Reverese(i)
    print(i,'revision is',res)