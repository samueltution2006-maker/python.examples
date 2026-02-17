from functools import reduce

import operator

mylist = [ 7, 8, 9 ]    #56 * 9  =   504

mystrlist = [ "hello", "reduce" ]

myset = { 1, 2, 5, 7 }

def do_sum(x, y):
    return x + y

print(reduce(do_sum, [1, 2, 3, 4]))  #1st x=1, y=2 ==> 3
                                     #2nd x=3, y=3 ==> 6
                                     #3rd x=6, y=4 ==> 10

print(reduce(operator.add, mylist))  # 7 + 8 + 9 = 24

print(reduce(operator.mul, myset))   #1 * 2 * 5 * 7 = 70
 
print(reduce(operator.add, mystrlist))