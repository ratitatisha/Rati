def main():
   total_coins = 0
   acceptable_coins = [5, 10 ,25]
   while True:
       x = int(input("insert coins: "))
       if x in acceptable_coins:
           total_coins += x
           if total_coins < 50:
               print(f"Amount Due: {50-total_coins}")
           else: 
                print(f"Change Owed: {total_coins-50}")
                break   
       else:
            print(f"Amount Due: {50-total_coins}")

if __name__ == '__main__':
    main()
