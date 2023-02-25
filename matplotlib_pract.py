import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import imread




def heart_function(t):
    x = 16*np.sin(t)**3
    y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
    return x, y

t = np.linspace(0, 2*np.pi, 1000)
x, y = heart_function(t)

plt.plot(x, y, color='red', linewidth=2, label='LOVE')
plt.axis('equal')
plt.legend() # add legend, label 추가
plt.show()

# Using forward slashes
img = imread('C:/Users/labinno/Desktop/sino galbo/20230110/TestDemo-English/image/monalisa.JPG')

# Escaping backslashes
# img = imread('C:\\Users\\labinno\\Desktop\\sino galbo\\20230110\\TestDemo-English\\image\\monalisa.JPG')

plt.imshow(img)
plt.show()