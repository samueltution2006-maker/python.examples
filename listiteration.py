mylst = [1,2,3,4,5,6,7,8,9]


class myiter :

    def __iter__(self):
        self.data = mylst
        return self

    def __next__(self):
        x = self.data
        i = mylst(0) 
        while i == mylst(1):
            i+=1
            return i            

    def next(self):
        return self.__next__()

MyIterObj = myiter()
Myiter = iter(MyIterObj)   

print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))

