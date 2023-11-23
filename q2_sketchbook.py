import math
from time import time



#Accepts a stack of tokens, removes the first token and returns it as an integer
def token_to_int(stack):

    try:
        integer = int(stack.pop(0))

    #If the stack is empty, or the content of the token is not an integer
    except (ValueError, KeyError):
        return None
    

    #Check if integer is outside range -300 to 300
    if integer > 300 or integer < -300:
        return None
    
    #All checks passed
    return integer


        
def evaluatePNExpressionOld(input_list):

    #Not a very Pythonic approach, but I'm taking no chances
    if not isinstance(input_list, list):
        return None
    for token in input_list:
        if not isinstance(token, str):
            return None
        
    
    #Put the operators on a stack, with the most recent first
    operator_stack = []
    for i, token in enumerate(input_list):
        if token in {"+", "-", "*", "/"}:
            operator_stack.insert(0, token)
        else:

            #We've reached the first integer
            integer_stack = input_list[i:]
            break

    
    #Get ready to start performing operations

    #Set result to the first integer on the stack
    #When operations begin, this variable will always hold the result of the most recent operation
    result = token_to_int(integer_stack)
    if result == None:
        return None
    

    #Begin operations
    for operator in operator_stack:


        #Convert the token on top of the integer stack to an integer
        operand = token_to_int(integer_stack)
        if operand == None:
            return None
        

        #Perform the operation
        if operator == "+":
            result += operand
        elif operator == "-":
            result -= operand
        elif operator == "*":
            result *= operand
        elif operator == "/":
            try:
                result = int(result / operand)

            #Oops, divided by zero!
            except ZeroDivisionError:
                return None
            
    
    #Make sure there are no leftover tokens
    if integer_stack != []:
        return None
    

    return result



#This is how ChatGPT does it
def evaluate_rpn_chatgpt(input_list):
    expression = input_list.copy()
    expression.reverse()
    stack = []
    operators = set(['+', '-', '*', '/'])

    for token in expression:
        if token not in operators:
            stack.append(float(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            stack.append(result)

    return stack[0]  # The final result should be on the top of the stack