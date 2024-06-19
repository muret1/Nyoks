# program that prompts a user to enter a letter then checks whether it is a consonant or a vowel


letter = input("enter letter:")
if letter in "a,e,i,o,u":
    print(letter, "is a vowel")

else:
    print("letter is a consonant")