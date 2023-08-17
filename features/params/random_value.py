import string, random


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


RAND_NAME = randomword(10)
RAND_EMAIL = f'test_{randomword(5)}@test.com'
