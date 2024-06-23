import torch
import torch.nn as nn


class MySigmoid(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return 1 / (1 + torch.exp(-x))


class MyReluActivation(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        zeros = torch.zeros_like(x)
        return torch.maximum(x, zeros)


class MySoftmaxActivation(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        return x_exp/torch.sum(x_exp)


if __name__ == "__main__":
    sigmoid_function = nn.Sigmoid()
    data = torch.Tensor([1, 2, 3])
    output = sigmoid_function(data)
    print(output)

    data = torch.Tensor([1, -2, 3])
    my_relu = MyReluActivation()
    output = my_relu(data)
    print(output)

    softmax = nn.Softmax()
    data = torch.Tensor([1, 2, 3])
    output = softmax(data)
    print(output)