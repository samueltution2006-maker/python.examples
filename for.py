

# Syntax
# for loop_variable in range(start, stop, step):
#     loop statements

#for i in range(51):
#    print(i) 

# print only event numbers
#for i in range(0,51):
#    print(i)

# print only odd numbers
#for i in range(1,51,2):
#    print(i)

# print 0 to 50 in reverse
#for i in range(51,0,-1):
#    print(i) 

#Nested for
# 1
# 1 2
# 1 2 3

#  range(1)  = 0
#  range(2)  = 0, 1
#  range(3)  = 0, 1, 2

#for i in range(1, 4):
 #   for j in range(i):
  #      print(j + 1, end=' ')
   # print()

#i = 1
#   j = i  ==>  j = 0  ==> 0 + 1 = 1

#i = 2
#   j = 1 ==>  j = 0 ==> 0 + 1 = 1
#   j = 2 ==>  j = 1 ==> 1 + 1 = 2

#i = 3
#   j = 1 ==>  j = 0 ==> 0 + 1 = 1
#   j = 2 ==>  j = 1 ==> 1 + 1 = 2
#   j = 3 ==>  j = 2 ==> 2 + 1 = 3

#EXERCISE 1
for i in range(0,5):
    for j in range(i+1):
        print(i+1,end=' ')
    print()

for i in range(1,6):
    for j in range(i):
        print(i,end=' ')
    print()
#Exercise 1
#1
#2 2 
#3 3 3
#4 4 4 4
#5 5 5 5 5


#EXERCISE 2
for i in range(6,1,-1):
    for j in range(i-1):
        print(i-1,end=' ')
    print()
#Exercise 2
#5 5 5 5 5
#4 4 4 4
#3 3 3
#2 2
#1s


#EXECISE3
for i in range(5,0,-1):
    for j in range(i, 0, -1):
        print(j,end=' ')
    print()
#Exercise 3
#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1
#1







#EXERCISE4
for i in range(5,0,-1):
    for j in range(i):
        print(j+1,end=' ')
    print()

#1 2 3 4 5
#1 2 3 4
#1 2 3
#1 2
#1