#Kishan Singh(42)
#Hanning window response
import numpy as np
import matplotlib.pyplot as plt
n = np.arange(0, 5)
hdn = ( (np.sin(np.pi/4) * (n-2)) / (np.pi * (n-2)))
wn = 0.5 - 0.5 * np.cos(2 * np.pi * n / 4)
hn = hdn * wn
hn[1] = 0.25
plt.figure()
plt.subplot(4, 1, 4)
plt.plot(n, hn)
plt.xlabel('n')
plt.ylabel('h(n)')
plt.title('Hanning Window Response')
plt.grid(True)
plt.show()  # Call show() to display the plot
