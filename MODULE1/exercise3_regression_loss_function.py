import random


def regression_loss_function(num_sample, loss_name):
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
        print(f"loss name: {loss_name}", end=", ")
        print(f"sample: {i}", end=", ")
        print(f"pred : {pred}", end=", ")
        print(f"target : {target}", end=", ")
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
        loss_name = input("Input loss name MAE| MSE| RMSE:")
        regression_loss_function (num_sample ,loss_name)

if __name__=='__main__':
    exercise3()