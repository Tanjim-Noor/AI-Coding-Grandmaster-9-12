import matplotlib.pyplot as plt

x = [0.5, 10, 15, 20, 25, 30]
y1 = [10, 15, 20, 20, 30, 15, 0]
y2 = [10, 12, 15, 12, 20, 10, 0]

plt.plot(x, y1, linestyle='dashed', marker='D', label='Velocity curve 1')
plt.plot(x, y2, linestyle='dashed', marker='D', label='Velocity curve 2')
plt.title('Velocity-Time Graph')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.xlim(5, 25)
plt.ylim(5, 25)
plt.legend()
plt.grid(True)
plt.show()
