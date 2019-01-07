def fun1():
    print("Function 1")
    fun2()

def fun3():
    print("Function 3")

def fun2():
    print("Function 2")
    fun3()

fun1()