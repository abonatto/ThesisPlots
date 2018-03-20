import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use(['thesis'])

x = np.linspace(0.75, 1.25, 201)

def model(x, p):
    return x ** (2 * p + 1) / (1 + x ** (2 * p))

fig, ax = plt.subplots()
for p in [10, 15, 20, 30, 50, 100]:
    ax.plot(x, model(x, p), label=p)
ax.legend(title=r'Order')
ax.set(xlabel=r'Voltage / $V_\mathrm{{gap}}$')
ax.set(ylabel=r'Current / $I_\mathrm{{gap}}$')
ax.autoscale(tight=True)
fig.savefig('figures/fig1.pdf')
fig.savefig('figures/fig1.pgf')
fig.savefig('figures/fig1.jpg', dpi=300)
