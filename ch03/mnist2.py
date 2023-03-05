import sys, os
sys.path.append(r'C:\Users\lcman\Desktop\개발\DeepLearningFromScratch\DeepLearning_fromScratch\ch03')
from mnist import load_mnist

(x_train, t_train), (x_test, t_test) = \
    load_mnist(flatten=True, normalize=False)
    
print(x_train.shape) # (60000,784)
print(t_train.shape) # (60000,)
print(x_test.shape) # (10000,784)
print(t_test.shape) # (10000,)
