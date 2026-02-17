'''[ [ 1, 2, 3], [ 4, 5, 6 ], [ 7, 8, 9] ]
1)  Create a function which accepts a list as parameter
2)  Pass over nested list as argument to the function
3)  Convert every  nested list to tuple and return them
4)  Print all the tuples

1)  Create a function which accepts a list as parameter
2)  Pass over nested list as argument to the function
3)  Convert every nested list to dictionary and return them
4)  Print all the dictionary
5)  If function tries to return other than dictionary it should error'''


# type casting means converting from one data type to another data type

varA = 30.22
varB = int(varA)

print("Variable B is ", varB)

example_list = list([ 1, 2, 3, 4, 5 ])
print(example_list)

example_tuple = tuple([ 1, 2, 3, 4, 5 ])
print(example_tuple)


'''list_no = [[1,2,3],[4,5,6],[7,8,9]]
list_nam = [[1:'karma'],[2:'starfish'],[3:'nolan']]
def listtotuple(list_no):
    for item in list_no:
        print(tuple(item))'''

'''def listtodict(list_nam):
    for item in list_no:
        print(dict(item))'''


'''listtotuple(list_no)
listtodict(list_no)'''

my_list = ['apple', 'banana', 'cherry']
my_dict = {}

for index, element in enumerate(my_list):
    my_dict[index] = element

print(my_dict)


