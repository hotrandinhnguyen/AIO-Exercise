import math
import random


#TASK1

def calc_f1_score( tp , fp , fn ) :
    #check condition1
    dictionary_check = {"tp":tp,"fp":fp,"fn":fn} # use dictionary because dictionary have values and key, ez to access
    for i in dictionary_check:
        try:
            if dictionary_check[i] == int(dictionary_check[i]):
                pass
        except:
            print(f"{i} must be int")
            return
    #change type to calc
    tp =int(tp)
    fp =int(fp)
    fn =int(fn)
    #check condition1
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greater than zero")
        return
    #calc Precision
    precision = tp / (tp+fp)
    #calc Recall
    recall = tp / (tp+fn)
    #calc F1-score
    f1_score = 2*precision*recall/(precision+recall)
    #print Precision,Recall,F1-score
    print(f"Precision is {precision}")
    print(f"Recall is {recall}")
    print(f"F1-score is {f1_score}")

def exercise1():
    tp = input("tp =")
    fp = input("fp =")
    fn = input("fn =")
    calc_f1_score(tp,fp,fn)

#TASK 2

def is_number ( n ) :
    try :
        float ( n ) # Type - casting the string to ‘float ‘.
                    # If string is not a valid ‘float ‘ ,
                    # it ’ll raise ‘ValueError ‘ exception
    except ValueError :
        return False
    return True
def sigmoid_funtion(x):
    return 1/(1+math.e**(-x))

def relu_function(x):
    if x <=0:
        return 0
    else:
        return x
    
def elu_function(x):
    a = 0.01
    if x<=0:
        return a*(math.e**x - 1)
    else:
        return x
    
def exercise2():
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

#TASK 3

def calc_loss_function(num_sample, loss_name):
    num_sample = int(num_sample)
    final = 0
    for i in range(num_sample):
        pred = random.uniform(0,10)
        target = random.uniform(0,10)
        if loss_name == "MAE":
            loss = abs(pred-target)
        elif loss_name == "MSE":
            loss = (pred-target)**2
        elif loss_name =="RMSE":
            loss = (pred-target)**2
        else:
            print("loss name incorrect ")
            return
        print(f"loss name: {loss_name}",end=", ")
        print(f"sample: {i}",end=", ")
        print(f"pred : {pred}",end=", ")
        print(f"target : {target}",end=", ")
        print(f"loss : {loss}")
        final += loss
    final = final/num_sample
    if loss_name == "RMSE":
            final = final**(1/2)
    else:
        pass
    print (f"final {loss_name}: {final}")

def exercise3():
    num_sample = input("Input number of samples ( integer number ) which are generated:")
    if num_sample.isnumeric() == False:
        print("number of samples must be an integer number")
        return
    else:
        loss_name = input("Input loss name :")
        calc_loss_function (num_sample ,loss_name)



#TASK 4

def calculate_factorial(x):
    factorial = 1
    for i in range(1,x+1):
        factorial = factorial*i
    return factorial

def approx_sin(x,n):
    sin = 0
    for i in range(n+1):
          sin += (-1)**i*(x**(2*i+1)/calculate_factorial(2*i+1))
    return sin 

def approx_cos(x,n):
    cos = 0
    for i in range(n+1):
        cos += (-1)**i*(x**(2*i)/calculate_factorial(2*i))
    return cos

def approx_sinh(x,n):
    sinh = 0
    for i in range(n+1):
        sinh += (x**(2*i+1)/calculate_factorial(2*i+1))
    return sinh

def approx_cosh(x,n):
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
    
#TASK 5

def MD_nRE_calc_loss(y,y_hat,n,p):
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
    MD_nRE_calc_loss(y,y_hat,n,p)
    
def menu():
    try:
        n =int(input("input exercise you want to see :"))
    except ValueError:
        print("exercise is not int")
    if n ==1:
        exercise1()
    elif n==2:
        exercise2()
    elif n==3:
        exercise3()
    elif n==4:
        exercise4()
    elif n==5:
        exercise5()
    else:
        print("exercise is not 1 to 5") 
    
if __name__=='__main__':
    menu()

