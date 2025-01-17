"""
Helper functions for advanced string operations.
"""

def reverse_string(string):
    return string[::-1]

def capitalize_words(string):
    return " ".join(word.capitalize() for word in string.split())
