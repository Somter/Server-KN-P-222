def func1():
    print("func1 called")

x = 10
def get_x():
    return x


def set_x(val):
    x = val
    print("new value", x)


def set_g(val):
    global x
    x = val
    print("new global value", x)


def get_x(addon=0):
    return(x + addon)

def show(x:int=1, y:int=2, w:int=3) -> None :
    print(x, y, w)


def factorial(n: int) -> int:
    """Calculate factorial of n recursively."""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    func1()
    print(get_x())
    set_x(20)
    print(get_x()) 
    set_g(30)
    print(get_x(1))
    show()
    show(10)
    show(y=20)
    show(w="A", x=40)
    print("Factorial of 5 is", factorial(5))


if __name__ == "__main__":
    main()