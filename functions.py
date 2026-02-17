


#def sum(a, b):
 #   print(a + b)


#a=10
#b=5

#print(a + b)
#sum(a, b)    # a- 10, b - 5

#d=10
#e=5

#print(d + e)
#sum(d, e)    # a - 10, b - 5

#x=10
#y=5

#print(f + g)
#sum(x, y)

#f(x) = x^2   x=2  result=4
#d(a) = a^3   a=3  result=27
#f(x,y)
#f(f(x))y
#f()

#if x == 0:
#   print(x)





n = input("enter the  number from the user:")
a=0
b=0
c=0
j=int(0)
def armstrong(n):
    a = int(n[0])   # n='153'   a='1'  a=int(n[0])   a=1
    b = int(n[1])   # b='5'  b=int(n[1])   b=5
    c = int(n[2])   # c='3'  c=int(n[2])   c=3
    global j
    j = ( a**3 + b**3 + c**3)
    print(a**3)
    print(b**3)
    print(c**3)
    print(j)
armstrong(n)


print("J value is ", j)
if j == int(n):    # 153 == "153"
    print("the given number is a armstrong number")
else:
    print("the given number is not a armstrong number")
    







    
    





  