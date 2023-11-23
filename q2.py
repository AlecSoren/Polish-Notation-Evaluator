#This is an implementation of the 'Evaluation algorithm' described in the Polish notation Wikipedia article
#Full reference:
#Wikipedia contributors, 2023. Polish notation [Online]. Wikipedia, The Free Encyclopedia. Available from:
#https://en.wikipedia.org/w/index.php?title=Polish_notation&oldid=1170860200 [Accessed  21 October 2023].
def evaluatePNExpression(input_list):

    try:

        #Not a very Pythonic approach, but I'm taking no chances
        if not isinstance(input_list, list):
            return None
        
        #Check if list is too short
        if len(input_list) < 3:
            return None

        #Operands will be stored here (top = last)
        stack = []

        #Surprisingly this is faster than a cast, plus more restrictive
        string_to_int_table = {str(i):i for i in range(-300, 301, 1)}

        #Begin iterating through the reversed list
        for token in reversed(input_list):

            #If the next token is an operator, perform the operation on the top two elements of the stack
            if token in ("+", "-", "*", "/"):
                try:
                    operand1, operand2 = stack.pop(), stack.pop()

                #An operator has fewer than two operands, meaning this is not a valid expression
                except IndexError:
                    return None

                #Perform the operation and put the result on top of the stack
                #Apparently this is faster than using a switch
                if token == "+":
                    stack.append(operand1 + operand2)
                elif token == "-":
                    stack.append(operand1 - operand2)
                elif token == "*":
                    stack.append(operand1 * operand2)
                elif token == "/":
                    try:
                        stack.append(int(operand1 / operand2))

                    #Oops, divided by zero!
                    except ZeroDivisionError:
                        return None
                    
            #Convert the token to an integer and put it on the stack
            else:
                try:
                    stack.append(string_to_int_table[token])

                #Token is neither an operator nor a valid integer
                except KeyError:
                    return None

        #Now that we've finished iterating, the stack should contain only one integer, which is the final result
        if len(stack) == 1:
            return stack[0]
        else:
            return None
        
    except:
        return None