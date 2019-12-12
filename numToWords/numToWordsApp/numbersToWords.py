units_words = ['zero', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć', 'dziesięć']
double_digits_to_20_words = ['jedenaście', 'dwanaście', 'trzynaście', 'czternaście', 'piętnaście', 'szesnaście', 'siedemnaście', 'osiemnaście', 'dziewiętnaście']
tens_words = ['dziesięć', 'dwadzieścia', 'trzydzieści', 'czterdzieści', 'pięćdziesiąt', 'sześćdziesiąt', 'siedemdziesiąt', 'osiemdziesiąt', 'dziewięćdziesiąt']
houndreds_words = ['sto', 'dwieście', 'trzysta', 'czterysta', 'pięćset', 'sześćset', 'siedemset', 'osiemset', 'dziewięćset']
larger_types_words = [['tysiąc', 'milion', 'miliard', 'bilion', 'biliard', 'trylion', 'triliard', 'kwadrylion', 'kwadryliard', 'kwintylion', 'kwintyliard'],
                    ['tysiące', 'miliony', 'miliardy', 'biliony', 'biliardy', 'tryliony', 'tryliardy', 'kwadryliony', 'kwadryliardy', 'kwintyliony', 'kwintyliardy'],
                    ['tysięcy', 'milionów', 'miliardów', 'bilionów', 'biliardów','trylionów', 'tryliardów', 'kwadrylionów', 'kwadryliardów', 'kwintylionów', 'kwintyliardów']]

def get_words_representation(number):
    if str(number).isdigit():
        number = int(number)
    else:
        return ''
    
    if check_if_zero(number):
        return units_words[0]

    # sign = check_if_negative_number(number)
    # number = abs(number)
    units, tens, hundreds, thousends = 0, 0, 0, 0
    larger_types = -1
    word_repr = ''

    while not number == 0:
        double_digits_to_20 = 0
        larger_types_words_group = None

        houndreds = count_houndreds(number)
        tens = count_tens(number)
        units = count_units(number)
        
        if check_if_double_digits_to_20(units, tens):
            double_digits_to_20 = units
            units, tens = 0, 0

        larger_types_words_group = check_which_larger_type(units, tens, houndreds, double_digits_to_20)
        
        word_reprTmp = '' 

        if houndreds != 0:
            word_reprTmp += houndreds_words[houndreds - 1] + ' '
        if tens != 0:
            word_reprTmp += tens_words[tens - 1] + ' '
        if check_if_add_unit_to_result(units, houndreds, tens, larger_types):
            word_reprTmp += units_words[units] + ' '
        if double_digits_to_20 != 0:
            word_reprTmp += double_digits_to_20_words[double_digits_to_20 - 1] + ' '
        if check_if_add_larger_types_to_result(larger_types_words_group, larger_types):
            word_reprTmp += larger_types_words[larger_types_words_group][larger_types] + ' '
            
        if word_reprTmp != '':
            word_repr = word_reprTmp + word_repr

        number = number // 1000
        larger_types += 1
    return word_repr[:-1]

def check_if_add_larger_types_to_result(larger_types_words_group, larger_types):
    if larger_types_words_group is not None and not larger_types == -1:
        return True
    return False

def check_if_add_unit_to_result(units, houndreds, tens, larger_types):
    if units != 0 and not(units == 1 and houndreds == 0 and tens == 0 and larger_types != -1):
        return True
    return False

def check_if_negative_number(num):
    if num < 0:
        return 'minus '
    return ''

def check_which_larger_type(units, tens, houndreds, double_digits_to_20):
    if units == 1:
        if tens > 0 or houndreds > 0:
            return 2
        else:
            return 0
    elif units > 1 and units < 5:
        return 1
    elif units >= 5 or (units == 0 and (tens > 0 or houndreds > 0)) or not double_digits_to_20 == 0:
        return 2
    else:
        return None
    
def check_if_zero(num):
    if num == 0:
        return True
    return False

def check_if_double_digits_to_20(units, tens):
    if tens == 1 and units > 0:
        return True
    return False

def count_houndreds(num):
    houndreds = num % 1000 // 100
    return houndreds

def count_tens(num):
    tens = num % 100 // 10
    return tens

def count_units(num):
    units = num % 10
    return units

