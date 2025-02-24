class AlphaTwo:

    #Properties
    outerAlphaTwoString = ""

    #Constructor
    def __init__(self):
        self.outerAlphaTwoString = "This is AlphaTwo's String"

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

#In Python, functions can exist outside of classes and are different from methods
def function_min_array(intarray):
    return min(intarray)

def void_function():
    print("Void function only executes code")