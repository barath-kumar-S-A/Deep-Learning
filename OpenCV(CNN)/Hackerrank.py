
# a='BANANA'
# b='A'
# i=0
# j=len(b)
# c=[]
# for k in range(len(a)):
#     q=a[i:j]
#     print(q)
#     if q == b:
#         c.append(1)
#     i+=1
#     j+=1
#     if j > len(a):
#         break    
    
# print(sum(c))    
        
# a='sfdvion'
# d=a[0:100]
# print(d)


# def add(x):
#     return (x)


# m = add(10)

# print(m)


# q=10
# b=12
# if q==10 or b==11:
#     print("skcfhb")



# b=input('')
# c=[]
# s=0
# j=len(b)
# while True:
#     q=b[s:j]
#     if q[0] =='A' or q[0]=='E' or q[0]=='I' or q[0]=='O' or q[0]=='U':
#         c.append(q)
#         j-=1
#         if s == len(b)-1:
#             break
#         if j == s:
#             if s == len(b)-1:
#                 break
#             s+=1
#             j=len(b)
            
#     elif s == len(b)-1:
#         break
#     else:
#         s+=1
#         j = len(b)


# d=[]
# i2=0
# j2=len(b)
# while True:
#     g=b[i2:j2]
#     if g[0] !='A' and g[0] !='E' and g[0] !='I' and g[0] !='O' and g[0] !='U':
#         d.append(g)
#         j2 -=1
#         if i2 == len(b)-1:
#             break
        
#         if j2 == i2:
#             if i2 == len(b)-1:
#                 break
#             i2+=1
#             j2 = len(b)
#     elif i2==len(b)-1:
#         break
    
#     else:
#         i2+=1
#         j2 = len(b)


# def count(list):
#     total=[]
#     for i in list:
#         k=len(i)
#         j=0
#         c1=[]
#         for i1 in range(len(b)):
#             e=b[j:k]
#             if e == i:
#                 c1.append(1)
#             j+=1
#             k+=1
#             if k>len(b):
#                 total.append(sum(c1))
#                 break
#     return sum(total)

# c9=set(c)
# d9 = set(d)
# c_value =count((c9))
# d_value = count(set(d9))
# if d_value > c_value:
#     print('Stuart',d_value)

# if c_value > d_value:
#     print('Kevin',c_value)
# elif c_value == d_value :
#     print('Draw')

import cv2

img = cv2.VideoCapture(0)

while True :
    a,frame = img.read()
    if not a: 
        break
    cv2.imshow('barath',frame)
    cv2.waitKey(1)
    
img.release()
cv2.destroyAllWindows()    





def minion_game(string):
    b=string
    c=[]
    s=0
    j=len(b)
    while True:
        q=b[s:j]
        if q[0] =='A' or q[0]=='E' or q[0]=='I' or q[0]=='O' or q[0]=='U':
            c.append(q)
            j-=1
            if s == len(b)-1:
                break
            if j == s:
                if s == len(b)-1:
                    break
                s+=1
                j=len(b)
                
        elif s == len(b)-1:
            break
        else:
            s+=1
            j = len(b)
   
    # Banana
    
    # d=[]
    # i2=0
    # j2=len(b)
    # while True:
    #     g=b[i2:j2]
    #     if g[0] !='A' and g[0] !='E' and g[0] !='I' and g[0] !='O' and g[0] !='U':
    #         d.append(g)
    #         j2 -=1
    #         if i2 == len(b)-1:
    #             break
            
    #         if j2 == i2:
    #             if i2 == len(b)-1:
    #                 break
    #             i2+=1
    #             j2 = len(b)
    #     elif i2==len(b)-1:
    #         break
        
    #     else:
    #         i2+=1
    #         j2 = len(b)
    
    
    # def count(list):
    #     total=[]
    #     for i in list:
    #         k=len(i)
    #         j=0
    #         c1=[]
    #         for i1 in range(len(b)):
    #             e=b[j:k]
    #             if e == i:
    #                 c1.append(1)
    #             j+=1
    #             k+=1
    #             if k>len(b):
    #                 total.append(sum(c1))
    #                 break
    #     return sum(total)
    
    # c9=set(c)
    # d9 = set(d)
    # c_value =count((c9))
    # d_value = count(set(d9))
    # if d_value > c_value:
    #     print('Stuart',d_value)
    
    # if c_value > d_value:
    #     print('Kevin',c_value)
    # elif c_value == d_value :
    #     print('Draw')