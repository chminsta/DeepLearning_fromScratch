import numpy as np

def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

a=np.array([0.3,2.9,4.0])

print(softmax(a))
#[0.01821127 0.24519181 0.73659691]


# [문제점] e^1000같이 큰수는 inf가 되어 돌아온다. 한계가 있다. 개선 필요!
# 해결: 식을 써서 계산해보면 각각 같은값을 더하거나 뺴도 softmax같음. 고로 최대값을 빼자

def softmax2(a):
    c=np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

b=np.array([1000,1010,990])
print(softmax(b))
print(softmax2(b))

# [nan nan nan]
# [4.53978686e-05 9.99954600e-01 2.06106005e-09]
# 해결!


#softmax 특징
#1. 모두 0과 1.0사이임
#2. 모든 합이 1임
#>>>확률로 해석 가능