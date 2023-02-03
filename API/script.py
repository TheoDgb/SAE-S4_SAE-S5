import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# accidents_data = pd.read_csv('../data/lieux-2021.csv')
# plt.plot(accidents_data['Num_Acc'], accidents_data['catr'])

y = np.array([335, 125, 125, 115])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels, startangle = 90)
plt.show()
plt.savefig("image.png")