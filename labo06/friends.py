print("druk enter voor te stoppen")

users = []
while True:
    user = input("vrienden:")
    if user == "":
        for x in users:
            print(x)
        print(len(users))
        exit()
    else:
        users.append(user)
        continue