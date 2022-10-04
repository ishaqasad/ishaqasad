import matplotlib.pyplot as plt
import numpy as np

data_test = np.empty((30,2))
for i in range(30):
  if i < 15:
    data_test[i] = np.random.random(2) * 0.5
  else:
    data_test[i] = np.random.random(2) * 2
#plt.axes(projection='3d')
plt.plot(data_test[:,0],data_test[:,1], "o")

const = 2
c_a = k_means(2, data_test)

plt.plot(c_a[0][:,0],c_a[0][:,1], "ro")
one = []
twos = np.empty((30,2))
zero = []
for i in range(30):
  if(c_a[1][i] == 1):
    one.append(data_test[i].tolist())
  else:
    zero.append(data_test[i].tolist())

for i in range(30):
  print(data_test[i] , " assigned " , c_a[1][i])
ones = np.array(one)
zeros = np.array(zero)

plt.plot(ones[:,0],ones[:,1] , "go")
plt.plot(zeros[:,0],zeros[:,1] , "mo")
