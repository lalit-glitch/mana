lis=["password1@","aal123","qwert345","wdnmk2#","fnjfnr234@"]
pass=input("Enter your password : ")

for i in lis:
    if i==pass:
        print("Passsword match")
        print(f"The password is {pass}")
        break
else:
    lis.append(pass)
    print(lis)
