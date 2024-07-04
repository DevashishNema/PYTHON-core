a=int(input("enter any no. "))
c=b=a

count = 0
sum = 0
while a>0:
    count = count+1
    a=a//10 

print("count = ",count)        

while b>0:
    digit = b%10
    sum = sum + digit**count
    b=b//10

print(sum)   

if sum==c:
    print("the no. is armstrong")
else : 
    print("its not armstrong")     