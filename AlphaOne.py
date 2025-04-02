#Press the green button in the gutter to run the script.
import unittest
import re
from itertools import product

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
        # Increment number with leading zeroes using zfill()
        intLeadingZeroes = "0001"
        strIncrementZeroes = str(int(intLeadingZeroes) + 1).zfill(len(intLeadingZeroes))

        print("Integers")
        print(f"Converting String '{stringNumber}' to Integer: {intStringNumber}")
        print(f"{forDivisionInt} can be divided by {divisorInt} a total of {divisionResultInt} times")
        print(f"Current Month {currentMonth} is in Quarter: {currentQuarter}")
        print(f"Increment {intLeadingZeroes} with leading zeroes by 1: {strIncrementZeroes}")

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
        # Replace part of String, will attempt to do so, but not break if not found
        replacedMessage = self.message.replace("One", "Prime")
        # Can string multiple .replace()
        replaceString = "51NGAP0RE"
        replaceString = replaceString.replace("5","S").replace("1","I").replace("0","O")
        # Replace multiple characters at once using REGEX, import re
        replaceMultiple = "This will be A String wIthoUt all vOwels"
        replacedMultiple = re.sub(r"[aeiouAEIOU]", "", replaceMultiple)
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
        # Remove part of String that comes after unique delimiter
        toRemoveAnchorString = "www.codewars.com#about"
        removedAnchorString = toRemoveAnchorString.split("#")[0]
        # Check if String is Alphabet
        stringAlphabet = "OnLyAlPhAbEt"
        checkAlphabet = stringAlphabet.isalpha()
        # Remove all non-alphabet or non-digit characters using [^'exclude'], C# requires Regex
        stringMixed = "ultr53o?n"
        removeDigits = re.sub(r"[^a-z]", "", stringMixed)
        removeAlphabet = re.sub(r"[^0-9]", "", stringMixed)
        # Verify if String starts or ends with
        startsWith = self.message.startswith("Alpha")
        endsWith = self.message.endswith("Initialized")
        # Check if String is Upper Case or Lower Case
        upperString = "ALLCAPS"
        isUpper = upperString.isupper()
        lowerString = "alllower"
        isLower = lowerString.islower()
        # Concatenate range from Array
        toConcatenateArray = ["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"]
        #2 is starting index and 6 is end of range
        stringConcatenated = "".join(toConcatenateArray[2:6])
        # Check if String contains substrings and remove them, leaving only domain: http://, https://, www
        urlString = "http://www.codewars.com/kata/"
        initialUrlString = urlString
        if "://" in urlString:
            urlString = urlString.split("://")[1]
        if urlString.startswith("www"):
            urlString = urlString.split(".")[1]
        else:
            urlString = urlString.split(".")[0]

        # String Interpolation format is easier to work with
        print("\nStrings")
        print(f"String length for '{stringValue}' is {lengthString}")
        print(f"Reversed String is '{reverseString}'")
        print(f"Removing all vowels from String '{replaceMultiple}' results in: '{replacedMultiple}'")
        print(f"Replace 'e' with 'E' only 3 times from '{nOccurrencesString}' is '{replaceNOccurrencesString}'")
        print(f"First character from '{stringValue}' is '{firstOfString}'")
        print(f"Last 3 characters from '{stringValue}' are '{lastOfString}'")
        print(f"Removing first and last characters from '{stringValue}' results in '{removeFirstLast1}' and '{removeFirstLast2}'")
        print(f"Remove from '{toRemoveAnchorString}' everything that comes after #: '{removedAnchorString}'")
        print(f"'{stringAlphabet}' contains only alphabet characters: {checkAlphabet}")
        print(f"'{stringMixed}' removing all non-digit characters: {removeAlphabet}")
        print(f"'{stringMixed}' removing all non-alphabet characters: {removeDigits}")
        print(f"'{replacedMessage}' starts with Alpha: '{str(startsWith)}' and ends with Initialized: '{str(endsWith)}'")
        print(f"'{upperString}' is all Upper Case: {isUpper}")
        print(f"'{lowerString}' is all Lower Case: {isLower}")
        print(f"Creating concatenated string from '[{", ".join(toConcatenateArray)}]' starting from index 2 and concatenating 4 elements: {stringConcatenated}")
        print(f"Domain part of URL '{initialUrlString}' is '{urlString}'")

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
        # Generate Array from String, remove .split() if String is not a sentence
        stringToArray = "This is an Array from a String."
        arrayFromString = [str(st) for st in stringToArray.split(" ")]
        # Generate String from Array with delimiter
        joinedStringArray = " ".join(self.stringArray)
        # Reverse Array requires .copy() in Python, otherwise the original might be mutated
        reverseArray1 = self.stringArray.copy()[::-1]
        reverseArray2 = reversed(self.stringArray.copy())
        # Count occurrences in Array
        occurrencesArray = ["a", "a", "b", "c", "d", "d", "e", "e", "f", "x", "x", "y", "y", "z",]
        occurrencesInArray = ["x", "y", "z"]
        occurrencesInArrayCount = 0
        for st in occurrencesArray:
            if st in occurrencesInArray:
                occurrencesInArrayCount += 1
        # Split Integer into Integer Array
        intForArray = 1234567
        intToArray = [int(i) for i in str(intForArray)]
        # Split String into Integer Array
        stringInt = '549713'
        stringToIntArray = [int(i) for i in stringInt]
        # Get Minimum and Maximum values from an Array
        minArray = min(self.integerArray)
        maxArray = max(self.integerArray)
        # Sum of Array
        sumArray = sum(self.integerArray)
        # Average of Array
        averageArray = sum(self.integerArray)/len(self.integerArray)
        # Multiply all elements of Array
        productArray = 1
        for num in self.integerArray:
            productArray *= num
        # Sort an Array
        unsortedArray = [9, 5, 2, 7, 1, 8, 3, 4]
        sortedArray = unsortedArray.copy()
        sortedArray.sort()
        # Iterate over object Array
        objArray = [1, 2, "3", "4"]
        objArraySum = 0
        for value in objArray:
            objArraySum += int(str(value))
        # Convert from Binary to base 10
        binaryArray = [0, 1, 0, 1]
        intConvertedFromBinary = 0
        for i in range(len(binaryArray)):
            intConvertedFromBinary += int(binaryArray[i] * math.pow(2, len(binaryArray) - i - 1))
        # Concatenate each entry N times from existing List
        toConcatenateArray = ["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"]
        intConcatenate = 3
        arrConcatenate = []
        for i in range(len(toConcatenateArray) - intConcatenate + 1):
            # i for starting range and i + intConcatenate for end of range
            toConcatenateSubList = toConcatenateArray[i:i + intConcatenate]
            stringConcatenated = "".join(toConcatenateSubList)
            arrConcatenate.append(stringConcatenated)

        print("\nArrays")
        print(f"Split String '{stringToArray}' into Array '{arrayFromString}'")
        print(f"String from joined Array is '{joinedStringArray}'")
        print(f"For '{self.stringArray}', Reversed Array is '{reverseArray1}' or '[{", ".join(reverseArray2)}]'")
        print(f"The characters '{occurrencesInArray}' appear in '{occurrencesArray}' a total of {occurrencesInArrayCount} times")
        print(f"Split {intForArray} to Int Array '{intToArray}'")
        print(f"Split '{stringInt}' to Int Array '{stringToIntArray}'")
        print(f"Minimum value of Array '{self.integerArray}' is {minArray}, Maximum value is {maxArray}")
        print(f"For Integer Array '{self.integerArray}', Sum is '{sumArray}', Average is '{averageArray}' and Product is'{productArray}'")
        print(f"Unsorted Array is '{unsortedArray}', sorted Array is '{sortedArray}'")
        print(f"Sum of Object Array '{objArray}'] is {objArraySum}")
        print(f"Converting binary number {binaryArray} to base 10 number is {intConvertedFromBinary}")
        print(f"Creating a new Array from '[{", ".join(toConcatenateArray)}]' and concatenating {intConcatenate} times: '[{", ".join(arrConcatenate)}]'")

    def testSets(self):
        """test case B"""
        # Set Operations
        print("\nSets")
        print(f"This is a Set and it only contains unique values '{self.declaredSet}'")

    def testDictionaries(self):
        """test case B"""
        # Dictionary Operations
        # Add entry to dictionary
        self.declaredDictionary.update({"F": 6})
        # Count occurrences in a String(Ness)
        stringOccurrences = "abcadcbba"
        dictOccurrences = {}
        arrOccurrences = [str(st) for st in stringOccurrences]
        for i in range(len(arrOccurrences)):
            if arrOccurrences[i] not in dictOccurrences:
                dictOccurrences.update({arrOccurrences[i]: 1})
            else:
                dictOccurrences[arrOccurrences[i]] += 1

        print("\nDictionaries")
        print(f"This is a Dictionary '{self.declaredDictionary}'")
        print(f"Getting occurrences of each character from String '{stringOccurrences}' as Dictionary {dictOccurrences}")

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
        # Reverse For Loop
        reverseLoopArray = []
        for i in range(len(self.integerArray) - 1, -1, -1):
            reverseLoopArray += str(self.integerArray[i])
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
        print(f"Using Foreach Loop on every element in Array '{self.stringArray}' returns the following String '{forEachString}'")
        print(f"Using Reverse For Loop to created Reversed Array: {reverseLoopArray}")
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
