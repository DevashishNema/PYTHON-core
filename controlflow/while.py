n = int(input("enter how many natural no. you want = "))
i=1
sum=0
multi=1
# while i<=n:
#     print(i,end=",")
#     i=i+1

# while i<=n:
#     if i<=n-1:
#         print(i,end=",")
#     else:
#         print(i)    
    
#     i=i+1

# while i<=n:
#     sum=sum+i
#     if i<=n-1:
#         print(i,end=",")
#     else:
#         print(i,end="=")    
    
#     i=i+1   

# print(sum)     


while i<=n:
    multi=multi*i
    if i<=n-1:
        print(i,end="*")
    else:
        print(i,end="=")    
    
    i=i+1   

print(multi)   