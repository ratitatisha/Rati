# 1.
print("What is the quote? These aren't the droids you're looking for.Who said it? Obi-Wan KenobiObi-Wan Kenobi says, These aren't the droids you're looking for.")

# 2.
def main():
    name = input("enter your name: ")
    fraza(name)
def fraza(filtered):
    fraza = {
       "Jordan" : "Magic pass the ball",
       "Lebron" : "The king is back",
       "Magic": "I'm the best point guard ever",
    }

    if filtered in fraza:
        print(fraza[filtered])
    else:
        print("Sheyvanili saxeli arasworia")
main()