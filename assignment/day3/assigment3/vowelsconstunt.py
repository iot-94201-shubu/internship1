# Function to count vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


# Function to count consonants
def count_consonants(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch.isalpha() and ch not in vowels:
            count += 1
    return count


# Function to calculate ratio of vowels to consonants
def vowel_consonant_ratio(vowels, consonants):
    if consonants == 0:
        return "Consonants count is zero, ratio not possible"
    return vowels / consonants


# Input from user
string = input("Enter a string: ")

vowel_count = count_vowels(string)
consonant_count = count_consonants(string)
ratio = vowel_consonant_ratio(vowel_count, consonant_count)

# Output
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
print("Ratio of vowels to consonants:", ratio)
