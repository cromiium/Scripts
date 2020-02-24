print("Pig Latin Translator v1.0 by John Skilitis")
print("Pig Latin -> English Coming Soon™")
print("\n\n\n" + "Please enter an English word/phrase (no numbers...):")
''' Initial basic implementation
pig_word = eng_word[1:] + eng_word[0] + "ay"
print(pig_word)
'''
#TODO: pig latin -> english
eng_sent = input()
eng_sent = eng_sent.split()

def is_number(s): #quick dirty check to see if entered string is a number
    try:
        float(s)
        return True
    except ValueError:
        return False

def translate_word(eng_word):
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    vowel_index = 0 
    if is_number(eng_word): #number case
        return eng_word

    if len(eng_word) == 1: #single letter case
        if eng_word in vowel_list:
            return eng_word + "way" 
        else:
            return eng_word + "ay"
    while True:
        if eng_word[vowel_index] in vowel_list: #vowel case
            if vowel_index == 0:
                pig_word = eng_word + "way"
                break
            else: #consonant case
                pig_word = eng_word[vowel_index:] + eng_word[0:vowel_index] + "ay"
            break
        else:
            vowel_index+=1
    return pig_word

def main():
    pig_list = []
    for word in eng_sent:
        pig_list.append(translate_word(word))
    pig_sent=" "
    pig_sent = (" ".join(pig_list))
    print(pig_sent)

main()