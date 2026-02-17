

# constructor - it's a special function or method which
# gets invoked automatically when an object is created
class constructor:
          
     def __init__(self):       # constructor
         a = 10
         print("Constructor called")

     def __init__(self, a , b):       # constructor
         print("2nd version of the Constructor called", a + b)

     def normalMethod(self):
         print("Normal Method")


#obj = constructor()

obj = constructor(10, 20)

obj.normalMethod()