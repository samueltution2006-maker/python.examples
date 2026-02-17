#without using the third variable 
a=input("enter the variable a:")
b=input("enter the varaible b:")
def swapping(a,b):
    a,b = b,a
    print(a)
    print(b)
swapping(a,b)


#with usin the third variable

def swap(a,b):
    temp=a
    a=b
    b=temp 
    
    print(a)
    print(b)
swap(a,b)