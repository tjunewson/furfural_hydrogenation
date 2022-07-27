##scaling of FCHO with other species
fig, ax = plt.subplots(figsize=(8,8))

xlpath = 'data.xlsx'
#df.set_index('surfaces', inplace=True)

#location of data
df = pd.read_excel(xlpath, 'scaling')
surfaces = np.array(df['surfaces'][0:10])
xx = np.linspace(-4,3,1000)



x = df['Eads_FCHO'][0:10]

Eads = ['Eads_H','Eads_FCHOH','Eads_FCH2O','Eads_FCH2OH']
labels = ['H','FCHOH','FCH$_2$O','FCH$_2$OH']
colors = ['gray','tab:orange','tab:green','royalblue']

for i,e in enumerate(Eads):
    y = df[e][0:10]
    ax.scatter(x1,y1, color=colors[i], s= 80) 
    a,b = np.polyfit(x,y,1)
    variance = np.var(y)
    residuals = np.var([(a*xx + b - yy)  for xx,yy in zip(x,y)])
    Rsqr = np.round(1-residuals/variance, decimals=2)
    print(a,b,Rsqr)
    ax.plot(xx, a*xx+b, color=colors[i], ls ='-', lw=1.5, label = labels[i] +': Y='+str(round(a,2))+'X'+str(round(b,2))+', R$^2$='+str(round(Rsqr,2)))

    
ax.set_xlim(-3,0)
ax.set_ylim(-4,1.0)



#plot setting
ax.set_xlabel('$\Delta E_{FCHO}$ (eV)',fontsize=20)
ax.set_ylabel('$\Delta E$ (eV)',fontsize=20)
ax.tick_params(labelsize=20)
#ax.legend(loc='upper left',fontsize=8)

#plt.show()
plt.tight_layout()
