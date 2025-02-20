
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
    message = "Alpha One Initialized"
    lowerCase = "lower case text"
    replacedMessage = message.replace("One", "Prime")
    #Convert to Upper Case
    upperCase = lowerCase.upper()
    startsWith = message.startswith("Alpha")
    endsWith = message.endswith("Initalized")
    integerArray = [1, 1]
    stringArray = ["First", "Second"]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    _alphaOne = AlphaOne()
    print(_alphaOne.replacedMessage + " starts with Alpha: " + str(_alphaOne.startsWith) + " and ends with Initialized: " + str(_alphaOne.endsWith))