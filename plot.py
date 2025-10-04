import sys
import matplotlib.pyplot as plt
xpoints=(1,2,3)
ypoints=(4,5,6)
plt.plot(ypoints,marker='o--')
plt.plot(xpoints,marker='o--')
plot.savefig(sys.stdout.buffer)
sys.stdout.flush()
plt.show()
