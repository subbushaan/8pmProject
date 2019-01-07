def fun1():
    print("Function 1")
    fun2()
    print("Hi")

def fun2():
    fun3()
    print("Function 2")

def fun4():
    print("Fucntion 4")
    fun2()

def fun3():
    print("Function 3")

fun1()
fun3()
fun4()







