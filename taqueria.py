def main():
    order_total = 0
    items = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    while True:
         try:
             item = input("Item: ").title()
             if item in items:
                 order_total += items[item]
                 print(f"Total: ${order_total:.2f}")
             else:
                  pass
         except(KeyboardInterrupt,EOFError):
          break
main()