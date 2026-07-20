def add_two_numbers() -> int:
    user_input = input()
    new_list = user_input.split(",")
    added = 0

    for item in new_list:
        added += int(item)

    return added




# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
