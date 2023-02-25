import numpy as np  #numpy를 np라는 이름으로 가져와라


print("1차원")
x = np.array([1.0, 2.0, 3.0])
print(x)
print(type(x))

y=np.array([2.0,4.0,6.0])
print("\n1차원 + - * /")
print(x+y)
print(x-y)
print(x*y)
print(x/y)



#2차원 배열도 가능하다
print("\n2차원")
a= np.array([[1,2],[3,4]])

print(a)

print(a.shape)

print(a.dtype)

b=np.array([[3,4],[1,1]])
print("\na+b,a*b")
print(a+b)

print(a*b)


print("\nrow 출력")
for row in a:
    print(row)

c=np.array([[3,4],[1,1],[3,1]])
print("\nflatten, flatten 후 0,2,4번째")
print(c.flatten())
cc=c.flatten()
cc=cc[np.array([0,2,4])]
print(cc)
print("\n1보다큰지, 1보다큰거만 남기기")
print(c>1)
print(c[c>1])


