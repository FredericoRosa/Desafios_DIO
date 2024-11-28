def is_palindrome(word):
    # Remove any spaces and convert to lowercase for uniformity
    cleaned_word = word.replace(" ", "").lower()
    # Check if the cleaned word is equal to its reverse
    return cleaned_word == cleaned_word[::-1]

# Test the function
test_word = "Ovo"
print(f"A Palavra '{test_word}' é palindromo? {is_palindrome(test_word)}")
