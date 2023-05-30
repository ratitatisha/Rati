def main():
    percent = fraction_into_prc()
    output(percent)
def fraction_into_prc():
    while True:
         try:
             fuel_size = input("Fraction: ")
             mricxveli , mnishvneli = fuel_size.split("/")
             if int(mricxveli) > int(mnishvneli):
                  raise ValueError
             prc = int(mricxveli)/int(mnishvneli) * 100
         except ValueError:
               pass
         except ZeroDivisionError:
               pass
         else:
              return prc
def output(percent):
     if percent >= 99:
          print("F")
     elif percent <= 1:
          print("E")
     else:
          print(f"{round(percent)}%")

main()