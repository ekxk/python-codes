"""
Make scatter plots using seaborn jointplot,
3 subplots (modify as needed),
with regression line fit in red color (changeable),
showing the text of regression equation and pearson correlation and its p-value (scipy stats),
with histogram and kde fit in the margins

"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import matplotlib.image as mpimg


def scatter_density_plot(df_in, x_column, y_column, s=5, cmap='viridis', x_title=r'Measured (W $m^{-2}$)', y_title=r'Modeled (W $m^{-2}$)'):
    if df_in.loc[:,y_column].isnull().any():
        df = df_in.copy().dropna()
    else:
        df = df_in.copy()
      
    ############### 1. CREATE PLOTS
    # plot scatter with regression line, and histogram with kde lines in the margin axes
    h = sns.jointplot(data=df,x=x_column, y=y_column, kind='reg', 
                      scatter_kws={'s': 1},
                      marginal_kws=dict(bins=15, fill=False))
  
    # set the color of regression line to red
    regline = h.ax_joint.get_lines()[0]
    regline.set_color('red')
    regline.set_zorder(5)

    #calculate slope and intercept of regression equation
    slope, intercept, r, p, sterr = stats.linregress(x=h.ax_joint.get_lines()[0].get_xdata(),
                                                       y=h.ax_joint.get_lines()[0].get_ydata())
    
    # calculate pearson correlation and its p-value
    r, p = stats.pearsonr(df[x_column], df[y_column])
    
    # add regressopm equation and pearson corelation and its p-value to the plot
    #ax = plt.gca()
    h.ax_joint.text(.05, .93, f'y = {slope:.3f}x + {intercept:.3f}\nr={r:.2f}, p={p:.2g}',
                    va='top', fontsize=14,
                    transform=h.ax_joint.transAxes)
  
    # Set x and y axes labels
    # JointGrid has a convenience function
    #h.set_axis_labels(x_title, y_title, fontsize=16)
    # or set labels via the axes objects
    h.ax_joint.set_xlabel(x_title)#, fontweight='bold')
    h.ax_joint.set_ylabel(y_title)#, fontweight='bold')
    # labels appear outside of plot area, so auto-adjust
    h.figure.tight_layout() 

    # to set limit in axes, but already done inside jointplot
    #h.ax_joint.set_xlim(-10,1050)
    #h.ax.set_ylim(-10,1050)

    # make 1:1 line
    h.ax_joint.axline((0, 0), slope=1, color='k',linestyle='dashed')

    # recolor patches/histogram in marginal axes
    for patch in h.ax_marg_x.patches:
        patch.set_facecolor('0.9')

    for patch in h.ax_marg_y.patches:
        patch.set_facecolor('0.9')

    ############### 2. SAVE PLOTS
    h.savefig(path+f'h{i}_{y_column}.png', bbox_inches='tight',facecolor='white',dpi=600)
    plt.close(h.fig)

############### 3. RUN AND CREATE SUBPLOTS FROM SAVED IMAGES
# RUN!
model_y_axis = 'y_axis_name' # modify as needed
for i,irrad_now in enumerate(['subplot1','subplot2','subplot3']):
    scatter_density_plot_subplots(i, df_data, 'x_axis_name', f'{model_y_axis}', s=5, cmap='viridis')

fig, axs = plt.subplots(1,3, figsize=(10,3), dpi=600, sharey=True)

axs[0].imshow(mpimg.imread(path+f'h0_{model_y_axis}.png'))
axs[1].imshow(mpimg.imread(path+f'h1_{model_y_axis}.png'))
axs[2].imshow(mpimg.imread(path+f'h2_{model_y_axis}.png'))


# turn off x and y axis
[ax.set_axis_off() for ax in axs.ravel()]

# name each subplots
for i,name in enumerate(['subplot1','subplot2','subplot3']):
    axs[i].text(0.5,1.03,name,va='bottom',ha='center',weight='bold',transform=axs[i].transAxes)

# Make the spacing between the two axes a bit smaller
plt.subplots_adjust(wspace=0.05)

plt.savefig(path+f'scatter_and_density_{model_y_axis}_vs_x_axis_name.png', bbox_inches='tight',facecolor='white',dpi=600)
plt.show()
plt.close()
