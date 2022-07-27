###FEDs
import numpy as np
import pylab as plt
import pandas as pd
from scipy.interpolate import UnivariateSpline

def plot_energies(reaction_energies, activation_energies, ax, color, ls):
    """plots free energy diagrams given reaction energies and activation
        energies,
    which should be same-length lists and a matploblit axes object 
    """
    half_width = 0.3
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    rxn_pathway = [0, 1, 2, 3, 4] # for stoichiometry
    #IS_energy = 0.
    IS_energy = 0.
    lw = 2
    for i, rxn_number in enumerate(rxn_pathway):
        if i == 0:
            ax.plot([-half_width, half_width], [IS_energy, IS_energy], ls, color=color, lw = lw)
        FS_energy = IS_energy + reaction_energies[rxn_number] 
        TS_energy = IS_energy + activation_energies[rxn_number] 
        ax.plot([i + 1 - half_width, i + 1 + half_width], [FS_energy, FS_energy], ls, color=color, lw = lw)
        if abs(TS_energy - IS_energy) < 0.001 or abs(TS_energy - FS_energy) < 0.001:
            ax.plot([i + half_width, i + 1 - half_width], [IS_energy, FS_energy], ls, color=color, lw = lw)
        else:
            A = UnivariateSpline([i + half_width, i + 0.5, i + 1 - half_width], 
                                 [IS_energy, TS_energy, FS_energy],k=2) 
            x = np.linspace(i + half_width, i + 1 - half_width)
            ax.plot(x, A(x), ls, color=color, lw = lw) 
        IS_energy = FS_energy
    return ax

#excel path
xpath='data.xlsx'
#location of data
df = pd.read_excel(xpath, 'pathway')



energy_dict = {}

energy_dict['Au(111)'] = list(df['Au(111)'])[:12]
energy_dict['Cu(111)'] = list(df['Cu(111)'])[:12]
energy_dict['Pt(111)'] = list(df['Pt(111)'])[:12]


print(energy_dict)

#metals = ['Au', 'Cu','Pt', 'Rh'] 
#colors = ['gold', 'brown', 'black', 'lightblue']
metals = ['Au(111)','Cu(111)','Pt(111)'] 
colors = ['gold', 'brown', 'black']
ls1 = '-'
ls2 = '--'
lss = [ls1,ls2]
paths = ['via FCHOH','via FCH$_2$O']

fig, ax = plt.subplots(figsize=(20,8)) 
for metal, color in zip(metals, colors):
    dE1, Ea2, dE2, Ea3, dE3, Ea4, dE4, Ea5, dE5, Ea6, dE6, dE7 = energy_dict[metal]
    Ea_1 = [0, Ea2, Ea3, Ea5, 0]
    Er_1 = [dE1, dE2, dE3, dE5, dE7]
    Ea_2 = [0, Ea2, Ea4, Ea6, 0]
    Er_2 = [dE1, dE2, dE4, dE6, dE7]
    ax1 = plot_energies(Er_1, Ea_1, ax, color, lss[0])
    ax2 = plot_energies(Er_2, Ea_2, ax, color, lss[1])
    handles = [tuple(ax.plot([-99, -98], [-99, -98], '-', color=color)) for color in colors]
    handles2 = [tuple(ax.plot([-99, -98], [-99, -98], ls=ls, color='black')) for ls in lss]
    ax1.legend(handles, metals, fontsize=25)
    ax2.legend(handles2, paths, fontsize=25)
    ax.set_xlim([-0.5, 5.5])
    ax.set_ylim([-1.5, 2])
    ax.set_ylabel("$\Delta$G (eV)", fontsize = 30)
    plt.yticks(fontsize=25) 
    ax.set_xticks([0, 1, 2, 3, 4, 5])
    ax.xaxis.tick_top()
    ax.set_xticklabels(['FCHO(g)+H$_2$(g)', 'FCHO*+H$_2$(g)', 'FCHO*+2H*', 'FCHOH*/FCH$_2$O*+H*','FCH$_2$OH*', 'FCH$_2$OH(g)'], rotation=10., fontsize = 20)
