from matplotlib import pyplot as plt
import numpy as np
x = np.linspace(1,10000,1000)
# Q = [0.5,1,10]
# for q in Q:
#     y_1 = np.sqrt(1/(1+q**2*(x/2500-2500/x)**2))

#     plt.plot(x,y_1)
U_r = 100*3/np.sqrt(100**2+(x*0.04-1/(x*1E-7))**2)
U_l = x*0.04*3/np.sqrt(100**2+(x*0.04-1/(x*1E-7))**2)
U_c = 1/(x*1E-7)*3/np.sqrt(100**2+(x*0.04-1/(x*1E-7))**2)

plt.plot(x,U_r)
plt.plot(x,U_l)
plt.plot(x,U_c)
plt.show()