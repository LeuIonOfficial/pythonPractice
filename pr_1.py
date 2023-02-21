def palindrome_check():
    word = input('word: ')
    if word[0] == word[-1]:
        print("Palindrome")
    else:
        print("Not palindrome")


palindrome_check()
