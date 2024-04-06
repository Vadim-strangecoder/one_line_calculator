"""
PLEASE READ INSTRUCTION!

this is linear calculator: enter your problem like this:  ( 2 + 2 ) * 2 ;
this calculator support this functions:
         '+' - addition
         '-' - substraction
         '*' - multiplication
         '/' - division
         '**' - exponentiation

EXAMPLES:
         input: 2.5 ** 2 + 0.25 * 3
         output: 7.0

         input: ( ( 2 + 2 ) * 1 ) / 2
         output: 2.0
"""
MATH_TEXT = str(input())

cases = {(False, False): lambda a,b: False,
         (True, True): min,
         (True, False): lambda a,b: a,
         (False, True): lambda a,b: b}

calc = {'*': lambda a,b: a * b,
        '/': lambda a,b: a / b,
        '+': lambda a,b: a + b,
        '-': lambda a,b: a - b,
        '**': lambda a,b: a ** b}


statment_list = MATH_TEXT.split()
# ['3', '+', '5', '*', '4']

def first_func(cases_in_func, s_list):
    """function returns index of math sign"""
    multiply = None
    divide = None
    if '*' in s_list:
        multiply = s_list.index('*')
    if '/' in s_list:
        divide = s_list.index('/')
    if '**' in s_list:
        _raise = s_list.index('**')
        return _raise
    return cases_in_func[isinstance(multiply, int), isinstance(divide, int)](multiply, divide)


def second_func(cases_in_func, s_list):
    """function returns index of math sign"""
    plus = None
    minuse = None
    
    if '+' in s_list:
        plus = s_list.index('+')
    if '-' in s_list:
        minuse = s_list.index('-')

    return cases_in_func[isinstance(plus, int),isinstance(minuse, int)](plus, minuse)

def calculate_list(s_list, cases_in_func, calc_in_func):
    """function returns list with math answer"""
    while len(s_list) != 1:
        result_list = first_func(cases_in_func, s_list)
        if not result_list:
            result_list = second_func(cases_in_func, s_list)

        a = float(s_list[result_list - 1])
        b = float(s_list[result_list + 1])
        num = calc_in_func[s_list[result_list]](a,b)
        s_list[result_list] = num
        s_list.pop(result_list - 1)
        s_list.pop(result_list)
        

    return s_list


while len(statment_list) != 1:
    if '(' in statment_list:
        close_index = statment_list.index(')')
        cut_statment_list = statment_list[0 : close_index]
        open_index = len(cut_statment_list) - cut_statment_list[::-1].index('(')
        brackets_statment = statment_list[open_index : close_index]
        result = calculate_list(brackets_statment, cases, calc)
        statment_list[open_index - 1: close_index + 1] = result
    else:
        statment_list = calculate_list(statment_list, cases, calc)

print(statment_list[0])
