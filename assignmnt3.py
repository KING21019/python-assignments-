# using any mathematical function or equation to give graphical representation like star,graph
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 400)
y1 = x**2 - 2*x + 1           
y2 = np.sin(x)
plt.figure(figsize=(10, 5))
plt.plot(x, y1, label='y = x² - 2x + 1', color='blue')
plt.plot(x, y2, label='y = sin(x)', color='red')
plt.title("Graph of Quadratic and Sine Functions")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()