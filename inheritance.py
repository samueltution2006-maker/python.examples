# Single, Multiple, Multi-level, Hybrid, Hierarchial

class base:
     def baseMethod(self):
        print("Base method called")

class anotherBase:
     def __privateMethod(self):
        print("Private Method called")

     def secondBase(self):
        print("Second Base Method called")

class derived(base, anotherBase):
     def derivedMethod(self):
        print("Derived Method called")


#bObj = base();
#bObj.baseMethod()

dObj = derived()
dObj.baseMethod()
dObj.secondBase()
dObj.derivedMethod()
dObj.__privateMethod()

