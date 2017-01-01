"""
String utils
"""


def consecutive_repetitions(string):
    """
        Given a non-empty string, it returns a substring containing the consecutive
        repetitions of the first character of the original string.

        @args:
        - string (str): the string to be evaluated.
    """
    if len(string) == 1:
        return string
    char_to_match = string[0]
    current_index = 1
    repetitions = char_to_match
    while current_index < len(string) and char_to_match == string[current_index]:
        repetitions += string[current_index]
        current_index += 1
    return repetitions

