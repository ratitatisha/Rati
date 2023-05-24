# 1.
name = input("Whats your name? ").strip().title()
print("Hello," + name + ",Nice to meet you!")
# 2.
name = input("Whats your name? ").strip().title()
output = ("Hello," + name + ",Nice to meet you!")
print(output)
# 3.
print(f"Hello," + input("Whats your name?").strip().title() + ",Nice to meet you!" )
# 4.
name = input("whats your name? ")
if name == 'Jordan':
    print("Hello," + name)
elif name == "James":
    print("Hi," + name)
else:
    print("Whats Up?" + name)