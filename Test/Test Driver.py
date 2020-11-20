#Alex Mello

#10/4/2019

#Test

#Function 1
#T(n) = 6n + 21
#O(n) = n

#counted "for" as n
#counted "if" as n
#counted lines inside "if" statement as 1
#everything else counted as 1

from Stack import *

def evaluate(expression):
    """Evaluates postfix expressions"""
    stack = Stack()
    expression_list = expression.split()
    
    for item in expression_list:
        if item.isdigit() == True:
            stack.push(item)

        if item == "+":
            return1 = int(stack.pop())
            return2 = int(stack.pop())
            result = return2 + return1
            stack.push(result)

        if item == "-":
            return1 = int(stack.pop())
            return2 = int(stack.pop())
            result = return2 - return1
            stack.push(result)

        if item == "*":
            return1 = int(stack.pop())
            return2 = int(stack.pop())
            result = return2 * return1
            stack.push(result)

        if item == "/":
            return1 = int(stack.pop())
            return2 = int(stack.pop())
            result = return2 / return1
            stack.push(result)
            
    final_result = stack.pop()
    return final_result




#Function 2
#T(n) = 5n + 5
#O(n) = n

#counted "for" as n
#counted everything inside "for" as n
#everything else counted as 1

def reverse_string(string):
    """Returns the reverse string of the original string"""
    
    stack = Stack()
    result = ""

    for char in string:
        stack.push(char)

    for char in string:
        returned = stack.pop()
        result = result + returned

    print(string)
    print(result)

    return result


