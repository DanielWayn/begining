import time


def wait(self):
    # wait self seconds
    time.sleep(self.sec)


def check(password1, password):
    # check if th first password is equal to the second password
    if password1 != password:
        return 0
    else:
        return 1


userName = str(input("Enter your name"))
Password = str(input("Enter your password"))
Password1 = str(input("Enter the password again"))

if check(Password1, Password) == 1:
    print("OK")
else:
    print("The second password that you enter is not equal to the first password")
