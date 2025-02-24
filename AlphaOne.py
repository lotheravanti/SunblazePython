#Press the green button in the gutter to run the script.
from AlphaTwo import AlphaTwo

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
    #Tuple
    #Set

    #Integer Operations

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
    #Replace only N occurrences of String
    nOccurrencesString = "every e in the sentence"
    replaceNOccurrencesString = nOccurrencesString.replace("e", "E", 3)
    #Get first N characters of a String
    firstOfString = stringValue[0:1]
    #Get last N characters of a String
    lastOfString = stringValue[-3:]
    #Remove First and Last characters of String
    removeFirstLast1 = stringValue[1: -1]
    removeFirstLast2 = stringValue[1: len(stringValue) - 1]
    #Check if String is Alphabet
    stringAlphabet = "OnLyAlPhAbEt"
    checkAlphabet = stringAlphabet.isalpha()
    #Verify if String starts or ends with
    startsWith = message.startswith("Alpha")
    endsWith = message.endswith("Initialized")
    #Check if String is Upper Case or Lower Case
    upperString = "ALLCAPS"
    isUpper = upperString.isupper()
    lowerString = "alllower"
    isLower = lowerString.islower()

    #Array Operations
    #Get length of Array
    lengthArray = len(stringArray)
    #Create new placeholder Array of fixed length
    fixedArray = [0] * 5
    fixedArray[2] = 10
    #Create Two Dimensional Array
    twoDimArray = [[1, 2], [3, 4], [5, 6]]
    #Generate String from Array with delimiter
    joinedArray = " ".join(stringArray)
    #Reverse Array
    reverseArray1 = stringArray[::-1]
    reverseArray2 = reversed(stringArray)
    #Count occurrences in Array
    countArray = ["a", "b", "a", "c", "a"]
    occurrenceString = "a"
    occurrencesArray = countArray.count(occurrenceString)
    # Split String into Integer Array
    stringInt = '549713'
    stringToIntArray = [int(i) for i in stringInt]
    #Get Minimum and Maximum values from an Array
    minArray = min(integerArray)
    maxArray = max(integerArray)

    #Dictionary Operations
    #Declare a new dictionary
    dictionary = {}
    #Add entry to dictionary
    dictionary.update({"String": 1})

    #If statements
    condition = False
    if integerArray[0] == 1:
        condition = True
    else:
        condition = False
    #If statement with AND
    if integerArray[0] == 1 and integerArray[1] == 2:
        condition = True
    #If statement with OR
    if integerArray[0] == 1 or integerArray[1] == 2:
        condition = True

    #For Loops
    #For index in Array
    #For item in Array

    #OOP
    _alphaTwo = AlphaTwo()
    alphaTwoIntSum = _alphaTwo.sum_int_array(integerArray)

    #Integers


    #Strings
    #String Interpolation format is easier to work with
    print(f"String length for '{stringValue}' is {lengthString}")
    print(f"Reversed String is '{reverseString}'")
    print(f"Replace 'e' with 'E' only 3 times from '{nOccurrencesString}' is '{replaceNOccurrencesString}'")
    print(f"First character from '{stringValue}' is '{firstOfString}'")
    print(f"Last 3 characters from '{stringValue}' are '{lastOfString}'")
    print(f"Removing first and last characters from '{stringValue}' results in '{removeFirstLast1}' and '{removeFirstLast2}'")
    print(f"'{stringAlphabet}' contains only alphabet characters: {checkAlphabet}")
    print(f"'{replacedMessage}' starts with Alpha: '{str(startsWith)}' and ends with Initialized: '{str(endsWith)}'")
    print(f"'{upperString}' is all Upper Case: {isUpper}")
    print(f"'{lowerString}' is all Lower Case: {isLower}")

    #Arrays
    print(f"Joined Array is '{joinedArray}'")
    print(f"Reversed Array is '{" ".join(reverseArray1)}' or '{" ".join(reverseArray2)}'")
    print(f"Array '{countArray}' contains {occurrencesArray} occurrences of '{occurrenceString}'")
    print(f"Split '{stringInt}' to Int Array '{stringToIntArray}'")
    print(f"Minimum value of Array '{integerArray}' is {minArray}, Maximum value is {maxArray}")

    #Dictionaries

    #OOP
    print(f"After creating instance of Class AlphaTwo, using its method SumIntArray to calculate sum of '{integerArray}' is {alphaTwoIntSum}")
