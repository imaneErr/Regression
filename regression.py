

import pandas as pd
import matplotlib.pyplot as plt

d = {'Seminaire': [94,90,95,89,88,92,92,97,91],
        'Tutorial': [83,86,89,87,85,86,85,81,83],
        'Ex_cathedra': [80,85,81,81,79,83,78,80,82],
         }


df = pd.DataFrame(d)
print(df)

plt.scatter(df['Seminaire'], df['Tutorial'])
plt.title('Seminaire Vs Interest Rate', fontsize=14)
plt.xlabel('Seminaire', fontsize=14)
plt.ylabel('Tutorial', fontsize=14)
plt.grid(True)
plt.show()
