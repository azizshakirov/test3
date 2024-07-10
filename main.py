with open("Numbers.txt") as file:
    data = file.readlines()
    data = [number.strip() for number in data]

codes = set()
for num in data:
    _, code, _, _, _  = num.split()
    codes.add(code)
print(codes)
<<<<<<< HEAD
print("salom")
=======
print("Hello")
>>>>>>> front
