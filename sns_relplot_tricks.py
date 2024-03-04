"""
Situation: 5 category to plot using seaborn's relplot, using "col" argument. 
setting the column number 3 and row number 2.
But, seaborn would plot the second row as 'Align Left', while I want 'Align Right'.
Maybe I can resort to GridSpec, but I want the ease of use from relplot's col and hue.
I came up with this trick, add one more category so that I have 6, 
use the col_order to specify that new category location in the spot that I want to be empty, 
and then set that category to be invisible.
"""
import seaborn as sns
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

# make subplots with 2 rows, 3 columns, 2nd row is aligned to the right.
# demonstration of what i want to do, using plt subplots blank fig:
#fig, axs = plt.subplots(ncols=3, nrows=2)
# remove the underlying axes
#for ax in axs[1:, 0]:
#    ax.remove()
#plt.show()
#plt.close()

# assume the data is in DataFrame df which will be turned into a long form df_long. 
# columns are x_column, y_column, model. 
# model has value of either ['cat1', 'cat2', 'cat3','cat4', 'cat5']
df_long = pd.melt(df.reset_index(), id_vars='x_column', value_vars=df.columns.tolist(),
                  var_name='model', value_name='y_column')
# make subplots with 2 rows, 3 columns, 2nd row is aligned to the right.
df_long.loc[len(df_long),:] = [np.nan,'skip',np.nan] # the trick! adding a new row (at the end, i.e. len(df_long))

# the trick
# 1 . preparation
# Map col to marker styles
col_to_marker = {'cat1': 'o', 'cat2': 's', 'cat3': 's', 'skip':'s', 'cat4':'s','cat5':'s'}
kwargs = {'markeredgewidth': 0.5, 'markers': col_to_marker}
# 2. the plotting
g = sns.relplot(
    data=df_long,
    x="x_column", y="y_column", col="model", hue="model",
    col_order=['cat1', 'cat2', 'cat3','skip', 'cat4', 'cat5'],
    kind="line", marker="s",markersize=5,
    palette="crest", linewidth=2, zorder=5,
    col_wrap=3, height=2, aspect=1.3, legend=False, **kwargs
)
# 3. the deletion
for (i,j,k), data in g.facet_data():
    if (data.model == 'skip').any():
        ax = g.facet_axis(i, j)
        ax.set_axis_off()

# ADDITIONAL THINGS: adding ticks and labels to all subplots, not only the outer ones (default of seaborn relplot)
# e.g. x axis is DateTime, y axis is just number
# Default, with shared x-axes, only the "outer" xlabels are set visible, 
# the inner ones are set invisible (and seaborn leaves them to be empty strings). 
# So, to see all labels, you need to set both the strings and the visibility explicitly.
# At the end, you might want to call plt.tight_layout() to remove the overlapping.

# assume year start and end is 2022 and 2023
year_start = 2022
year_end = 2023

# Set the locator
locator = mdates.YearLocator()  # every year
fmt = mdates.DateFormatter('%Y')

for ax in g.axes.flat:
    ax.set_xlabel('X Label here', visible=True)
    ax.set_ylabel('Y Label here', visible=True)
    ax.tick_params(axis='both', which='both', labelbottom=True, labelleft=True) #  labelsize=7, 
    X = plt.gca().xaxis
    X.set_major_locator(locator)
    ax.set_xlim(np.datetime64(f'{year_start-1}-12-01T01:00:00'), np.datetime64(f'{year_end}-12-31T23:00:00'))
    # set y axis ticks
    tick_spacing = 25
    ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

plt.tight_layout()

plt.savefig(path+'picture_name.png',dpi=600,facecolor='white',bbox_inches='tight')
plt.show()
plt.close()
