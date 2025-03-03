#Press the green button in the gutter to run the script.
from AlphaTwo import AlphaTwo, function_min_array, void_function
from AlphaTwoSub import AlphaTwoSub
import math

if __name__ == '__main__':
    #Primitives
    integer = 16
    floatValue = 3.1417639
    booleanValue = True

    #Non Primitives
    #String
    message = "Alpha One Initialized"
    #Arrays are Lists in Python, ordered non-homogeneous, columns of a single or multiple rows, allows duplicate elements
    #Multiple primitive types are possible, compared to C# and JAVA
    integerArray = [1, 2, 3, 4, 5, 6, 7]
    stringArray = ["This", "is", "an", "Array", "from", "a", "String."]
    mixedArray = [1, "b", 3, "d"]
    #Tuple non-homogeneous, columns of a single or multiple rows, allows duplicate elements
    #Tuple is immutable, changes cannot be made
    declaredTuple = ("A", 1, [1,2,3])
    #Set non-homogeneous, single row, will not allow duplicate elements
    declaredSet = {1, 2, 3, 4, 5, 6, 7}
    #Dictionary non-homogeneous, stores key-value pairs, doesn’t allow duplicate keys
    emptyDictionary = {}
    declaredDictionary = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}

    #Integer Operations
    #Convert String to Integer
    stringNumber = "12345"
    intStringNumber = int(stringNumber)
    #Always return positive number
    negativeInteger = -4
    negativeToPositiveInteger = abs(negativeInteger)
    #Round number down
    math.ceil(floatValue)
    #Round number up
    math.floor(floatValue)
    #Check if number is a perfect square
    math.sqrt(integer)
    #Get difference between two numbers
    firstNumber = 40
    secondNumber = 13
    differenceBetween = abs(secondNumber - firstNumber)
    #Get current quarter of the year
    currentMonth = 5
    currentQuarter = math.ceil(currentMonth/3.0)

    #Character Operations

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
    #Append to Array
    #Generate Array from String
    #Generate String from Array with delimiter
    joinedArray = " ".join(stringArray)
    #Reverse Array
    reverseArray1 = stringArray[::-1]
    reverseArray2 = reversed(stringArray)
    #Count occurrences in Array
    countArray = ["a", "b", "a", "c", "a"]
    occurrenceString = "a"
    occurrencesArray = countArray.count(occurrenceString)
    #Split String into Integer Array
    stringInt = '549713'
    stringToIntArray = [int(i) for i in stringInt]
    #Get Minimum and Maximum values from an Array
    minArray = min(integerArray)
    maxArray = max(integerArray)
    #Sort an Array
    #Sum of Array
    #Average of Array
    #Multiply all elements of Array
    #Convert from Binary to base 10

    #Dictionary Operations
    #Add entry to dictionary
    declaredDictionary.update({"F": 6})

    #Enumerable Operations

    #Conditionals
    #If Else Statement
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
    #Switch
    switchString = "Green Light"
    waitForSwitch = ""
    match switchString:
        case "Yellow Light":
            waitForSwitch = "Wait for Red Light"
        case "Red Light":
            waitForSwitch = "Wait for Green Light"
        case _:
            waitForSwitch = "Wait for Yellow Light"

    #For Loops
    #For index in Array
    forLoopCount = 0
    for i in range(len(integerArray)):
        forLoopCount += integerArray[i]
    #For item in Array
    forEachString = ""
    for s in stringArray:
        forEachString += s
    #Count number of matching characters in a String
    matchingString = "We will count the number of vowels"
    countMatchingString = 0
    matchingStringArray = [s for s in matchingString]
    matchingVowels = ["a", "e", "i", "o", "u"]
    for i in range(len(matchingStringArray)):
        #Using .matches() with expression to count all vowels
        if matchingStringArray[i] in matchingVowels:
            countMatchingString += 1

    #While Loops
    #Calculate number of divisors in a number, example: 30 has 1, 2, 3, 5, 6, 10, 15 and 30
    intDivisors = 30
    numberOfDivisors = 1
    whileIterator = 1
    while whileIterator < intDivisors:
        #Check if number can be divided by iterator
        if intDivisors % whileIterator == 0:
            numberOfDivisors += 1
        whileIterator += 1

    #OOP
    #Public method requires Instance of Class
    _alphaTwo = AlphaTwo()
    alphaTwoIntSum = _alphaTwo.sum_int_array(integerArray)
    #Static method does not require Instance of Class
    alphaTwoIntAverage = AlphaTwo.average_int_array(integerArray)
    #Function needs to be imported separately in Python
    alphaTwoIntMin = function_min_array(integerArray)
    #Create instance of Inner Class
    _innerAlphaTwo = AlphaTwo.InnerAlphaTwo()
    innerAlphaTwoIntMin = _innerAlphaTwo.min_int_array(integerArray)
    _innerAlphaTwo.inner_alpha_two_set()
    #Create instance of Subclass(shorthand)
    _alphaTwoSub = AlphaTwoSub()
    #Subclass inherits method from Superclass
    alphaTwoSubIntSum = _alphaTwoSub.sum_int_array(_alphaTwoSub.alphaTwoIntArray)

    #Integers
    print("Integers")
    print(f"Current Month {currentMonth} is in Quarter: {currentQuarter}")

    #Characters
    print("\nCharacters")

    #Strings
    #String Interpolation format is easier to work with
    print("\nStrings")
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
    print("\nArrays")
    print(f"Joined Array is '{joinedArray}'")
    print(f"Reversed Array is '{" ".join(reverseArray1)}' or '{" ".join(reverseArray2)}'")
    print(f"Array '{countArray}' contains {occurrencesArray} occurrences of '{occurrenceString}'")
    print(f"Split '{stringInt}' to Int Array '{stringToIntArray}'")
    print(f"Minimum value of Array '{integerArray}' is {minArray}, Maximum value is {maxArray}")

    #Dictionaries
    print("\nDictionaries")
    print(f"This is a dictionary '{declaredDictionary}'")

    #Enumerable
    print("\nEnumerable")

    #Conditionals
    print("\nConditionals")

    #For Loops
    print("\nFor Loops")
    print(f"Using Index For Loop to count Array '{integerArray}' returns {forLoopCount}")
    print(f"Using Foreach Loop on every element in Array '{stringArray}' returns the following String '{forEachString}'")
    print(f"The number of vowels in '{matchingString}' is {countMatchingString}")

    #While Loops
    print("\nWhile Loops")
    print(f"The number {intDivisors} has {numberOfDivisors} divisors")

    #OOP
    print("\nOOP")
    print(f"After creating instance of Class AlphaTwo, using its method sum_int_array to calculate sum of '{integerArray}' is {alphaTwoIntSum}")
    print(f"Static method of Class AlphaTwo average_int_array used to calculate average of '{integerArray}' is {alphaTwoIntAverage}")
    _alphaTwo.void_alpha_two()
    void_function()
    print(f"Function of Class AlphaTwo min_int_array used to retrieve minimum value of '{integerArray}' is {alphaTwoIntMin}")
    _innerAlphaTwo.inner_alpha_two_get()
    print(f"Array Field from AlphaTwo is '{_alphaTwo.alphaTwoIntArray}', from AlphaTwoSub is '{_alphaTwoSub.alphaTwoIntArray}'")
    print(f"AlphaTwoSub is a Subclass and has inherited sum_int_array from AlphaTwo to sum '{_alphaTwoSub.alphaTwoIntArray}', resulting in {alphaTwoSubIntSum}")
    print(f"AlphaTwoSub's String has been reversed using Base Class' Method: '{_alphaTwoSub.alphaTwoSubString}'")
    print(_alphaTwo.outerAlphaTwoString)
