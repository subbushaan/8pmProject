a = "Sathya"
def display():
    global a
    a = 100
    print(a)
    print(id(a))

print(a)
print(id(a))

display()

print(a)
print(id(a))