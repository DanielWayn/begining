import random


def key_bank():
    chars = list(range(ord('a'), ord('z')+1))
    chars += list(range(ord('&'), ord('+')+1))
    chars += list(range(ord('0'), ord('9')+1))
    chars += list(range(ord('A'), ord('Z')+1))
    chars += list(range(ord('!'), ord('^')+1))
    return chars


def random_password(ketString, long):
    key = []
    for i in range(long):
        key.append(chr(ketString[random.randint(0, len(ketString) - 1)]))
    return key


long = int(input("Enter the password length you want: "))
char = key_bank()
password = random_password(char, long)
password = ''.join(str(b) for b in password)
print(password)
