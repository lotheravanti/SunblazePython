#Press the green button in the gutter to run the script.
import datetime
import math
import re
import unittest
import numpy as np
from collections import OrderedDict
from datetime import date
from itertools import combinations
from itertools import product

from AlphaTwo import AlphaTwo, function_min_array, void_function
from AlphaTwoSub import AlphaTwoSub


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
        # Check if String is number
        stringNumber = "12345"
        stringIsNumber = stringNumber.isnumeric()
        # Convert String to Integer
        intStringNumber = int(stringNumber)
        # Always return positive number
        negativeInteger = -4
        negativeToPositiveInteger = abs(negativeInteger)
        # Round number down
        math.ceil(self.floatValue)
        # Round number up
        math.floor(self.floatValue)
        # Round number to 2 decimal places
        intNumberForRound = 1.23456
        intRoundedNumber = round(intNumberForRound,2)
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
        # Add leading zeroes
        intForZeroes = 1
        strAddLeadingZeroes = f"{intForZeroes:05d}"
        # Increment number with leading zeroes using zfill()
        leadingZeroes = "0001"
        incrementZeroes = str(int(leadingZeroes) + 1).zfill(len(leadingZeroes))
        # Generate Fibonacci sequence up to a number
        numForFib = 200
        fibArr = [0, 1]
        while fibArr[-1] + fibArr[-2] <= numForFib:
            fibArr.append(fibArr[-1] + fibArr[-2])

        print("\nIntegers")
        print(f"Checking String '{stringNumber}' is number: {stringIsNumber}")
        print(f"Converting String '{stringNumber}' to Integer: {intStringNumber}")
        print(f"Rounding number '{intNumberForRound}' to 2 decimals: {intRoundedNumber}")
        print(f"{forDivisionInt} can be divided by {divisorInt} a total of {divisionResultInt} times")
        print(f"Current Month {currentMonth} is in Quarter: {currentQuarter}")
        print(f"For number {intForZeroes}, adding 4 leading zeroes: {strAddLeadingZeroes}")
        print(f"Increment {leadingZeroes} with leading zeroes by 1: {incrementZeroes}")
        print(f"Generate Fibonacci sequence up to {numForFib} results in: {fibArr}")

    def testCharacters(self):
        """Character Operations"""
        # Convert character to number
        charArray = ["a", "b", "c", "x", "y", "z"]
        numFromCharArray = [ord(st) - 96 for st in charArray]
        numForCharArray = [1, 2, 3, 4]
        charFromNumArray = [chr(i + 96) for i in numForCharArray]

        print("\nCharacters")
        print(f"Converting letters from Array {charArray} to numbers: {numFromCharArray}")
        print(f"Converting numbers from Array {numForCharArray} to letters: {charFromNumArray}")

    def testStrings(self):
        """String Operations"""
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
        # Replace multiple characters at once with REGEX, using import re
        replaceMultiple = "This will be A String wIthoUt all vOwels"
        replacedMultiple = re.sub(r"[aeiouAEIOU]", "", replaceMultiple)
        # Replacing multiple characters each with a different corresponding value using Translation where a Switch would have been used
        stringForTranslate = "Hello this would be a Translation"
        translationCipher = str.maketrans("aeiou", "12345") # Replace all vowels with numbers
        translationString = stringForTranslate.translate(translationCipher)
        stringPolishDiacritics = "Jędrzej Błądziński"
        stringRemovePolish = stringPolishDiacritics.translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))
        # Add a character N times to a String
        fiveStars = "*" * 5
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
        # Remove last same characters of String
        stringEndSame = "Hello!!!!!!!!!!!!!"
        stringEndSameRemove = stringEndSame.rstrip("!")
        # Remove part of String that comes after unique delimiter
        toRemoveAnchorString = "www.codewars.com#about"
        removedAnchorString = toRemoveAnchorString.split("#")[0]
        # Check if String is Alphabet
        stringAlphabet = "OnLyAlPhAbEt"
        checkAlphabet = stringAlphabet.isalpha()
        # Count number of instances of a Character in String
        countString = "n___nnnn____n_"
        countCharInString = countString.count('n')
        # Check if String contains any characters other than specified combination and also of certain length
        matchCharactersString = "regex_34"
        noMatchCharactersString = "H 3"
        removeDigitsPattern = "[a-z0-9_]{4,16}"
        matchCharactersBool = bool(re.match(removeDigitsPattern, matchCharactersString)) # cast to boolean
        noMatchCharactersBool = bool(re.match(removeDigitsPattern, noMatchCharactersString))
        # Check if String contains any of the following
        stringContains = "The number 3.50 can be spelled Three Fifty"
        stringContainsBool1 = any(i in stringContains for i in ('three fifty', '3.50'))
        stringContainsBool2 = bool(re.search(r"3\.50|three fifty", stringContains)) # using import re
        # Remove all non-alphabet or non-digit characters using [^'exclude'], using import re
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
        # Swap case of letters
        stringForSwap = "aBcDE"
        stringSwapped = stringForSwap.swapcase()
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
        # Single line String Join with conditions replace each single occurrence with (, otherwise ), case-insensitive
        stringForSingleLine = "@qc!@!CGqDjc@wBbz"
        stringSingleLine = "".join(["(" if stringForSingleLine.lower().count(c) == 1 else ")" for c in stringForSingleLine.lower()])
        # Get every Substring of a String
        stringForSub = "aba12321abba"
        arrSubs = [stringForSub[i:j] for i in range(len(stringForSub)) for j in range(i + 1, len(stringForSub) + 1)]
        # Get all Palindromes for Array of Substrings
        arrPalindromes = [st for st in arrSubs if st == st[::-1] and len(st) > 2]
        # Get Substrings that contain only vowels using import re
        stringWithVowels = "ultrarevolutionariees"
        vowelsArray = re.findall(r"[aeiou]+", stringWithVowels)
        # Perform arithmetical operations on String
        arithmString = "1+2*3-4/2"
        arithmNumber = eval(arithmString)
        # Parsing date from string using import datetime
        dateUnparsed1 = "July 2, 2015" #notice date has comma
        dateUnparsed2 = "July 9, 2015"
        dateParsed1 = datetime.datetime.strptime(dateUnparsed1,'%B %d, %Y').strftime('%d/%m/%Y') #can specify format from input with any delimiters like spaces, - and ,
        dateParsed2 = datetime.datetime.strptime(dateUnparsed2,'%B %d, %Y').strftime('%d/%m/%Y') #can specify output format with strftime
        checkDates = dateParsed1 < dateParsed2
        # Get number of days between 2 dates
        date1 = date(2020, 1, 1)
        date2 = date(2020,10,31)
        numDays = (date2 - date1).days
        # Generate custom String from sorted Array with "".join
        nameArray = [('ARNO', 'ALEX'), ('KERN', 'ANN'), ('BELL', 'SARAH'), ('DORNY', 'PAUL'), ('DORRIES', 'ANDREW'), ('CORNWELL', 'ALISSA'), ('KERN', 'MADISON'), ('ARNO', 'HALEY')]
        sortedName = ''.join(f'({a}, {b})' for a, b in sorted(nameArray))

        # String Interpolation format is easier to work with
        print("\nStrings")
        print(f"String length for '{stringValue}' is {lengthString}")
        print(f"Reversed String is '{reverseString}'")
        print(f"Removing all vowels from String '{replaceMultiple}' results in: '{replacedMultiple}'")
        print(f"Replacing all vowels with numbers from '{stringForTranslate}' using Translation results in: '{translationString}'")
        print(f"From Polish name '{stringPolishDiacritics}' removing all diacritics: '{stringRemovePolish}'")
        print(f"Generating strings with 5 times the character *: '{fiveStars}'")
        print(f"Replace 'e' with 'E' only 3 times from '{nOccurrencesString}' is '{replaceNOccurrencesString}'")
        print(f"First character from '{stringValue}' is '{firstOfString}'")
        print(f"Last 3 characters from '{stringValue}' are '{lastOfString}'")
        print(f"Removing first and last characters from '{stringValue}' results in '{removeFirstLast1}' and '{removeFirstLast2}'")
        print(f"Removing any number of the same character at the end of a String '{stringEndSame}' results in '{stringEndSameRemove}'")
        print(f"Remove from '{toRemoveAnchorString}' everything that comes after #: '{removedAnchorString}'")
        print(f"'{stringAlphabet}' contains only alphabet characters: {checkAlphabet}")
        print(f"The character 'n' appears {countCharInString} times in String '{countString}'")
        print(f"'{matchCharactersString}' has length between 4 and 6 and only contains lowercase alphabet,_ and numbers: {matchCharactersBool}")
        print(f"'{noMatchCharactersString}' has length between 4 and 6 and only contains lowercase alphabet,_ and numbers: {noMatchCharactersBool}")
        print(f"'{stringContains}' contains '3.50' or 'Three Fifty' {stringContainsBool1} and {stringContainsBool2}")
        print(f"'{stringMixed}' removing all non-digit characters: {removeAlphabet}")
        print(f"'{stringMixed}' removing all non-alphabet characters: {removeDigits}")
        print(f"'{replacedMessage}' starts with Alpha: '{str(startsWith)}' and ends with Initialized: '{str(endsWith)}'")
        print(f"'{upperString}' is all Upper Case: {isUpper}")
        print(f"'{lowerString}' is all Lower Case: {isLower}")
        print(f"'{stringForSwap}' with Case swapped is : {stringSwapped}")
        print(f"Creating concatenated string from '[{", ".join(toConcatenateArray)}]' starting from index 2 and concatenating 4 elements: {stringConcatenated}")
        print(f"Domain part of URL '{initialUrlString}' is '{urlString}'")
        print(f"From '{stringForSingleLine}' replace every single occurrence with (, otherwise ): {stringSingleLine}")
        print(f"From String '{stringForSub}' generate every Substring and select longest Palindrome '{max(arrPalindromes)}'")
        print(f"From String '{stringWithVowels}' get all Substrings containing only vowels '{vowelsArray}'")
        print(f"With String '{arithmString}' return result of arithmetical operations: '{arithmNumber}'")
        print(f"Parsing dates '{dateUnparsed1}' and '{dateUnparsed2}: '{dateParsed1}' and '{dateParsed2}'")
        print(f"Checking if '{dateParsed1}' is before '{dateParsed2}': {checkDates}")
        print(f"The number of days between '{date2}' and '{date1}' is: {numDays}")
        print(f"'Sorting Array of names '{nameArray}' \nby Last Name, then First Name as String: {sortedName}")

    def testREGEX(self):
        """REGEX Operations"""
        # Using import re
        fileName = "1231231223123131_BIG_FILE_NAME_HERE.EXTENSION.OTHEREXTENSION23423423"
        # Match group of numbers(or +), first result
        regNumberOne = re.match(r'\d+', fileName).group(0)
        regNumberOneAlt = re.search(r'\d+', fileName).group(0)
        # Get all numbers from a String
        regStringNumbers = "a 54b.i2...11ghl345"
        regSumNumbers = sum(int(x) for x in re.findall(r"(\d+)", regStringNumbers))
        # Match group of numbers, all results
        regNumberAll = re.findall(r'\d+', fileName)
        # Match first file extension, first result between '.' and '.'
        regExt = re.match(r'.*?\.(.*)\..*', fileName).group(1)
        regExtAlt = re.search(r'\.(.*)\.', fileName).group(1)
        # Match all file extensions
        regExtAll = re.findall(r'\.+\w+', fileName)
        # Match all substrings between two delimiters.
        # In order for findall to not 'consume' the results and thus excluding valid consecutive matches, use (?=expression)
        consumeText = "This is_an_example and_that_is_it."
        regExtAllConsumed = regExtAllConsumed = re.findall(r"[_]{1}(.*?)[_]{1}", consumeText)
        regExtAllNotConsumed = re.findall(r"(?=[_]{1}(.*?)[_]{1})", consumeText)
        # Find date format in text. Here we specify a number of a certain length with \d, example \d{4} for the year
        # We can also specify between different lengths to include cases with missing leading zeroes: \d{1,2}
        datesText = "The war lasted from 1939-01-4 to 1945-08-15, but on 1946-1-30 it started again"
        regDates = re.findall(r"\d{4}-\d{1,2}-\d{1,2}", datesText)

        print("\nREGEX")
        print(f"From {fileName} using REGEX to get first number found: {regNumberOne} or {regNumberOneAlt}")
        print(f"From '{regStringNumbers}' using REGEX to get add all numbers: {regSumNumbers}")
        print(f"From {fileName} using REGEX to get all numbers found: {regNumberAll}")
        print(f"From {fileName} using REGEX to get the first file extension : {regExt} or {regExtAlt}")
        print(f"From {fileName} using REGEX to get all file extensions : {regExtAll}")
        print(f"From {consumeText} using REGEX to get all substrings between _ and _ consuming the results : {regExtAllConsumed}")
        print(f"From {consumeText} using REGEX to get all substrings between _ and _ not consuming the results : {regExtAllNotConsumed}")
        print(f"From {datesText} using REGEX to get all dates found, even those with missing leading zeroes: {regDates}")

    def testArrays(self):
        """Array Operations"""
        # Arrays in Python are Lists
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
        # Get index of item in array
        arrNeedle = ["hay", "hay", "hay", "hay", "needle", "hay", "hay"]
        indexNeedle =  arrNeedle.index("needle")
        # Generate Array from String, remove .split() if String is not a sentence
        stringToArray = "This is an Array from a String."
        arrayFromString = [str(st) for st in stringToArray.split(" ")]
        # Generate String from Array with delimiter
        joinedStringArray = " ".join(self.stringArray)
        # Reverse Array requires .copy() in Python, otherwise the original might be mutated
        reverseArray1 = self.stringArray.copy()[::-1]
        reverseArray2 = reversed(self.stringArray.copy())
        # Compare if two Arrays are equal
        equalArray1 = [ 1, 2, 3, 4 ]
        equalArray2 = [ 1, 2, 3, 4 ]
        equalArray3 = [ 1, 2, 5, 4 ]
        equalsArr1Arr2 = equalArray1 == equalArray2
        equalsArr1Arr3 = equalArray1 == equalArray3
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
        sortedArray = sorted(unsortedArray.copy())
        # Generate Array of numbers with Step
        startStep = 2
        endStep = 10
        arrStep = [i for i in range(startStep, endStep + 1, 2)] # (start, end, step)
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
        # Iterate over possible combinations of array using from itertools import combinations
        iterArray = [45,32,98,101,76,5]
        sumComboIter = [sum(combo) for combo in combinations(iterArray, 3)] # every combination of 3 elements
        # Closest value in an array to a given value
        closestIterValue = min(sumComboIter, key=lambda x: abs(149 - x))
        # Find unique element coordinate in 2D array using numpy as np
        mazeArr = [[1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 3],
                [1, 0, 1, 0, 1, 0, 1],
                [0, 0, 1, 0, 0, 0, 1],
                [1, 0, 1, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 2, 1, 0, 1, 0, 1]]
        mazeStart = (0, 0)
        arrNump = np.array(mazeArr)
        for index, item in np.ndenumerate(arrNump):
            if item == 2:
                mazeStart = index
        mazeStart = list(mazeStart) # convert from tuple to list
        coordElem = [mazeStart[0], mazeStart[1]]
        # Navigate through the 2D array following directions
        mazeDir = ["N", "N", "N", "N", "N", "E", "E", "E", "E", "E"]
        for d in mazeDir:
            match d:
                case "N":
                    coordElem[0] -= 1
                case "S":
                    coordElem[0] += 1
                case "E":
                    coordElem[1] += 1
                case "W":
                    coordElem[1] -= 1
        mazeEnd = mazeArr[coordElem[0]][coordElem[1]]

        print("\nArrays(Lists)")
        print(f"From '{arrNeedle}' getting index position of 'needle': {indexNeedle}")
        print(f"Split String '{stringToArray}' into Array '{arrayFromString}'")
        print(f"String from joined Array is '{joinedStringArray}'")
        print(f"For '{self.stringArray}', Reversed Array is '{reverseArray1}' or '[{", ".join(reverseArray2)}]'")
        print(f"Array '{equalArray1}' is equal to Array '{equalArray2}': {equalsArr1Arr2}")
        print(f"Array '{equalArray1}' is equal to Array '{equalArray3}': {equalsArr1Arr3}")
        print(f"The characters '{occurrencesInArray}' appear in '{occurrencesArray}' a total of {occurrencesInArrayCount} times")
        print(f"Split {intForArray} to Int Array '{intToArray}'")
        print(f"Split '{stringInt}' to Int Array '{stringToIntArray}'")
        print(f"Minimum value of Array '{self.integerArray}' is {minArray}, Maximum value is {maxArray}")
        print(f"For Integer Array '{self.integerArray}', Sum is '{sumArray}', Average is '{averageArray}' and Product is'{productArray}'")
        print(f"Unsorted Array is '{unsortedArray}', sorted Array is '{sortedArray}'")
        print(f"Generating Array of numbers from 2 to 10 with Step of 2: {arrStep}")
        print(f"Sum of Object Array '{objArray}'] is {objArraySum}")
        print(f"Converting binary number {binaryArray} to base 10 number is {intConvertedFromBinary}")
        print(f"Creating a new Array from '[{", ".join(toConcatenateArray)}]' and concatenating {intConcatenate} times: '[{", ".join(arrConcatenate)}]'")
        print(f"From Array '{iterArray}' sums of all possible combinations of 3 is '{sorted(sumComboIter)}'")
        print(f"From Array of Combinations '{sorted(sumComboIter)}' value closest to '149' is '{closestIterValue}'")
        print(f"Navigating through maze starting element element {mazeArr[mazeStart[0]][mazeStart[1]]} at {mazeStart} to {mazeEnd} at {coordElem}")

    def testSets(self):
        """Set Operations"""
        # Create ordered Set requires collections import OrderedDict
        strForSet = "abracadabra"
        letterCountSet = {f"{s}: {strForSet.count(s)}" for s in OrderedDict.fromkeys(strForSet)}
        print("\nSets")
        print(f"This is a Set and it only contains unique values '{self.declaredSet}'")
        print(f"Counting every letter in '{strForSet}' and returning as Set: {letterCountSet}")

    def testTupples(self):
        """Set Operations"""
        strForTupple = "abracadabra"
        letterCountTupple = [(s, strForTupple.count(s)) for s in OrderedDict.fromkeys(strForTupple)]
        print("\nTupples")
        print(f"Counting every letter in '{strForTupple}' and returning as Tupple: {letterCountTupple}")

    def testDictionaries(self):
        """Dictionary Operations"""
        # Create new Dictionary
        newDict = {}
        # Add items to Dictionary
        self.declaredDictionary.update({"F": 6})
        newDict.update({"oranges": 4})
        newDict.update({"pears": 1})
        newDict.update({"apples": 2})
        newDict.update({"bananas": 3})
        # Get value from Dictionary
        bananaCount = newDict["bananas"]
        # Get entry at index of Dictionary
        newDictEntryAtIndex = (list(newDict)[0], list(newDict.values())[0])
        # Sort Dictionary by Value using Lambda function
        newDictSortedByValue = dict(sorted(newDict.items(), key=lambda item: item[1]))
        # Sort Dictionary by Key
        newDictSortedByKey = dict(sorted(newDict.items()))
        # Count occurrences in a String(Ness)
        stringOccurrences = "abcadcbba"
        dictOccurrences = {}
        arrOccurrences = [str(st) for st in stringOccurrences]
        for i in range(len(arrOccurrences)):
            if arrOccurrences[i] not in dictOccurrences:
                dictOccurrences.update({arrOccurrences[i]: 1})
            else:
                dictOccurrences[arrOccurrences[i]] += 1
        # Get median of values from dictionary
        dictForMedian = {"a":2, "b":3, "c":2, "d":1}
        medianDict = sum(dictForMedian.values())/len(dictForMedian)

        print("\nDictionaries")
        print(f"This is a Dictionary '{self.declaredDictionary}'")
        print(f"From '{newDict}' getting the number of bananas: {bananaCount}")
        print(f"From '{newDict}' get Value at Index 0: {newDictEntryAtIndex}")
        print(f"Sorting '{newDict}' by Value: '{newDictSortedByValue}'")
        print(f"Sorting '{newDict}' by Key: '{newDictSortedByKey}'")
        print(f"Getting occurrences of each character from String '{stringOccurrences}' as Dictionary {dictOccurrences}")
        print(f"Median of values from '{dictForMedian}' is : {medianDict}")

    def testEnumerables(self):
        """Enumerable Operations"""
        # Create an Array with conditions
        # Get every odd element(first, third, fith, etc), since i starts at zero, the expression % will be for even indexes
        arrForCondition = [4, 1, 1, 3, 2, 3]
        arrCondition = [j for i,j in enumerate(arrForCondition) if i % 2 == 0] # i is the iterator and j is the element itself
        # Create copy of Array except for an index
        indexExclude = 2
        arrMinusIndex = [x for i,x in enumerate(arrForCondition) if i != indexExclude]
        # Reverse every other word in a String
        stringForReverse = "This is a String that will have words reversed"
        arrReversedOther = " ".join([y[::-1] if x % 2 else y for x, y in enumerate(stringForReverse.split())])
        # Get only numbers or letters from array, two methods
        arrMixed = ["a", "1", "b", "2", "c", "3"]
        arrNumbers = [i for i in arrMixed if i.isnumeric()]
        # Filter creates a stream that runs every argument in an Array through a function
        def isLetter(st):
            return st.isalpha()
        arrLettersStream = filter(isLetter, arrMixed)
        arrLetters = [i for i in arrLettersStream] # Creating readable Array from Stream

        print("\nEnumerable")
        print(f"From '{arrForCondition}' get every odd element: '{arrCondition}'")
        print(f"From '{arrForCondition}' excluding element at index {indexExclude} returns: '{arrMinusIndex}'")
        print(f"From '{stringForReverse}' reverse every other word: '{arrReversedOther}'")
        print(f"From '{arrMixed}' get only numbers: '{arrNumbers}'")
        print(f"From '{arrMixed}' get only letters: '{arrLetters}'")

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
        # Applying logical operator on an array of booleans
        boolArr = [True, True, False]
        andBool = boolArr[0]
        orBool = boolArr[0]
        xorBool = boolArr[0]
        # To apply the operator in pairs, instantiate with the value of the first element, then iterate from second element
        for b in boolArr[1:]:
            andBool &= b # add AND between all booleans
        for b in boolArr[1:]:
            orBool |= b # add OR between all booleans
        for b in boolArr[1:]:
            xorBool ^= b # add XOR between all booleans

        print("\nConditionals")
        print(f"For Array of booleans {boolArr},  apply AND between each element: {andBool}")
        print(f"For Array of booleans {boolArr},  apply OR between each element: {orBool}")
        print(f"For Array of booleans {boolArr},  apply XOR between each element: {xorBool}")

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
        # For Loop range(start, end, add or subtract iterator)
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

    def testFP(self):
        """FP"""
        # Have a function return another function
        # Note the first function does not need to have the second parameter defined
        def addFP(n):
            def subAddFP(m):
                return n + m
            return subAddFP
        # Pass the parameters to the function in this way (n) for the first then (m) for the sub function
        numAddFP = addFP(5)(3)

        print("\nFP")
        print(f"Returning a function from another function: {numAddFP}")

    def testTryExceptFinally(self):
        """Exception Handling"""
        filePathCorrectDate = "resources/Exception Correct Date.txt"
        filePathIncorrectDate = "resources/Exception Incorrect Date.txt"
        dataTextFile = AlphaTwo.getTextFile(filePathCorrectDate)

        print("\nException Handling")
        print(f"Reading Text File and parsing date: {dataTextFile}")
        #Incorrect Date exception
        AlphaTwo.getTextFile(filePathIncorrectDate)
        #Missing path exception
        AlphaTwo.getTextFile("")
        #Incorrect path exception
        AlphaTwo.getTextFile("/main/file.txt")

    def testGetJSONFile(self):
        """Read JSON file"""
        filePath = "resources/Resources.json"
        jsonData = AlphaTwo.getJSON(filePath)

        name = jsonData["name"]
        age = jsonData["age"]
        email = jsonData["email"]
        isEmployed = jsonData["isEmployed"]

        address = jsonData["address"]
        street = address["street"]
        city = address["city"]
        zipCode = address["zipCode"]
        skills = jsonData["skills"] #Gets Array

        print("\nRead JSON file")
        print(f"Reading JSON root: \nname: '{name}' age: '{age}' email: '{email}' isEmployed: '{isEmployed}'")
        print(f"Reading JSON address: \nstreet: '{street}' city: '{city}' zipCode: '{zipCode}'")
        print(f"Reading JSON skills: \n{skills[0]} {skills[1]} {skills[2]} {skills[3]}")

    def testExercise(self):
        """Exercise"""
        print("\nExercise")


if __name__ == '__main__':
    print(f"Starting Tests")
    unittest.main()
    print(f"Test(s) completed")
