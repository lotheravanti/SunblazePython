
class AlphaOne():
    #Primitives
    integer = 10
    double = 12.45
    float = 3.1417639
    long = 100000000000
    booleanValue = True
    # Single quotes for Character
    character = 'a'

    #Non Primitives
    #String
    message = "Alpha One Initialized"
    #Arrays
    integerArray = [1, 2, 3, 4, 5, 6, 7]
    stringArray = ["This", "is", "an", "Array", "from", "a", "String."]

    #String Operations
    stringValue = "lower case text"
    #Get length of String
    lengthString = len(stringValue)
    #Convert to Upper Case
    upperCase = stringValue.upper()
    #Reverse String
    reverseString = stringValue[::-1]
    #Replace part of String
    replacedMessage = message.replace("One", "Prime")
    #Get last N characters of a String
    lastOfString = stringValue[-3:]
    #Remove First and Last characters of String
    removeFirstLast1 = stringValue[1 : -1]
    removeFirstLast2 = stringValue[1 : len(stringValue) - 1]
    #Check if String is Alphabet
    checkAlphabet = stringValue.isalpha()
    #Verify if String starts or ends with
    startsWith = message.startswith("Alpha")
    endsWith = message.endswith("Initialized")
    #Check if String is Upper Case or Lower Case
    upperString = stringValue.isupper()
    lowerString = stringValue.islower()

    #Array Operations
    #Generate String from Array with delimiter
    joinedArray = " ".join(stringArray)
    #Reverse Array
    reverseArray1 = stringArray[::-1]
    reverseArray2 = reversed(stringArray)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    _alphaOne = AlphaOne()
    #f"" String format is easier to work with
    print(f"'{_alphaOne.replacedMessage}' starts with Alpha: {str(_alphaOne.startsWith)} and ends with Initialized: {str(_alphaOne.endsWith)}")
    print(f"String length for '{_alphaOne.stringValue}' is {_alphaOne.lengthString}")
    print(f"Reversed String is '{_alphaOne.reverseString}', Reversed Array is '{" ".join(_alphaOne.reverseArray1)}' or {" ".join(_alphaOne.reverseArray2)}'")
    print(f"Stripping last 3 characters from '{_alphaOne.stringValue}' results in '{_alphaOne.lastOfString}'")
    print(f"Joined Array is '{_alphaOne.joinedArray}'")
    print(f"Removing first and last characters from '{_alphaOne.stringValue}' results in '{_alphaOne.removeFirstLast1}' and '{_alphaOne.removeFirstLast2}'")
