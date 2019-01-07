
def validateAge():
    age = int(input("Enter Age : "))
    if age >= 16:
        return "Valid Age"
    else:
        return "Invalid Age"

print(validateAge())