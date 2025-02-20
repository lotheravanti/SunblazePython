#Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #Primitives
    integer = 10
    floatValue = 3.1417639
    booleanValue = True

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
    removeFirstLast1 = stringValue[1: -1]
    removeFirstLast2 = stringValue[1: len(stringValue) - 1]
    #Check if String is Alphabet
    checkAlphabet = stringValue.isalpha()
    #Verify if String starts or ends with
    startsWith = message.startswith("Alpha")
    endsWith = message.endswith("Initialized")
    #Check if String is Upper Case or Lower Case
    upperString = stringValue.isupper()
    lowerString = stringValue.islower()

    #Array Operations
    #Create new placeholder Array of fixed length
    #Create Two Dimensional Array
    twoDimArray = [[1, 2], [3, 4], [5, 6]]
    #Generate String from Array with delimiter
    joinedArray = " ".join(stringArray)
    #Reverse Array
    reverseArray1 = stringArray[::-1]
    reverseArray2 = reversed(stringArray)
    #f"" String format is easier to work with
    print(f"'{replacedMessage}' starts with Alpha: {str(startsWith)} and ends with Initialized: {str(endsWith)}")
    print(f"String length for '{stringValue}' is {lengthString}")
    print(f"Reversed String is '{reverseString}', Reversed Array is '{" ".join(reverseArray1)}' or {" ".join(reverseArray2)}'")
    print(f"Stripping last 3 characters from '{stringValue}' results in '{lastOfString}'")
    print(f"Joined Array is '{joinedArray}'")
    print(f"Removing first and last characters from '{stringValue}' results in '{removeFirstLast1}' and '{removeFirstLast2}'")
