# range = 1 to 4
# yield 1 * 1
# yield 2 * 2
# yield 3 * 3
# yield 4 * 4
# YEILD SAVES IN LOCAL MEMEORY SO IT CAN BE ACCESSED AT ANY TIME UNTIL YEILD FINISHES
# RETURN WILL NOT SAVE IN MEMEORY ONCE THE VALUE IS RETURNED 

#YEILD OF I*I = 1,4,9
#RETURN GIVES ONLY 1

def genex(x):
    for i in range(1, x):  #x = 5, 1 to 5 - 1 ie 1 to 4
        yield i*i

a = genex(10)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))