unitsWords = ['zero', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć', 'dziesięć']
doubleDigitsTo20Words = ['jedenaście', 'dwanaście', 'trzynaście', 'czternaście', 'piętnaście', 'szesnaście', 'siedemnaście', 'osiemnaście', 'dziewiętnaście']
tensWords = ['dziesięć', 'dwadzieścia', 'trzydzieści', 'czterdzieści', 'pięćdziesiąt', 'sześćdziesiąt', 'siedemdziesiąt', 'osiemdziesiąt', 'dziewięćdziesiąt']
houndredsWords = ['sto', 'dwieście', 'trzysta', 'czterysta', 'pięćset', 'sześćset', 'siedemset', 'osiemset', 'dziewięćset']
largerTypesWords = [['tysiąc', 'milion', 'miliard', 'bilion', 'biliard', 'trylion', 'triliard', 'kwadrylion', 'kwadryliard', 'kwintylion', 'kwintyliard'],
                    ['tysiące', 'miliony', 'miliardy', 'biliony', 'biliardy', 'tryliony', 'tryliardy', 'kwadryliony', 'kwadryliardy', 'kwintyliony', 'kwintyliardy'],
                    ['tysięcy', 'milionów', 'miliardów', 'bilionów', 'biliardów ','trylionów', 'tryliardów', 'kwadrylionów', 'kwadryliardów', 'kwintylionów', 'kwintyliardów']]

def getWordsRepresentation(number):
    
    if checkIfZero(number):
        return unitsWords(0)

    # sign = checkIfNegativeNumber(number)
    number = abs(int(number))
    units, tens, hundreds, thousends, largerTypes = 0, 0, 0, 0, -1
    wordRepr = ''

    while not number == 0:
        doubleDigitsTo20 = 0
        largerTypesWordsGroup = None

        houndreds = countHoundreds(number)
        tens = countTens(number)
        units = countUnits(number)
        
        if checkIfDoubleDigitsTo20(units, tens):
            doubleDigitsTo20 = units
            units, tens = 0, 0

        largerTypesWordsGroup = checkWchichLargerType(units, tens, houndreds, doubleDigitsTo20)
        
        wordReprTmp = '' 

        if not houndreds == 0:
            wordReprTmp += houndredsWords[houndreds - 1] + ' '

        if not tens == 0:
            wordReprTmp += tensWords[tens - 1] + ' '
        if not units == 0:
            wordReprTmp += unitsWords[units] + ' '
        if not doubleDigitsTo20 == 0:
            wordReprTmp += doubleDigitsTo20Words[doubleDigitsTo20 - 1] + ' '
        if largerTypesWordsGroup is not None and not largerTypes == -1:
            wordReprTmp += largerTypesWords[largerTypesWordsGroup][largerTypes] + ' '
        wordRepr = wordReprTmp + ' ' + wordRepr
         
        number = number // 1000
        largerTypes += 1
    return wordRepr

def checkIfNegativeNumber(num):
    if num < 0:
        return 'minus '
    else:
        return ''

def checkWchichLargerType(units, tens, houndreds, doubleDigitsTo20):
    if units == 1:
        if tens > 0 or houndreds > 0:
            return 2
        else:
            return 0
    elif units > 1 and units < 5:
        return 1
    elif units >= 5 or (units == 0 and (tens > 0 or houndreds > 0)) or not doubleDigitsTo20 == 0:
        return 2
    else:
        return None
    
def checkIfZero(num):
    if num == 0:
        return True
    return False

def checkIfDoubleDigitsTo20(units, tens):
    if tens == 1 and units > 0:
        return True
    return False

def countHoundreds(num):
    houndreds = num % 1000 // 100
    return houndreds

def countTens(num):
    tens = num % 100 // 10
    return tens

def countUnits(num):
    units = num % 10
    return units


