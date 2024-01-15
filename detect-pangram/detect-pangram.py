import re

def is_pangram(s):
    alphabets = sorted(set("abcdefghijklmnopqrstuvwxyz"))
    s_letters = sorted(set(re.sub(r'[^a-z]', '',s.lower())))
    print(alphabets)
    print(s_letters)
    if alphabets == s_letters:
        return True
    return False