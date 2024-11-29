expression = "3 + 2 * (8 / 4)"
try:
    result = eval(expression)
    print(result)
except  Exception as e:
    print(f"Error :{e} in expression")
