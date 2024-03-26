def replace_exclamation(st):
    """
    Replaces all vowels in the given string with exclamation marks.
    
    Args:
        st (str): The input string.
    
    Returns:
        str: The modified string with vowels replaced by exclamation marks.
    """
    vowels = "aeiouAEIOU"
    new_st = ""
    for _, char in enumerate(st):
        if char in vowels:
            new_st += "!"
        else:
            new_st += char
    return new_st
