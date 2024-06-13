def calculate_factorial(x):
    factorial = 1
    for i in range(1,x+1):
        factorial = factorial*i
    return factorial


def approx_sin(x, n):
    sin = 0
    for i in range(n+1):
          sin += (-1)**i*(x**(2*i+1)/calculate_factorial(2*i+1))
    return sin 


def approx_cos(x, n):
    cos = 0
    for i in range(n+1):
        cos += (-1)**i*(x**(2*i)/calculate_factorial(2*i))
    return cos


def approx_sinh(x, n):
    sinh = 0
    for i in range(n+1):
        sinh += (x**(2*i+1)/calculate_factorial(2*i+1))
    return sinh


def approx_cosh(x, n):
    cosh = 0
    for i in range(n+1):
        cosh += (x**(2*i)/calculate_factorial(2*i))
    return cosh


def exercise4():
    #check codition input
    try: 
        x = float(input("Input x = "))
    except ValueError:
        print("x is not float")
        return
    try:
        n = int(input("Input n = "))
    except ValueError:
        print("n is not integer number")
        return
    if n <= 0:
            print("n is not > 0 ")
            return
    a = input("Input Function ( sin | cos | sinh | cosh ) :")
    if a == "sin":
        print(approx_sin(x,n))
    elif a == "cos":
        print(approx_cos(x,n))
    elif a ==  "sinh":
        print(approx_sinh(x,n))
    elif a == "cosh":
        print(approx_cosh(x,n))
    else:
        return


if __name__=='__main__':
    exercise4()