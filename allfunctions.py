

def noParam():
    print("Function with no parameter")

def oneParam(a):
    print("Function with one param ", a)

def twoParams(a, b):
    print("Function with two params ", a + b)

def varParams(*args):
    print("Function with one param ", args[0], args[1], args[2], args[3], args[4])

def mixedParams(a, b, *varArgs):
    print("Mixed params ", a, b, varArgs[0], varArgs[1])


noParam()
oneParam(5)
twoParams(5, 10)
varParams(1, 2, 3, 4, 5)
mixedParams(10, 20, 30, 40)