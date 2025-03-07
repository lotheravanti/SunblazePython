#Press the green button in the gutter to run the script.
import unittest
from AlphaTwo import AlphaTwo, function_min_array, void_function
from AlphaTwoSub import AlphaTwoSub
import math

class AlphaOne(unittest.TestCase):
    # Primitives
    integer = 16
    floatValue = 3.1417639
    booleanValue = True

    # Non Primitives
    # String
    message = "Alpha One Initialized"
    # Arrays are Lists in Python, ordered non-homogeneous, columns of a single or multiple rows, allows duplicate elements
    # Multiple primitive types are possible, compared to C# and JAVA
    integerArray = [1, 2, 3, 4, 5, 6, 7]
    stringArray = ["This", "is", "an", "Array", "from", "a", "String."]
    mixedArray = [1, "b", 3, "d"]
    # Tuple non-homogeneous, columns of a single or multiple rows, allows duplicate elements
    # Tuple is immutable, changes cannot be made
    declaredTuple = ("A", 1, [1, 2, 3])
    # Set non-homogeneous, single row, will not allow duplicate elements
    declaredSet = {1, 2, 3, 4, 5, 6, 7}
    # Dictionary non-homogeneous, stores key-value pairs, doesn’t allow duplicate keys
    emptyDictionary = {}
    declaredDictionary = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}

    def setUp(self):
        """Call before every test case."""


    def tearDown(self):
        """Call after every test case."""


    def testIntegers(self):
        """Integer Operations
        Note that all test method names must begin with 'test.'"""
        #assert foo.bar() == 543, "bar() not calculating values correctly"
        # Integer Operations
        # Convert String to Integer
        stringNumber = "12345"
        intStringNumber = int(stringNumber)
        # Always return positive number
        negativeInteger = -4
        negativeToPositiveInteger = abs(negativeInteger)
        # Round number down
        math.ceil(self.floatValue)
        # Round number up
        math.floor(self.floatValue)
        # Dividing two Integers will always return a whole number
        forDivisionInt = 10
        divisorInt = 3
        divisionResultInt = int(forDivisionInt / divisorInt)
        # Get number at the power of N
        numberForPower = 7
        powerN = 2
        numberAtPowerN = numberForPower ** powerN
        # Check if number is a perfect square
        math.sqrt(self.integer)
        # Get difference between two numbers
        firstNumber = 40
        secondNumber = 13
        differenceBetween = abs(secondNumber - firstNumber)
        # Get current quarter of the year
        currentMonth = 5
        currentQuarter = math.ceil(currentMonth / 3.0)

        print("Integers")
        print(f"Converting String '{stringNumber}' to Integer: {intStringNumber}")
        print(f"{forDivisionInt} can be divided by {divisorInt} a total of {divisionResultInt} times")
        print(f"Current Month {currentMonth} is in Quarter: {currentQuarter}")

    def testCharacters(self):
        """test case B"""
        print("\nCharacters")

    def testStrings(self):
        """String OperationsB"""
        stringValue = "lower case text"
        # Get length of String
        lengthString = len(stringValue)
        # Convert to Upper Case
        upperCase = stringValue.upper()
        # Reverse String
        reverseString = stringValue[::-1]
        # Replace part of String
        replacedMessage = self.message.replace("One", "Prime")
        # Replace only N occurrences of String
        nOccurrencesString = "every e in the sentence"
        replaceNOccurrencesString = nOccurrencesString.replace("e", "E", 3)
        # Get first N characters of a String
        firstOfString = stringValue[0:1]
        # Get last N characters of a String
        lastOfString = stringValue[-3:]
        # Remove First and Last characters of String
        removeFirstLast1 = stringValue[1: -1]
        removeFirstLast2 = stringValue[1: len(stringValue) - 1]
        # Check if String is Alphabet
        stringAlphabet = "OnLyAlPhAbEt"
        checkAlphabet = stringAlphabet.isalpha()
        # Verify if String starts or ends with
        startsWith = self.message.startswith("Alpha")
        endsWith = self.message.endswith("Initialized")
        # Check if String is Upper Case or Lower Case
        upperString = "ALLCAPS"
        isUpper = upperString.isupper()
        lowerString = "alllower"
        isLower = lowerString.islower()

        # String Interpolation format is easier to work with
        print("\nStrings")
        print(f"String length for '{stringValue}' is {lengthString}")
        print(f"Reversed String is '{reverseString}'")
        print(f"Replace 'e' with 'E' only 3 times from '{nOccurrencesString}' is '{replaceNOccurrencesString}'")
        print(f"First character from '{stringValue}' is '{firstOfString}'")
        print(f"Last 3 characters from '{stringValue}' are '{lastOfString}'")
        print(
            f"Removing first and last characters from '{stringValue}' results in '{removeFirstLast1}' and '{removeFirstLast2}'")
        print(f"'{stringAlphabet}' contains only alphabet characters: {checkAlphabet}")
        print(
            f"'{replacedMessage}' starts with Alpha: '{str(startsWith)}' and ends with Initialized: '{str(endsWith)}'")
        print(f"'{upperString}' is all Upper Case: {isUpper}")
        print(f"'{lowerString}' is all Lower Case: {isLower}")

    def testArrays(self):
        """Array Operations"""
        # Get length of Array
        lengthArray = len(self.stringArray)
        # Create new placeholder Array of fixed length
        fixedArray = [0] * 5
        fixedArray[2] = 10
        # Create Two Dimensional Array
        twoDimArray = [[1, 2], [3, 4], [5, 6]]
        # Append one item to Array
        self.integerArray.append(8)
        # Append multiple items to Array
        self.integerArray.extend([9, 10])
        # Remove item by index from Array
        self.integerArray.pop(9)
        # Generate Array from String
        # Generate String from Array with delimiter
        joinedArray = " ".join(self.stringArray)
        # Reverse Array
        # In Python use .copy() to create a new variable, otherwise the original might be mutated
        reverseArray1 = self.stringArray.copy()[::-1]
        reverseArray2 = reversed(self.stringArray.copy())
        # Count occurrences in Array
        countArray = ["a", "b", "a", "c", "a"]
        occurrenceString = "a"
        occurrencesArray = countArray.count(occurrenceString)
        # Split String into Integer Array
        stringInt = '549713'
        stringToIntArray = [int(i) for i in stringInt]
        # Get Minimum and Maximum values from an Array
        minArray = min(self.integerArray)
        maxArray = max(self.integerArray)
        # Sort an Array
        # Sum of Array
        # Average of Array
        # Multiply all elements of Array
        # Convert from Binary to base 10

        print("\nArrays")
        print(f"Joined Array is '{joinedArray}'")
        print(f"Reversed Array is '{" ".join(reverseArray1)}' or '{" ".join(reverseArray2)}'")
        print(f"Array '{countArray}' contains {occurrencesArray} occurrences of '{occurrenceString}'")
        print(f"Split '{stringInt}' to Int Array '{stringToIntArray}'")
        print(f"Minimum value of Array '{self.integerArray}' is {minArray}, Maximum value is {maxArray}")

    def testDictionaries(self):
        """test case B"""
        # Dictionary Operations
        # Add entry to dictionary
        self.declaredDictionary.update({"F": 6})

        print("\nDictionaries")
        print(f"This is a dictionary '{self.declaredDictionary}'")

    def testEnumerables(self):
        """Enumerable Operations"""
        print("\nEnumerable")

    def testConditionals(self):
        """Conditionals"""
        # If Else Statement
        condition = False
        if self.integerArray[0] == 1:
            condition = True
        else:
            condition = False
        # If statement with AND
        if self.integerArray[0] == 1 and self.integerArray[1] == 2:
            condition = True
        # If statement with OR
        if self.integerArray[0] == 1 or self.integerArray[1] == 2:
            condition = True
        # Switch
        switchString = "Green Light"
        waitForSwitch = ""
        match switchString:
            case "Yellow Light":
                waitForSwitch = "Wait for Red Light"
            case "Red Light":
                waitForSwitch = "Wait for Green Light"
            case _:
                waitForSwitch = "Wait for Yellow Light"

        print("\nConditionals")

    def testForLoops(self):
        """For Loops"""
        # For index in Array
        forLoopCount = 0
        for i in range(len(self.integerArray)):
            forLoopCount += self.integerArray[i]
        # For item in Array
        forEachString = ""
        for s in self.stringArray:
            forEachString += s
        # Count number of matching characters in a String
        matchingString = "We will count the number of vowels"
        countMatchingString = 0
        matchingStringArray = [s for s in matchingString]
        matchingVowels = ["a", "e", "i", "o", "u"]
        for i in range(len(matchingStringArray)):
            # Using .matches() with expression to count all vowels
            if matchingStringArray[i] in matchingVowels:
                countMatchingString += 1

        print("\nFor Loops")
        print(f"Using Index For Loop to count Array '{self.integerArray}' returns {forLoopCount}")
        print(
            f"Using Foreach Loop on every element in Array '{self.stringArray}' returns the following String '{forEachString}'")
        print(f"The number of vowels in '{matchingString}' is {countMatchingString}")

    def testWhileLoops(self):
        """While Loops"""
        # Calculate number of divisors in a number, example: 30 has 1, 2, 3, 5, 6, 10, 15 and 30
        intDivisors = 30
        numberOfDivisors = 1
        whileIterator = 1
        while whileIterator < intDivisors:
            # Check if number can be divided by iterator
            if intDivisors % whileIterator == 0:
                numberOfDivisors += 1
            whileIterator += 1

        print("\nWhile Loops")
        print(f"The number {intDivisors} has {numberOfDivisors} divisors")

    def testOOP(self):
        """OOP"""
        # Public method requires Instance of Class
        _alphaTwo = AlphaTwo()
        alphaTwoIntSum = _alphaTwo.sum_int_array(self.integerArray)
        # Static method does not require Instance of Class
        alphaTwoIntAverage = AlphaTwo.average_int_array(self.integerArray)
        # Function needs to be imported separately in Python
        alphaTwoIntMin = function_min_array(self.integerArray)
        # Create instance of Inner Class
        _innerAlphaTwo = AlphaTwo.InnerAlphaTwo()
        innerAlphaTwoIntMin = _innerAlphaTwo.min_int_array(self.integerArray)
        _innerAlphaTwo.inner_alpha_two_set()
        # Create instance of Subclass(shorthand)
        _alphaTwoSub = AlphaTwoSub()
        # Subclass inherits method from Superclass
        alphaTwoSubIntSum = _alphaTwoSub.sum_int_array(_alphaTwoSub.alphaTwoIntArray)

        print("\nOOP")
        print(f"After creating instance of Class AlphaTwo, using its method sum_int_array to calculate sum of '{self.integerArray}' is {alphaTwoIntSum}")
        print(f"Static method of Class AlphaTwo average_int_array used to calculate average of '{self.integerArray}' is {alphaTwoIntAverage}")
        _alphaTwo.void_alpha_two()
        void_function()
        print(f"Function of Class AlphaTwo min_int_array used to retrieve minimum value of '{self.integerArray}' is {alphaTwoIntMin}")
        _innerAlphaTwo.inner_alpha_two_get()
        print(f"Array Field from AlphaTwo is '{_alphaTwo.alphaTwoIntArray}', from AlphaTwoSub is '{_alphaTwoSub.alphaTwoIntArray}'")
        print(f"AlphaTwoSub is a Subclass and has inherited sum_int_array from AlphaTwo to sum '{_alphaTwoSub.alphaTwoIntArray}', resulting in {alphaTwoSubIntSum}")
        print(f"AlphaTwoSub's String has been reversed using Base Class' Method: '{_alphaTwoSub.alphaTwoSubString}'")
        print(_alphaTwo.outerAlphaTwoString)

if __name__ == '__main__':
    print(f"Starting Tests")
    unittest.main()
    print(f"Test(s) completed")
