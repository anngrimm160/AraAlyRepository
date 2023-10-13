
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

print()
print()
print()

art = str(input("Do you have a favorite artist? (Y/N): "))

art= art.upper()

if (art == "Y"):
  artist = str(input("Who is it?: "))
  print()
  print("I see,", userName + "! You like the author", authorName, "and the artist", artist)

else:
  print("That's okay, perhaps you should visit the museum for inspiration!")
