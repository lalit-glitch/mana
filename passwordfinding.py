lis=["password1@","aal123","qwert345","wdnmk2#","fnjfnr234@"]
a=input("Enter your password : ")

for i in lis:
    if i==a:
        print("Passsword match")
        print(f"The password is {a}")
        break
else:
    print("Password not match")