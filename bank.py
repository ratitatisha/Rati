greeting = str(input("What was your greeting? "))
greeting = greeting.strip()
greeting = greeting.lower()

if greeting.startswith("hello"):
   print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")

