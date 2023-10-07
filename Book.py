
userName = str(input("What is your name?: "))
userAge = int(input("How old are you?: "))

print("Your name is", userName, "and you are", userAge, "years old.")

print()
print()
print()

bookName = str(input("What's your favorite book?: "))
authorName = str(input("Who wrote this book?: "))

combined_list = [userName, userAge, bookName, authorName]
print("Thank you for answering " + combined_list[0] + ", it is interesting to know that " + str(combined_list[1]) + " year olds are reading " + combined_list[2] + " by " + combined_list[3] + ".")
