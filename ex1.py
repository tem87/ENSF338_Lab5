import sys
import re

def calculate(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2

def evaluate_expression(expression):
    stack = []

    # Tokenize the expression using regular expressions
    tokens = re.findall(r'[-]?\d+|\S', expression)

    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(float(token))
        elif token == '(':
            stack.append(token)
        elif token == ')':
            subexpression = []
            while stack and stack[-1] != '(':
                subexpression.append(stack.pop())

            if stack and stack[-1] == '(':
                stack.pop()  # Remove the '('
                result = calculate(subexpression[1], subexpression[0], subexpression[2])
                stack.append(result)
        elif token in "+-*/":
            stack.append(token)

    # Final calculation
    while len(stack) > 1:
        operator = stack.pop()
        operand2 = stack.pop()
        operand1 = stack.pop()
        result = calculate(operand1, operand2, operator)
        stack.append(result)

    if len(stack) != 1:
        print("Invalid expression. More than one result remaining.")
        return None

    return stack[0]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python your_script.py 'expression'")
        sys.exit(1)

    expression = sys.argv[1]

    # Evaluate the expression using the stack
    result = evaluate_expression(expression)

    if result is not None:
        print(int(result))




