from typing import List

def contains_duplicate(words: List[str]) -> bool:
    value = False
    my_list = []
    for i in words:
        if i in my_list:
            value = True
        else:
            my_list.append(i)
    return value

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
