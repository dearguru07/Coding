# def Leep(n):
#     if n%4==0 or n%100==0 and n%400!=0:
#         print('leep year')
#     else:
#         print('not a leep')    
# n=int(input('entera number'))        
# Leep(n)


def Leep(n):
    if n%4==0 or n%100==0 and n%400!=0:
        return True
    else:
        return False
sr=int(input('enter a number'))    
er=int(input('enter a number'))    
for i in range(sr,er+1):
    flog=Leep(i)
    if flog==True:
        print(i)

        