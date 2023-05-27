def main():
    txt = input("Enter your string: ")
    print(omitted_str(txt))

def omitted_str(str):
    vowels = ["A","E","I","O","U","a","e","i","o","u"]
    for letter in str:
        if letter in vowels:
           str = str.replace(letter,"")
    return str

if __name__ == "__main__":
    main()