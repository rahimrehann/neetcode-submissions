from typing import List

def read_integers() -> List[int]:
    user_input = input()
    my_list = user_input.split(",")
    new_list = []

    for item in my_list:
        new_list.append(int(item))

    return new_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
