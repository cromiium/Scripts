print("Pig Latin Translator v1.0 by John Skilitis")
print("\n\n\n" + "Please enter an English word:")

''' Initial basic implementation
pig_word = eng_word[1:] + eng_word[0] + "ay"
print(pig_word)
'''
vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']
eng_word = input()

for letter in eng_word:
    if letter in vowel_list:
        pig_word = eng_word + "way"
    else:
        pig_word = eng_word[1:] + eng_word[0] + "ay"

print(pig_word)