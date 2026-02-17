a=10
b=40
c=30

#  a > b and a > c
#  b > a and b > c
#  c > a and c > b

#if a>b and a>c:
#   print("a is greater")
#elif (b>a) and (b>c):
#   print("b is greater")
#elif (c>a) and (c>b):
#   print("c is greater")


# a > b and a > c
# 10 > 40 
#if a > b and a > c:
 #  print("a is greater")
#elif b > c:
 #  print("b is greater")
#else:
   #print("c is greater")

#Nested if


#if ( cond ):
#  statements-1;
#statements-2;

#age=3
#age above 60 then print senior citizen
#age above 80 then print super senior citizen
#age below 60 not a senior citzen

#if age >= 18:
 #   print("eligible to vote")
  #  if age >= 80 :
   #     print("he or she is a supersenior citizen")
    #elif age >= 60 and age <= 80 :
     #    print(" he or she is a senior citizen")
    #else:
     #   print("he or she is not a supersenior citizen")   
#else:
 #  print("not eligible to vote")


# eb unit 0 to 100 = 2.5 per unit
#    subsidy_applicable = yes then reduce 0.5 per unit
# eb unit 101 to 200 = 3.5 per unit
#    subsidy_applicable = yes then reduce 0.75 per unit
# eb unit 201 to 300 = 4.5 per unit
#    subsidy_applicable = yes then reduce 0.90 per unit
# eb unit greater 300 5.0 per unit
#    subsidy_applicable = yes then reduce 1.0 per unit


units = int(input("enter the amount of units used :")
subsidy = str(input("is subsidy applicable (yes/no):") 

price_per_unit = 0
subsidy_reduce = 0

if units <= 100 :
    price_per_unit = 2.5
    if subsidy == "yes":
        subsidy_reduce = 0.5

elif units <= 200 :
    price_per_unit = 3.5
    if subsidy == "yes"
        subsidy_reduce = 0.75

elif units <= 300 :
    price_per_unit = 4.5
    if subsidy == "yes":
        subsidy_reduce = 0.90

else : 
    price_per_unit = 5.0
    if subsidy == "yes":
        subsidy_reduce = 1.0

final_rate = price_per_unit - subsidy_reduce
bill_amount = units * final_rate

print("amount of units used :",units)
print("subsidiy applicable or not:",subsidy)
print("price per unit :",price_per_unit)
print("subsidy applied :",subsidy_reduce)
print("final rate :",final_rate)
print("bill amount :",bill_amount)
print("\n-----thank yoy------")







        
    
        
     

   


