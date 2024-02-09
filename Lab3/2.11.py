def checking_pal(word):
    if word == word[::-1]:
        return True
    else:
        return False


user_input = input("Enter the word: ")
print(checking_pal(user_input))

