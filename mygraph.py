import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()

#1 create a virtual enviroment to isolate use of packages: py -3 -m venv _______
#2 activate your virtual enviroment: .\myvenv\Scripts\activate (directory location)
#3 install 3rd party library: pip3 install _______

# interprator must be virtual and NOT root
# new project requires new virtual enviroment