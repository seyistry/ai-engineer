
print('\n--- Task 1: Full name to UPPER ---')
name = input("Enter your fullname: ").strip()
print(name.upper())

print('\n--- Task 2: First and last character ---')
word = "python"
print("First character is", word[0], "\nLast character is", word[-1])

print('\n--- Task 3: Greet user ---')
name = input("Enter your name: ").strip()
print(f"Hello, {name}!")

print('\n--- Task 4: Index of last character ---')
text = "Welcome to python"
last_char = text[-1]
# index of last character is simply length-1; rfind shows last occurrence index if repeated
idx = len(text) - 1
last_occurrence = text.rfind(last_char)
print(f"Text: '{text}'\nLast character: '{last_char}' at index: {idx} (last occurrence index: {last_occurrence})")

print('\n--- Task 5 & 6: Replace substring and membership test ---')
word_2 = "Hello world"
new_word_2 = word_2.replace("world", "python")
print(new_word_2)
print('Does "python" appear in the new string?', "python" in new_word_2)

print('\n--- Task 7: Reverse a string ---')
a = "Hello"
print("Original:", a)
print("Reversed:", a[::-1])

print('\n--- Task 8: Strip whitespace ---')
word_2 = "  Hello world   "
print("Before strip: '" + word_2 + "'")
print("After strip: '" + word_2.strip() + "'")

print('\n--- Task 9: Count vowels (case-insensitive) ---')
sentence = input("Enter a short sentence: ").strip()
if sentence:
    s = sentence.lower()
    counts = {v: s.count(v) for v in 'aeiou'}
    total_vowel = sum(counts.values())
    print("Vowel counts:", counts)
    print("The total number of vowels in the sentence is:", total_vowel)
else:
    print("No sentence entered. Skipping vowel count.")

print('\n--- Task 10: Numeric string conversion ---')
string_1 = "1234"
conv_string = int(string_1) * 2
print(conv_string)

print('\n--- Task 11: Split words ---')
string_1 = "apple banana orange"
print(string_1.split())

print('\n--- Task 12: Join words with / ---')
user_input = input("Enter a sentence: ").strip()
input_conv = user_input.split()
print("Joined with '/':", "/".join(input_conv))

print('\n--- Task 13: Replace spaces with underscores ---')
string_1 = "Hello user welcome"
print(string_1.replace(" ", "_"))

print('\n--- Task 14: Count occurrences of a ---')
string_1 = "banana"
string_count = string_1.count("a")
print(string_count)

print('\n--- Task 15: Is alphabetic? ---')
word_1 = "https://"
print(f"Is '{word_1}' alphabetic?", word_1.isalpha())
