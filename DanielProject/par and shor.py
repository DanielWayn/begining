import random


def random_number():
    number = random.randint(1000, 9999)
    return number


print("Welcome to the Cows and Bulls Game!")
guess_times = 0
random_num = str(random_number())
par = 0
shor = 0
print("thr nuber is: ", random_num)
while par != 4:
    if shor > 4:
        shor = 4
    print("par: ", par)
    print("shor: ", shor)
    par = 0
    shor = 0
    print("guess number: ", guess_times)
    guess_times += 1
    guess = str(input("enter number with 4 nums: "))
    guess_place = 0
    for i in guess[::]:
        random_num_place = 0
        for n in random_num[::]:
            if i == n:
                if guess_place == random_num_place:
                    par += 1
                else:
                    shor += 1
            random_num_place += 1
        guess_place += 1

print("!!corect!!")