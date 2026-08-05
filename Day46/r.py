with open("inventory.csv") as file:

    print(file.read())

    for row in file:
        print(row)