from AlphaTwo import AlphaTwo
#Subclass of AlphaTwo
class AlphaTwoSub(AlphaTwo):

    alphaTwoSubString = "This is AlphaTwoSub's String"

    #Subclass Constructor
    def __init__(self):
        #In Python, the Superclass is not initialized automatically
        super().__init__()
        #Inherited Field can be updated
        self.alphaTwoIntArray[4] = 6
        #Use Method of Base Class
        self.alphaTwoSubString = super().reverse_string(self.alphaTwoSubString)
