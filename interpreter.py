def main():
    user_prompt = input("arithmetic expression: ")
    print(interpreter(user_prompt))

def interpreter(expression):
    x,y,z = expression.split()
    x = float(x)
    z = float(z)
    if y == "+":
        return x+z
    elif y == "-":
        return x-z
    elif y == "/":
        return x/z
    elif y == "*":
        return x*z
main()
