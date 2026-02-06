a = int(input("Enter temperature: "))
b = input("Enter unit (c or f): ")

if b == "c":
    f = (a * 9/5) + 32
    print(f)
elif b == "f":
    c = (a - 32) * 5/9
    print(c)
else:
    print("Invalid")