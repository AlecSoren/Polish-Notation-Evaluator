import time
from q2 import evaluatePNExpression

def big_list (operator, operand, max_list_size = 536870912):
    if max_list_size % 2 == 0:
        max_list_size -= 1
    return [operator] * int((max_list_size - 1) / 2) + [operand] * int((max_list_size + 1) / 2)

def test(test_cases):
    passed_tests = 0
    for input, output in test_cases:
        try:
            result = evaluatePNExpression(input)
        except Exception as e:
            result = type(e).__name__
        
        if result == output and (type(result) == int or result == None):
            passed_tests += 1
        else:
            print(f'INPUT: {input}\nEXPECTED OUTPUT: {output}\nACTUAL OUTPUT: {result}')
    print(f'Passed {passed_tests} of {len(test_cases)} tests')

test_cases = (
    #Basic functionality
    (["+", "299", "4"], 303), #Addition
    (["-", "-100", "250"], -350), #Subtraction
    (["*", "90", "8"], 720), #Multiplication
    (["/", "150", "5"], 30), # Division

    (["+", "-60", "-12"], -72), #Add negative
    (["-", "4", "-7"], 11), #Subtract negative
    (["*", "2", "-3"], -6), #Multiply negative
    (["/", "18", "-6"], -3), #Divide by negative

    (["+", "*", "-", "/", "99", "-10", "-50", "-2", "-11"], -93), #Complex vald expression
    ("This is bad input", None), #Argument is not iterable
    (("+", "3", "3"), None), #Argument is iterable but not list
    (["This", "is", "also", "bad", "input"], None), #Invalid tokens
    (["+", 3, 3], None), #Tokens are int instead of string
    (["-", "30.5", "2"], None),
    (["*", "+", "301", "5", "-6"], None),
    (["-", "-500", "11"], None),
    (["123"], None),
    (["+", "+", "+", "123", "7", "11", "50", "200", "19"], None),
    (["+-", "3", "2"], None),
    (["*", "/", "100", "-0", "2"], None),
    (["+", "/", "1", "2"], None),
    (["/", "-199", "10"], -19),
    (['+', '5', '3'], 8),
    (['*', '6', '2'], 12),
    (['-', '10', '3'], 7),
    (['/', '12', '4'], 3),
    (['*', '4', '+', '5', '3'], 32),
    (['*', '+', '5', '3', '2'], 16),
    (['-', '10', '*', '3', '2'], 4),
    (['/', '/', '6', '2', '/', '12', '4'], 1),
    ([], None),
    (None, None),
    ([None], None),
    (["+"], None),
    (['+', '3', '*', '2', '4'], 11),
    (['+', '+', '3', '4'], None),
    (['/', '5', '0'], None),
    (['+', '5', '2', '+', '3', "101"], None),
    (["/", '+', '45', '*', '3', '2', '*', '4', '/', '10', '2'], 2),
    (["/", "1", "2"], 0),
    (["/", "12", "7"], 1),
    (["+", "035", "5"], None),

    (big_list("*", "300", 1000), 300 ** 500)
)

def test_time():
    for i in range(1, 9):
        start = time.time()
        evaluatePNExpression(big_list("*", "-300", 10 ** i))
        print(f'10^{i} tokens: Evaluated in {round(time.time() - start, 3)} seconds')

test(test_cases)
#test_time()