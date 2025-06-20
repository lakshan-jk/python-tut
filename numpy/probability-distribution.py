from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
plt.plot(x, norm.pdf(x, 11, 1))
plt.title("Normal Distribution")
plt.show()
