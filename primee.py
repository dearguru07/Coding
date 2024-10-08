# def Prime(n):
#     tem=False
#     errange=n//2
#     for i in range(2,errange+1):
#         if n%i==0:
#             tem=True
#             break
#     if tem==False:
#         print('Prime number')
#     else:
#         print('not a prime')        
# n=int(input('ener '))        
# Prime(n)




# def Prime(n):
#     er=n//2
#     for i in range(2,er+1):
#         if n%i==0:
#             return False
#     return True
# sr=int(input('ener '))
# eer=int(input('ener '))
# for i in range(sr,eer+1):
#     if i>1:
#         flag=Prime(i)
#         if flag==True:
#             print(i)
            

def Prime(n):
    er=n//2
    for i in range(2,er+1):
        if n%i==0:
            return False
    return True
sr=int(input('enter '))    
eer=int(input('enter '))    
if sr>eer:
    print('inavalod range')
else:
    for i in range(sr,eer+1):
        if i>1:
            flag=Prime(i)
            if flag==True:
                print(i)
            # print(i)