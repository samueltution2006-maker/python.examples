
nested_list = [ 1, 2.0, "Hello", True, [ 1, 2, 3, [ "Hi", "inner", "list" ] ] ]

'''
print(nested_list[0])
print(nested_list[1])
print(nested_list[2])
print(nested_list[3])
print(nested_list[4])

print(nested_list[4][0])
print(nested_list[4][1])
print(nested_list[4][2])
'''

for item in nested_list:
    if type(item) is list:
       for element in item:
           print(element)
           if type(element) is list:
              for nl in element:
                  print(nl)

# item in nested if 
#    1 => int => no
#    2.0 => float=> no
#    hello => string => no 
#    true => bool => no
#    [1,2,3] => list => elements in list => 1,2,3 


