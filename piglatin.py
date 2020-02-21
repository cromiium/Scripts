print("Pig Latin Translator v1.0 by John Skilitis")
print("\n\n\n" + "Please enter an English word:")

eng_word = input()

pig_word = eng_word[1:] + eng_word[0] + "ay"
print(pig_word)