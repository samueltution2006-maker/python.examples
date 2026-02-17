#SINGLE INHERITANCE

#class base:
 #    def baseMethod(self):
  #      print("Base method called")

#class derived(base):
 #    def derivedMethod(self):
  #      print("Derived Method called")

#dObj = derived()
#dObj.baseMethod()
#dObj.derivedMethod()

#MULTI-LEVEL INHERITANCE

#class base:
 #   def baseMethod(self):
  #      print("Base method called")
   # def secondMethod(self):
    #    print("Private Method called")


#class anotherBase(base):
 #   def secondMethod(self):
  #      print("Private Method called")

#class derived(base):
 #   def derivedMethod(self):
  #      print("Derived Method called")

#dObj = derived()
#dObj.baseMethod()
#dObj.derivedMethod()
#dObj.secondMethod()

#HEIRARCHIAL INHERITANCE

#class base:
#    def baseMethod(self):
#        print("Base method called")
#class anotherBase(base):
#    def secondMethod(self):
#        print("Private Method called")
#class derived(anotherBase):
#    def derivedMethod(self):
#        print("Derived Method called")

#dObj = derived()
#dObj.baseMethod()
#dObj.derivedMethod()
#dObj.secondMethod()

#MULTIPLE INHERITANCE

#class base:
#    def baseMethod(self):
#        print("Base method called")
#class anotherBase:
#    def secondMethod(self):
#        print("Private Method called")
#class derived(base,anotherBase):
#    def derivedMethod(self):
#        print("Derived Method called")

#dObj = derived()
#dObj.baseMethod()
#dObj.derivedMethod()
#dObj.secondMethod()

#HYBRID INHERITANCE 
# CLASS A
# CLASS B INHERIT A
# CLASS C INHERIT A
# CLASS D INHERIT B AND C 

class base:
    def firstMethod(self):
        print("first method called")

    def overridingMethod(self):
        print("Base override Method called")

class secondBase(base):
    def secondMethod(self):
        print("second Method called")


class thirdBase(base):
    def thirdMethod(self):
        print("third Method called")

class derived(secondBase,thirdBase):
    def derivedMethod(self):
        print("Derived Method called")


    #def overridingMethod(self):
    #    print("Derived override Method called")   

    def overridingMethod(self, a):
        print("Derived override Method called", a)   



dObj = derived()
dObj.firstMethod()
dObj.secondMethod()
dObj.thirdMethod()
dObj.derivedMethod()
#dObj.overridingMethod()
dObj.overridingMethod(5)



























