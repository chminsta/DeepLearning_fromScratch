import numpy as np

# def AND(x1,x2):
#     w1,w2,theta = 0.5, 0.5, 0.7
#     tmp = x1*w1 + x2*w2
#     if tmp <= theta:
#         return 0
#     else:
#         return 1

def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5, 0.5])
    b = -0.7

    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else:
        return 1



def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else:
        return 1   

print("ㅋ\n\nAND\n0,0: ",AND(0,0),"\n0,1: ",AND(0,1),"\n1,0: ",AND(1,0),"\n1,1: ",AND(1,1))
print("\nㅋ\n\nOR\n0,0: ",OR(0,0),"\n0,1: ",OR(0,1),"\n1,0: ",OR(1,0),"\n1,1: ",OR(1,1))
print("\nㅋ\n\nNAND\n0,0: ",NAND(0,0),"\n0,1: ",NAND(0,1),"\n1,0: ",NAND(1,0),"\n1,1: ",NAND(1,1))


#퍼셉트론 하나만으로는 선형 직선으로만 컷할수 있음
#다중퍼셉트론 이용!
#x1 XOR x2 = (x1 NAND x2) AND (x1 OR x2)

def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y

print("\nㅋ\n\nXOR\n0,0: ",XOR(0,0),"\n0,1: ",XOR(0,1),"\n1,0: ",XOR(1,0),"\n1,1: ",XOR(1,1))