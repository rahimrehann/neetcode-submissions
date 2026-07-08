def get_substring(input_string: str, start: int, end: int) -> str:
    max_allowed = len(input_string)
    word = input_string[start:end]

    if end > max_allowed:
        return ""
    else:
        return word



# do not modify below this line
print(get_substring("NeetCode", 1, 7))
print(get_substring("NeetCode", 1, 8))
print(get_substring("NeetCode", 1, 9))
print(get_substring("NeetCode", 0, 2))
print(get_substring("NeetCode", 0, 7))
print(get_substring("NeetCode", 4, 8))
