import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0 , dtype=int)

# x = np.arange(-5.0,5.0,0.1)
# y = step_function(x)
# plt.plot(x,y)
# plt.ylim(-0.1,1.1) #y축 범위
# plt.show()

def sigmoid(x):
    return 1/(1+np.exp(-x))

# x = np.arange(-5.0,5.0,0.1)
# y = sigmoid(x)
# plt.plot(x,y)
# plt.ylim(-0.1,1.1) #y축 범위
# plt.show()
def relu(x):
    return np.maximum(0,x)

x = np.arange(-5.0,5.0,0.1)

# plot step function
y_step = step_function(x)
plt.plot(x, y_step, label='Step Function')

# plot sigmoid function
y_sigmoid = sigmoid(x)
plt.plot(x, y_sigmoid, label='Sigmoid Function')

# plot relu function
y_relu = relu(x)
plt.plot(x, y_relu, label='Relu Function')

plt.ylim(-0.1,1.1) #y축 범위
plt.legend() # add legend, label 추가
plt.show()
##