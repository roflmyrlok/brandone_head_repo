import random


def generate_password_1(length_of_password):
    fill_list = [None] * length_of_password
    result_list = list(map(lambda element: generate_random_char(), fill_list))
    return ''.join(result_list)


def generate_password_2(lenght_of_password):
    key = ''
    for i in range(lenght_of_password):
        key += generate_random_char()
    return key


def generate_password_3(length_of_password):
    key = []
    for i in range(length_of_password):
        key.append(generate_random_char())
    return ''.join(key)


def generate_random_char():
    characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b',
                  'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                  'Y', 'Z', '!', '@', '#', '$', '%', '^', '&', '*']
    key = random.choice(characters)
    return key


result1 = generate_password_1(8)
result2 = generate_password_2(8)
result3 = generate_password_3(8)
print(result1, result2, result3)
