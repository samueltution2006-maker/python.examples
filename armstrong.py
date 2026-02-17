#n = input("enter the  number from the user:")

#sum = 0

#for character in n:
 #   sum = sum + int(character) ** 3


#print("Sum of cube root ", sum)

#if sum == int(n):    # 153 == "153"
 #   print("the given number is a armstrong number")
#else:
#    print("the given number is not a armstrong number")



n = int(input("enter the number :"))
temp = n 
sum = 0

# temp = 153
#     153 > 0     d = 153 % 10 = 3  sum = 0 + 27    temp = 153 // 10 = 15

#     15 > 0      d = 15 % 10  = 5  sum = 27 + 125  temp = 15 // 10 = 1

#     1 > 0       d = 1 % 10  = 1   sum = 152 + 1   temp = 1 // 10 = 0

while temp > 0:
    d = temp % 10
    sum = sum + d*d*d
    temp = temp // 10
if sum  == n: 
    print("the give no is a armstrong")
else: 
    print("the given no is not a armstrong")

    
     
