def main():
    txt = input("Enter your text please: ")
    txt = convert(txt)
    print(txt)

def convert(str):
   str = str.replace(":)","🙂")
   str = str.replace(":(","🙁")
   return str

main()