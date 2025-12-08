import math

def sigmoid(x):
    return 1/(1+math.exp(-x))

def forward(x, w1, w2):
    h = []
    for j in range(3):
        s = sum(x[i]*w1[i][j] for i in range(2))
        h.append(sigmoid(s))
    o = sigmoid(sum(h[j]*w2[j] for j in range(3)))
    return o

x = [1, 0]

w1 = [
    [0.2, 0.4, -0.5],
    [0.3, -0.2, 0.1]
]

w2 = [0.7, -0.3, 0.5]

print(forward(x, w1, w2))
