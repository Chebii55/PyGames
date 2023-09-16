def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
           data=line.rstrip()
           user, passw=data.split("|")
           print("User:",user,"|Password:",passw)
def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")
master_pwd = input("What is your password?")
if master_pwd=="pass":
    while True:
        mode = input("would you like to add a new password or view the existing ones(view,add)?press q to quit").lower()
        if mode == "q":
            break

        if mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid mode.")
            continue

else:
    print("Wrong Password")






