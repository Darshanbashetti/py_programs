def tricky_reverse_string(s):
    """
    Reverse a string in a tricky way:
    - Reverse the entire string.
    - Reverse each word in the string.
    """
    reversed_string = s[::-1]  # Reverse the entire string
    words = reversed_string.split()  # Split the string into words
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    return ' '.join(reversed_words)  # Join the reversed words into a string

# Example usage:
s = "Hello World! This is a tricky string reversal program."
result = tricky_reverse_string(s)
print("Tricky reversed string:", result)
