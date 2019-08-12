import random
import string


def random_letter(num_len):
    """Generate a random string of fixed length """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(num_len))


def random_uppercase_letter(num_len):
    """Generate a random string of fixed length """
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(num_len))


def random_integer(start_num, finish_number):
    return random.randrange(start_num, finish_number)


def get_generated_number(init_letter, rand_letter_len, start_num, finish_number):
    return "{}-{}-{}".format(init_letter.upper(), random_uppercase_letter(rand_letter_len),
                             random_integer(start_num, finish_number))


__name__ = '__main__'
print(get_generated_number("cust", 3, 10000, 99999))
