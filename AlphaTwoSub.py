from AlphaTwo import AlphaTwo
#Subclass of AlphaTwo
class AlphaTwoSub(AlphaTwo):
    #Subclass Constructor
    def __init__(self):
        #In Python, the Superclass is not initialized automatically
        super().__init__()
        #Inherited Field can be updated
        self.alphaTwoIntArray[4] = 6
