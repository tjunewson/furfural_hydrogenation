###1D volcano of facets 111 and 211 using polyfit
import numpy as np
import pylab as plt
from scipy.interpolate import make_interp_spline,interp1d

fig, (ax, ax1) = plt.subplots(2, 1, figsize=(20,16), gridspec_kw={'height_ratios': [1, 3]}, sharex=True, constrained_layout=True)


##mkm results
surfaces = ['Ru','Rh','Pt','Ni','Pd','Cu','Au','Ag']
raw_data = [(-2.43,-7.65),(-2.29,-4.77),(-1.82,-3.22),(-1.88,1.20),(-1.77,2.76),(-0.91,3.09),(-0.84,0.861),(-0.76,-3.125)]

X = [x[0] for x in raw_data]
Y = [y[1] for y in raw_data]

fit = np.polyfit(X, Y, 2)
f = np.poly1d(fit)
x_new = np.linspace(-3, 0, 300)
ax1.plot(x_new, f(x_new), color='black')

##experiments results
labels = ['Cu','Cu216Pd1','Cu20Pt1','PdCu','Pd','Ni','Pt']
raw_data_1 = [(-0.91,-2.71),(-0.97,-0.77),(-0.92,-1.78),(-1.52,-2.51),(-1.77,-2.86),(-1.88,-3.68),(-1.82,-3.08)]
X1 = [x[0]-0.1 for x in raw_data_1]
Y1 = [y[1] for y in raw_data_1]
ax.scatter(X1, Y1, color='black',marker='D',s=500)


##candidates in theory
metal_111 = {'Ag(111)': [-0.76], 'Au(111)': [-0.84],'Co(111)': [-1.85], 'Cu(111)': [-0.95], 'Ir(111)': [-1.92], 'Ni(111)': [-1.88],'Pd(111)': [-1.77], 'Pt(111)': [-1.82], 'Rh(111)': [-2.29], 'Ru(111)': [-2.43], 'Cr(111)': [-3]}
metal_211 = {'Ag(211)': [-0.88], 'Au(211)': [-0.92],'Co(211)': [-2.35], 'Cu(211)': [-1.48], 'Ir(211)': [-3.35], 'Ni(211)': [-2.62],'Pd(211)': [-2.16], 'Pt(211)': [-2.57], 'Rh(211)': [-2.90], 'Ru(211)': [-2.85]}

CuNi = {'Cu3Ni1':[-1.22], 'Cu2Ni2':[-1.85],'Cu1Ni3':[-1.99]}
CuPt = {'Cu3Pt1':[-1.14], 'Cu2Pt2':[-1.59],'Cu1Pt3':[-1.76]}
CuPd = {'Cu3Pd1':[-1.12], 'Cu2Pd2':[-1.30],'Cu1Pd3':[-1.52]}
CuCo = {'Cu3Co1':[-1.77], 'Cu2Co2':[-1.50],'Cu1Co3':[-1.81]}
CuCr = {'Cu3Cr1':[-2.38]}
SAA = {'Cu@Ir1':[-1.36],'Cu@Ni1':[-1.19],'Cu@Pd1':[-0.96],'Cu@Pt1':[-0.92],'Cu@Rh1':[-1.32],'Cu@Ru1':[-1.71]}

data = [metal_111, metal_211, SAA, CuNi, CuPt, CuPd, CuCo, CuCr]
colors = ['tab:black','tab:red','tab:green']
markers = ['o','^']

metals = ['Ag','Au','Co','Cu','Ir','Ni','Pd','Pt','Rh','Ru','Cr']
colors = ['silver','gold','pink','brown','lightblue','green','royalblue','gray','deepskyblue','lightseagreen','black']
colors_ba = ['green','gray','royalblue','pink','black']
colors_sa = ['lightblue','green','royalblue','gray','deepskyblue','lightseagreen']

for i, d in enumerate(data):
    x = [v[0]-0.1 for v in d.values()]
    l = [k for k in d.keys()]
    y = f(x)
    if i == 0:
        for iv, v in enumerate(x):
            y = f(v)
            ax1.plot(v,y,marker='o',color=colors[iv], markeredgewidth=0, markersize=30,  alpha = 0.7, lw=0, label=metals[iv])
    elif i == 1:
        for iv, v in enumerate(x):
            y = f(v)
            ax1.plot(v,y,marker='^',color=colors[iv],  markeredgewidth=0, markersize=30, alpha = 0.7, lw=0)
    elif i == 2:
        for iv, v in enumerate(x):
            y = f(v)
            ax1.plot(v,y,color= 'brown', marker="*", fillstyle="left", markeredgewidth=0, markersize=40, alpha = 0.9)
            ax1.plot(v,y,color= colors_sa[iv], marker="*", fillstyle="right" , markeredgewidth=0,markersize=40, alpha = 0.9)
    else:
        ax1.plot(x, y, color = 'brown', marker="p", fillstyle="left" , markeredgewidth=0,markersize=30, alpha = 0.7, lw=0)
        ax1.plot(x, y, color = colors_ba[i-3], marker="p", fillstyle="right" , markeredgewidth=0,markersize=30, alpha = 0.7, lw=0)

ax.set_xlim(-3,0)
ax.set_ylim(-5,0)
ax.tick_params(labelsize=30)
ax.set_ylabel("log(TOF (s$^{-1})$)", fontsize = 30)
ax1.set_ylim(-12,5)
ax1.tick_params(labelsize=30)
ax1.set_xlabel("$\Delta E_{FCHO}$ (eV)", fontsize = 30)
ax1.set_ylabel("log(TOF (s$^{-1}$))", fontsize = 30)
ax1.legend(ncol=2, fontsize = 25, frameon=False, loc = 2)
