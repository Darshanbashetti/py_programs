def tricky_string(s1, s2):
    """
    Concatenates two strings in a tricky way:
    - If the length of s1 is greater than the length of s2, 
      add s2 in the middle of s1.
    - If the length of s2 is greater than the length of s1, 
      add s1 in the middle of s2.
    - If both strings have equal lengths, concatenate them normally.
    """
    if len(s1) > len(s2):
        middle_index = len(s1) // 2
        return s1[:middle_index] + s2 + s1[middle_index:]
    elif len(s2) > len(s1):
        middle_index = len(s2) // 2
        return s2[:middle_index] + s1 + s2[middle_index:]
    else:
        return s1 + s2

# Example usage:
s1 = "python"
s2 = "program"
result = tricky_string(s1, s2)
print("Tricky string:", result)
