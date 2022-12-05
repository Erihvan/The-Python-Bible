# get sentence from user

original = input("Please enter a sentence:").strip().lower()
# plit sentece into words

words = original.split()
# loop through words and convert to pig latin

new_words =[]

for word in words:
    if word [0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)

# if starts with vowel, just add "yay",
#otherwise, move the first cononant cluster to end, and add "ay"

output = " ".join(new_words)
#stick words back together

#output the final string

print(output)
