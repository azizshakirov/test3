with open("Numbers.txt") as file:
    data = file.readlines()
    data = [number.strip() for number in data]
    print(data)