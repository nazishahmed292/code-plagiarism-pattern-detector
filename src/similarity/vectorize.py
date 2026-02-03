from collections import Counter

def build_frequency_vector(tokens):
    """
    Converts list of tokens into a frequency dictionary
    """
    return Counter(tokens)
