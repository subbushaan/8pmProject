
def fact(no):
    print(no)
    if no == 1:
        return 1
    else:
        return no * fact(no-1)


res = fact(5)
print(res)