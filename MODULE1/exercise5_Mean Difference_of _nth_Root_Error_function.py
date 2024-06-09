def MD_nRE(y, y_hat, n, p):
    loss = (y**(1/n) - y_hat**(1/n))**p
    print(loss)


def exercise5():
    try:
        y = float(input("y ="))
    except ValueError:
        print("y is not float")
        return
    try:
        y_hat = float(input("y_hat ="))
    except ValueError:
        print("y_hat is not float")
        return
    try:
        n = int(input("n ="))
    except ValueError:
        print("n is not integer")
        return
    try:
        p = int(input("p ="))
    except ValueError:
        print("p is not integer")
        return
    MD_nRE(y, y_hat, n, p)

if __name__=='__main__':
    exercise5()