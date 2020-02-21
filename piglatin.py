print("Pig Latin Translator v1.0 by John Skilitis")
print("\n\n\n" + "Please enter an English word:")
''' Initial basic implementation
pig_word = eng_word[1:] + eng_word[0] + "ay"
print(pig_word)
'''
vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']
vowel_index = 0 

eng_word = input()

while True:
    if eng_word[vowel_index] in vowel_list:
        if vowel_index == 0:
            pig_word = eng_word + "way"
            break
        else:
            pig_word = eng_word[vowel_index:] + eng_word[0:vowel_index] + "ay"
        break
    else:
        vowel_index+=1
print(pig_word)