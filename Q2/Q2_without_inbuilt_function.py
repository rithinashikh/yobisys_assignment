def operator_precedence(operator):
    if operator in ('+', '-'):
        return 1
    if operator in ('*', '/'):
        return 2
    return 0

def execute_operator(value1, value2, operator):
    if operator == '+':
        return value1 + value2
    if operator == '-':
        return value1 - value2
    if operator == '*':
        return value1 * value2
    if operator == '/':
        if value2 == 0:
            raise ValueError("Division by zero")
        return value1 / value2

def convert_to_postfix(expression):
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    postfix_list = []
    operator_stack = []

    for token in tokens:
        if token.isdigit() or '.' in token:  
            postfix_list.append(float(token))
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                postfix_list.append(operator_stack.pop())
            operator_stack.pop()  
        else:  
            while (operator_stack and operator_stack[-1] != '(' and
                   operator_precedence(operator_stack[-1]) >= operator_precedence(token)):
                postfix_list.append(operator_stack.pop())
            operator_stack.append(token)

    while operator_stack:
        postfix_list.append(operator_stack.pop())

    return postfix_list

def evaluate_postfix(postfix_tokens):
    evaluation_stack = []
    for token in postfix_tokens:
        if isinstance(token, float):  
            evaluation_stack.append(token)
        else:  
            value2 = evaluation_stack.pop()
            value1 = evaluation_stack.pop()
            evaluation_stack.append(execute_operator(value1, value2, token))
    return evaluation_stack[0]

def calculate_expression(expression):
    try:
        postfix_expression = convert_to_postfix(expression)
        return evaluate_postfix(postfix_expression)
    except Exception as error:
        raise ValueError(f"Invalid expression: {expression}. Error: {error}")


example_expression = "3 + 2 * (8 / 4)"
calculated_result = calculate_expression(example_expression)
print(f"The result of '{example_expression}' is {calculated_result}")
