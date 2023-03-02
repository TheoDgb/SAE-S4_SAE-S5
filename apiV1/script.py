import matplotlib.pyplot as plt
import numpy as np

# y = np.array([335,125,125,115])
# mylabels = ["Apples","Bananas","Cherries","Dates"]
#
# plt.pie(y,labels=mylabels,startangle=90)
# plt.draw()
# plt.savefig('image.png',dpi=100)




# test mais marche pas
# accidents_data = pd.read_csv('../data/lieux-2021.csv')
# plt.plot(accidents_data['Num_Acc'], accidents_data['catr'])

# ca affiche le graphe de base
y = np.array([335, 125, 125, 115])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels, startangle = 90)
plt.savefig("public/images/image.png")
plt.show()