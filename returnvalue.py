

#def sum(a, b):          # Line no 1
    #print(a + b)       # Line no 2
    #return a  + b       # Line no 3


#result = sum(5, 10);  # Function call
                      # a = 5 and b = 10

#print(result * 5)


# f(x)     = 9
# f(f(x))  = f(9)


n= int(input("enter the number to find the factorial of "))
def factorial(n):   
    result = 0
                
    for i in range(n, 1, -1):
        next_number = i - 1
        print("N is ", n, "Next number ", next_number)

        if result == 0:
            result = i * next_number
        else:
            result = result * next_number

    print("Result is ", result)
        
 
          
factorial(n)


# WAP with a function to swap two numbers with and without using third variable