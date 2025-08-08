char = input("Enter a character: ")
if len(char) == 1:
    if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
        print(f"'{char}' is an alphabet.")
    else:
        print(f"'{char}' is not an alphabet.")
else:
    print("Please enter exactly one character.")