class base {
     private void privateMethod() {
        System.out.println("Base private method called");
     }
     
     public void publicMethod() {
        System.out.println("Base public method called");
     }
}

public class derived extends base {
     public void derivedMethod() {
        System.out.println("Derived Method called");
     }
     
     public static void main(String []a) {
         derived dObj = new derived();
         dObj.publicMethod();
         dObj.derivedMethod();
         dObj.privateMethod();

     }
}


class base
{
    public void baseMethod() {
        System.out.println("Base Method");
    }
	
}
public class derived extends base
{
    public void derivedMethod() {
        System.out.println("Derived Method");
    }
    
    public static void main(String []a) {
        derived dObj = new derived();
        dObj.baseMethod();
        dObj.derivedMethod();
    }
}



// Hierarchial Inheritance - A class that's derived by another class which in turn is derived by another class
class base
{
    public void baseMethod() {
        System.out.println("Base Method");
    }
	
}

class anotherBase extends base
{
    public void anotherBaseMethod() {
        System.out.println("AnotherBase Method");
    }
	
}

public class derived extends anotherBase
{
    public void derivedMethod() {
        System.out.println("Derived Method");
    }
    
    public static void main(String []a) {
        derived dObj = new derived();

        dObj.baseMethod();
        dObj.anotherBaseMethod();
        dObj.derivedMethod();
    }
}
