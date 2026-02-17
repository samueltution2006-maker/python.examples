import math
# -32768 
a = 10
b = 0

try:
    print("The result is ", a / b)
except FloatingPointError:
    print("Divide by Zero Not Allowed")
except:
    print("General exception caught when exact match is not found")

try:
    result = math.exp(1000)
except OverflowError:
    print("Overflow error occurred")
except:
    print("General exception caught when exact match is not found")

print("End of program")


# print("The result is ", a / b)
#except ArithmeticError:
#    print("Arithmetic Error")
# except:
#    print("Exception occurred, continuing with program")