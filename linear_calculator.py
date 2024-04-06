statment = str(input())

cases = {(False, False): lambda a,b: False,
         (True, True): lambda a,b: min(a, b),
         (True, False): lambda a,b: a,
         (False, True): lambda a,b: b}

calc = {'*': lambda a,b: a * b,
        '/': lambda a,b: a / b,
        '+': lambda a,b: a + b,
        '-': lambda a,b: a - b,
        '**': lambda a,b: a ** b}


statment_list = statment.split()
# ['3', '+', '5', '*', '4']

def first_func(cases, s_list):
    multiply = None
    divide = None
    if '*' in s_list:
         multiply = s_list.index('*')
    if '/' in s_list:
         divide = s_list.index('/')
    if '**' in s_list:
         _raise = s_list.index('**')
         return _raise
    
    return cases[isinstance(multiply, int), isinstance(divide, int)](multiply, divide)
    
    
    
def second_func(cases, s_list):
    plus = None
    minuse = None
    if '+' in s_list:
         plus = s_list.index('+')
    if '-' in s_list:
         minuse = s_list.index('-')
    
    return cases[isinstance(plus, int),isinstance(minuse, int)](plus, minuse)
    
    
    
#while len(statment_list) != 0:
def calculate_list(statment_list, cases, calc):
    while len(statment_list) != 1:
        result = first_func(cases, statment_list)
        if not(result):
            result = second_func(cases, statment_list)
        

        a = float(statment_list[result - 1])
        b = float(statment_list[result + 1])
        num = (calc[statment_list[result]](a,b))
        statment_list[result] = num 
        statment_list.pop(result - 1)
        statment_list.pop(result)
        
        #print(statment_list)
    return statment_list

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



