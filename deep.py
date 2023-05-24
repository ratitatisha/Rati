def main():
    user_prompt = input("What is the answer to the great question of life,The Universe,and everything? ").strip().lower()
    print(answer(user_prompt))

def answer(text):
    match text:
        case "42":
           return "Yes"
        case "forty two":
            return "Yes"
        case "forty-two":
            return "Yes"
        case _:
            return "No"
main()