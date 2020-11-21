import log
import random

# 447,856 words

def gen_credentials():
    log.info("Loading dictionary...")
    dictionary_file = open('dictionary.txt', 'r')
    dictionary = dictionary_file.read().split('\n')
    log.good("Loaded!")

    username = f'{dictionary[random.randint(0, 447856)]}{random.randint(100, 999)}'
    password = f'{dictionary[random.randint(0, 447856)]}{random.randint(100000, 999999)}'
    date_of_birth = (random.randint(1, 12), random.randint(1, 28), random.randint(1940, 2002))
    email = f'{username}@gmail.com'
    log.good(f"Generated username ({username}), password ({password}), email ({email}), and date of birth ({str(date_of_birth)})")
    return (username, password, date_of_birth, email)