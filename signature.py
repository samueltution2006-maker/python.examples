# Function signature
#   Number of parameters / arguments
#   Order of arguments
#   Data type of arguments
#   Return type

class overloading:
    def signature(self) -> int:
        print("Function with no arguments")
        return 10

    def signature(self, a) -> int:
        print("Function with one argument")
        return 10 + a

    def signature(self, a , b) -> int:
        print("Function with two arguments")
        return 10 + a + b

result1 = overloading()
print(result1.signature())
print(result1.signature(5))
print(result1.signature(10, 20))