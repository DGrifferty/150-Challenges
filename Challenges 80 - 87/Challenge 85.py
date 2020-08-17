# 085
# Ask the user to type in their name and then tell them
# how many vowels are in their name.

print(f'You have {len(list(i for i in list(input("Enter ya name: ")) if i.lower() in "aeiou"))} vowel(s) in your name')
