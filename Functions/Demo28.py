
def fun1():
    print("I am Function 1")
    fun2()

def fun2():
    print("I am Function 2")
    fun1()

fun1()
