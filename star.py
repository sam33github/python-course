# # *
# # **
# # ***
# # ****
# # # *****
# # # print()




# n=int(input("enter the given number :"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1    
    
    
    
# 2.*****
#   ****
#   ***
#   **
#   *
# n=int(input("enter the given number :"))
# i=0
# while n>=i:
#     j=n
#     while i<j:
#         print("*",end="")
#         j-=1
#     print()
#     i+=1
    

# n=int(input("enter a value :"))
# i=0
# m=n

# while n>i:
#     j=0
#     while j<m:
#         print("*",end="")
#         j+=1
#     print()
#     m=m-1
#     i+=1
    
# 3.
# n=int(input("enter the given number :"))
# i=1
# m=n
# while i<=n:
#     k=1
#     while k<m:
#         print(" ",end=" ")
#         k+=1
#     m=m-1
#     j=1
   
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1 
    
# #  5        *
#            ***
#           *****
           
n=int(input("enter a value :"))
i=0
m=n//2
while i<=n:
    k=0
    while k<m:
        print(" ",end=" ")
        k+=1
    m-=1
    j=0
    while j<i:
        print("*",end=" ")
        j+=1
    print()
    i+=2
    
    
#              #5.forloop

# n=int(input("enter a number : "))
# m=n//2
# for index in range(0,n,2):
#     for sample in range(m)
#     print(" ",end="")
#     for space in range(m):
#         print("*",end="")
#     print()
#     m+=2
    