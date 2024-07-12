# block of code , use for specific task , always have to call function  

# user define function 
# syntex: 
#        def 



# def add(x,y,z):
#     print(x+y+z)
    
# p = int(input("Enter 1 no."))
# q = int(input("Enter 2 no."))
# r = int(input("Enter 3 no.")) 
# add(p,q,r)   

# x = add(p,q,r)
# print(x)

# x= x+100
# print(x)



def add(x,y):
    return x+y , x-y , x*y , x/y , x%y , x//y
    
p = int(input("Enter 1 no."))
q = int(input("Enter 2 no."))
a,b,c,d,e,f=add(p,q)   

print(a,b,c,d,e,f)