def main():
    user_prompt = input("whats file name? ").strip().lower()
    print(file_name(user_prompt))

def file_name(file):
    if len(file.split('.'))<2 :
        return "application/octet-stream"
    if file.endswith(".jpg") or file.endswith(".jpeg"):
        return "image/jpeg"
    elif file.endswith(".png"):
        return "image/png"
    elif file.endswith(".gif"):
        return "image/gif"
    elif file.endswith(".pdf"):
        return "application/pdf"
    elif file.endswith(".txt"):
        return "text/plain"
    elif file.endswith(".zip"):
        return "application/zip"
    elif file.endswith(".bin"):
        return "application/octet-stream"
    else:
        return "application/octet-stream"
main()
