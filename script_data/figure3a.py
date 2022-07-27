import matplotlib.pyplot as  plt
import numpy as np
import pandas as pd

#excel path
xpath='data.xlsx'

#location of data
df = pd.read_excel(xpath, 'FCHOH_FCH2O')

fig, ax = plt.subplots(figsize=(8,8))

metals = df['surfaces']
colors = ['silver','gold','pink','brown','lightblue','green','royalblue','gray','deepskyblue','lightseagreen','black']

x = np.linspace(-4,0,100)
y = x
ax.plot(x, y, color = 'black', ls ='-')
y1 = 0
y2 = -4

ax.fill_between(x,y,y1,color='tab:orange',alpha=0.5)
ax.fill_between(x,y,y2,color='tab:green',alpha=0.5)

for i in range(len(df['Eads_FCHOH'][:10])):
    ax.scatter(df['Eads_FCHOH'][i], df['Eads_FCH2O'][i], color = colors[i], marker = 'o', s = 200, label = str(metals[i]))
    ax.annotate(metals[i], (df['Eads_FCHOH'][i], df['Eads_FCH2O'][i]+0.08),color = colors[i],fontsize=18)

#plot setting        
ax.set_xlim(-4, 0)
ax.set_ylim(-4, 0)
ax.set_xlabel('$\Delta E_{FCHOH}$ (eV)',fontsize=20)
ax.set_ylabel('$\Delta E_{FCH_2O}$ (eV)',fontsize=20)
ax.tick_params(labelsize=20)

plt.tight_layout()
