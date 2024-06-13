import math


def is_number (n) :
    try :
        float (n) # Type - casting the string to ‘float ‘.
                    # If string is not a valid ‘float ‘ ,
                    # it ’ll raise ‘ValueError ‘ exception
    except ValueError :
        return False
    return True


def sigmoid_funtion(x):
    return 1/(1+math.e**(-x))


def relu_function(x):
    if x <= 0:
        return 0
    else:
        return x
    

def elu_function(x):
    a = 0.01
    if x <= 0:
        return a*(math.e**x - 1)
    else:
        return x
    

def activation_function():
    x = input("Input x = ")
    if is_number(x) == False:
        print("x must be a number")
        return 
    else:
        x = float(x)
        a = input("Input activation Function ( sigmoid | relu | elu ) :")
        if a == "sigmoid":
            print(f"sigmoid: f({x}) = {sigmoid_funtion(x)}")
        elif a == "relu":
            print(f"relu: f({x}) = {relu_function(x)}")
        elif a == "elu":
            print(f"elu: f({x}) = {elu_function(x)}")
        else: 
            print(f"{a} is not supported")
        
        

if __name__=='__main__':
    activation_function()