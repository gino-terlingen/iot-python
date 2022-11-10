print("druk enter voor te stoppen")

users = []
while True:
    user = input("vrienden:")
    if user == "":
        print(users)
        exit()
    else:
        users.append(user)
        continue
