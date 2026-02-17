
#name="Global"

#def print_name():
    #name="Local"
 #   print(name)


#print(name)  #  I am a global variable
#print_name() #  I am a global variable

# Exercise
#    Create a function sum() which accepts 2 integers as arguments*
#    Create two global variables *
#    Pass the 2 integers as params to sum() and print the output *
#    Create two local variable with the same name as that of global variable
#    Add two integers and print it


fnum=30
snum=20
c= 25

def sum(f,s):  # sum(*args) ===> 10 20 30 40 50
    global c
    
    print("Local variable ", hex(id(f)))
    print("Local variable ", hex(id(s)))
    print( fnum + snum + c ) 
    

print("Global variable ", hex(id(fnum)))
print("Global variable ", hex(id(snum)))

sum(fnum,snum)


    
    #first_num = 25
    #second_num =25
    #print sum()
#  
#def sum(fnum,snum) {
#    print( fnum + snum   ) 
#}

#  fnum = 1000    snum = 2000
#  sum(fnum, snum)
#  f = fnum ==> 1000
#  s = snum ==> 2000