#Superclass/Base Class
class AlphaTwo:

    #Fields/Properties
    outerAlphaTwoString = ""

    #Constructor
    def __init__(self):
        # Fields/Properties are declared inside constructor in Python
        self.outerAlphaTwoString = "This is AlphaTwo's String"
        #Array is declared here in Python otherwise the Subclass will overwrite it
        self.alphaTwoIntArray = [1, 2, 3, 4, 5]

    #Methods
    #Public method
    def sum_int_array(self, intarray):
        return sum(intarray)
    #Static method
    @staticmethod
    def average_int_array(intarray):
        return sum(intarray)/len(intarray)
    #Void method does not have return type, it only executes code
    def void_alpha_two(self):
        print(f"AlphaTwo's Void method returned: {self.outerAlphaTwoString}")
    @staticmethod
    def reverse_string(s):
        return s[::-1]
    #Method overloading is not recommended in Python

    #Inner Class
    class InnerAlphaTwo:
        innerAlphaTwoString = "This is InnerAlphaTwo's String"
        updatedAlphaTwoString = ""

        #Setter
        def inner_alpha_two_set(self):
            self.updatedAlphaTwoString = "AlphaTwo's String has been updated from within InnerAlphaTwo"

        #Getter
        def inner_alpha_two_get(self):
            print(f"Inner Class of AlphaTwo's property reads: {self.innerAlphaTwoString}")
            print(self.updatedAlphaTwoString)

        @staticmethod
        def min_int_array(intarray):
            return min(intarray)

#In Python, functions can exist outside of classes and are different from methods
def function_min_array(intarray):
    return min(intarray)

def void_function():
    print("Void function only executes code")