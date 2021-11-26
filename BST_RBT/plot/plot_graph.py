import pandas as pd
import matplotlib.pyplot as plt
#iterations,build_time,delete_time,heightTree

data = pd.read_csv('Scripts/data.csv')
x = data['n']
y = data['time']
z = data['avgH']
a = data['dtime']

plt.xlabel('N')
plt.ylabel('Time taken(seconds)')
plt.title('Time it took to build BST with TREE-INSERT with n keys')
plt.plot(x, y)
plt.show()

plt.xlabel('N')
plt.ylabel('Time taken(seconds)')
plt.title('Time it took to delete BST with TREE-DELETE with n keys')
plt.plot(a, y)
plt.show()

plt.xlabel('N')
plt.ylabel('Height of tree')
plt.title('Asymptotic growth regarding height: TREE-INSERT')
plt.plot(x, z)
plt.show()

data2 = pd.read_csv('Scripts/rbt.csv')
x_rb = data2['n']
y_rb = data2['time']
plt.xlabel('N')
plt.ylabel('Time taken(seconds)')
plt.title('Time taken for n keys for RB-INSERT')
plt.plot(x_rb, y_rb)
plt.show()
