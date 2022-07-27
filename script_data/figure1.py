import matplotlib.pyplot as  plt
import numpy as np
import pandas as pd
#excel path
xpath='data.xlsx'

#location of data
df = pd.read_excel(xpath, 'scaling')

#barwidth
bw = 0.2

# Set position of bar on X axis 
br1 = np.arange(10) 
br2 = [x + bw for x in br1]

#plot
fig, (ax1,ax2) = plt.subplots(2, sharex=True)
fig.set_size_inches(6, 8)

ax1.bar(br1, df['ads_flat_111'][0:10], color ='lightblue', width = bw, 
        edgecolor ='grey', label ='flat') 
ax1.bar(br2, df['ads_up_111'][0:10], color ='gold', width = bw, 
        edgecolor ='grey', label ='upright') 
ax2.bar(br1, df['ads_flat_211'][0:10], color ='lightblue', width = bw, 
        edgecolor ='grey', label ='flat') 
ax2.bar(br2, df['ads_up_211'][0:10], color ='gold', width = bw, 
        edgecolor ='grey', label ='upright') 

xx = np.linspace(-1,11,100)
y = xx*0
surface = list(df['SURFACES'][0:10])
print(surface)
for ax in [ax1,ax2]:
    ax.plot(xx,y,color='black',lw=0.5)
    ax.set_xticks([r + 0.5*bw for r in np.arange(10)])
    ax.set_xticklabels(surface) 
    ax.set_ylabel('$\Delta G_{FCHO}$ (eV)', fontsize=25)
    ax.tick_params(labelsize=20)
    ax.set_xlim(-0.2,9.4)
    ax.set_ylim(-3,0.5)

ax1.legend(fontsize=20)
plt.tight_layout()
