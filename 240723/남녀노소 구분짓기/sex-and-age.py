female = int(input())
age = int(input())

if female:
    if age <19:
        print("GIRL")
    else:
        print("WOMAN")
else:
    if age < 19:
        print("BOY")
    else:
        print("MAN")