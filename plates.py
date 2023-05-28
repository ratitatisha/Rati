def main():
    plate = input("Enter a vanity plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or not s[:2].isalpha():
        return False

    elif not all(c.isalnum() for c in s):
        return False

    elif len(s) < 2 or len(s) > 6:
        return False

    elif s.isalnum():
        for i in range(2, len(s)):
           if s[i] == "0" and s[i-1].isalpha():
               return False

           for i in range(2, len(s)-1):
               if s[i].isdigit() and s[i+1].isalpha():
                   return False
           else:
                return True
main()

