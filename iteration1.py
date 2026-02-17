'''class MyIter:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a          #x = 1
        if self.a <= 5:     #1 <= 5
            self.a += 1     #self.a = 1 + 1 = 2
            return x        #return 2
        else:
            raise StopIteration

    def next(self):
        return self.__next__()

MyIterObj = MyIter()
myiter = iter(MyIterObj)   # myiter = 1

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
#print(next(myiter))'''


