n = int(input("enter any no. = "))
digit,x = 0,n
while n>0:
    rev = n%10
    digit = digit *10 + rev
    n = n//10

print(digit)   
print(x) 
print(n)

if x==digit:
    print("palindrom")
else:
    print("not palindrom")    