list_example = [ 1 , 2 , 3 , True ,"five",6.0]

#  Indexes     0	1		2		3
#	       1	Two		3.0		True


index  = 0
for item in list_example:
    print(index)
    index += 1


#print("Index 0th element ", list_example[0])
#print("Index last element ", list_example[3])
#print("List slicing ", list_example[0:2])
#print("Negative List slicing ", list_example[-1])

#list_numbers = [ 8, 12, 7, 1, 5, 3, 15, 10, 11 ]


    a = [1,4,10,66,71,920,1000,2]
   #a = [1,4,10,66,71,920,2,1000]

i = 0
while True:
    try:
        if a[i] > a[i + 1]:
            t = a[i]
            a[i] = a[i + 1]
            a[i + 1] = t
            i = 0      
        else:
            i = i + 1
    except:
        break

print(a)

#a[0] = 1   a[1] = 4    a[2] = 10    a[3] = 66    a[4] = 71    a[5] = 920    a[6] = 1000   a[7] = 2
#i=0 a[0] > a[0 + 1] = a[0] > a[1]  
#i=1 a[1] > a[1 + 1] = a[1] > a[2]
#i=2 a[2] > a[2 + 1] = a[2] > a[3]
#i=3 a[3] > a[3 + 1] = a[3] > a[4]
#i=4 a[4] > a[4 + 1] = a[4] > a[5]
#i=5 a[5] > a[5 + 1] = a[5] > a[6]
#i=6 a[6] > a[6 + 1] = a[6] > a[7]   1000 > 2
#    t = 1000
#    a[i] = a[i + 1]  =  a[6] = 2
#    a[i + 1] = t = 2    

#i = 0





