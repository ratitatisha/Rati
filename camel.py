def camel_to_snake(variable_name):
    snake_case = ""
    for char in variable_name:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case

variable_name = input("Enter a variable name in camel case: ")
snake_case_name = camel_to_snake(variable_name)
print("Snake case:", snake_case_name)
