import matplotlib.pyplot as plt
import numpy as np

y = np.array([335,125,125,115])
mylabels = ["Apples","Bananas","Cherries","Dates"]

plt.pie(y,labels=mylabels,startangle=90)
plt.draw()
plt.savefig('image.png',dpi=100)