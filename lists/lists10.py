prev_list = [-1, 10, -20, 2, -90, 60, 45, 20]

positive_numbers = [number for number in prev_list if number > 0]

print(positive_numbers)

negative_numbers_squared = [number * number for number in prev_list if number < 0]

print(negative_numbers_squared)

sentence = 'My name is Vlad'

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

print(is_consonant('a'))

consonants = [letter for letter in sentence if is_consonant(letter) == True]
print(consonants)