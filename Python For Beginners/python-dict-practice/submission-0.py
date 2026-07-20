from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    my_dict = {}
    for letter in word:
        target = letter
        count = 0
        for letters in word:
            if letters == target:
                count +=1
        my_dict[letter] = count
    return my_dict




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
