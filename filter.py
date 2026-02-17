
list = [ 1, 3, 5, 6, 8, 11, 13, 9 ]
list1 = [ "Hello", "World", "from", "python", "Hello" ]
mydict = { 1: 'Three', 2: 'Four' }

def even(x):
    if x % 2 == 0:  #1 % 2 = 1, 3 % 2 = 1, 5 % 2 = 1, 6 % 2 = 0
        return True #1 % 2 = 1, 2 % 2 = 0
    else:
        return False


def filterword(x):
    if x != 'Hello': # Hello != "Hello", "World" != "Hello", "from" != "Hello"
        return False
    else:
        return True  # output = "Hello", "Hello"

# list = [ 1, 3, 5, 6, 8, 11, 13, 9 ]
evenos = filter(even, list)    # filter(even, [ 1, 3, 5, 6, 8, 11, 13, 9 ])
                               # evenos = 1, 3, 5, 11, 13, 9

for no in evenos:
    print("Filtered List ", no)

# Collect all IP addresses, CHINA

# list1 = [ "Hello", "World", "from", "python", "Hello" ]
wf = filter(filterword, list1)   # filter(filterword, [ "Hello", "World", "from", "python", "Hello" ])

for word in wf:
    print("Filtered word" , word)

# mydict = { 1: 'Three', 2: 'Four' }
dt = filter(even, mydict.keys())   #filter(even, {1, 2})

for item in dt:
    print("Dictionary Result", item)