userInput = input("Enter a word to see if it is a palindrome: ")
if len(userInput)%2==0:
    half = userInput[0:int((len(userInput)/2))]
    if half+half[::-1] != userInput:
        print(f"{userInput} is not a palindrome!")
    else:
        print(f"{userInput} is a palindrome!")
else:
    half = userInput[0:int((len(userInput)/2))]
    if half+userInput[int((len(userInput)/2))]+half[::-1] != userInput:
        print(f"{userInput} is not a palindrome!")
    else:
        print(f"{userInput} is a palindrome!")
