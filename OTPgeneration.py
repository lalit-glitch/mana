import random

def otpgen():
    otp=""
    for i in range(4):
        otp+=str(random.randint(1,9))
    print("Your one time password is :",otp)

otpgen()