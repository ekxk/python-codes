# MAKE SEABORN BARPLOT with DISCONTINUED Y-AXIS
# from https://stackoverflow.com/a/5669301

# assuming the data is inside DataFrame dfp (modify according to actual data)
# with index as x data
# y_col as y data
# hue_col as hue data

dfp = pd.DataFrame()

fig,(ax,ax2) = plt.subplots(2, 1, sharex=True, 
                            figsize=[6,4],dpi=600,
                            gridspec_kw={'height_ratios': [1, 1]})

# plot the same data on both axes
p2 = sns.barplot(x=dfp.index, y=dfp["y_col"], hue=dfp["hue_col"],ax=ax)
p1 = sns.barplot(x=dfp.index, y=dfp["y_col"], hue=dfp["hue_col"],ax=ax2)

# only use one legend
p1.legend_.remove()
sns.move_legend(
        p2, "upper right",
        bbox_to_anchor=(0.99, 0.99), ncol=3, title=None, frameon=True,
        fontsize=12
)

# zoom-in / limit the view to different portions of the data (modify according to data)
ax2.set_ylim(0,1) # smaller y data
ax.set_ylim(15,25) # larger y data

# hide the spines between ax and ax2
ax2.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Make the spacing between the two axes a bit smaller
plt.subplots_adjust(wspace=0.15)

# MAKE DIAGONAL to indicate the discontinued axis
d = .015 # how big to make the diagonal lines in axes coordinates
# arguments to pass plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((1-d,1+d),(-d,+d), **kwargs) # top-left diagonal
ax.plot((-d,d),(-d,+d), **kwargs) # bottom-left diagonal
#ax.plot((1-d,1+d),(1-d,1+d), **kwargs) # bottom-left diagonal # this was for discontinued x-axis

kwargs.update(transform=ax2.transAxes) # switch to the bottom axes
#ax2.plot((-d,d),(-d,+d), **kwargs) # top-right diagonal # this was for discontinued x-axis
ax2.plot((1-d,1+d),(1-d,1+d), **kwargs) # top-right diagonal
ax2.plot((-d,d),(1-d,1+d), **kwargs) # bottom-right diagonal

# turn off y-label from seaborn then replace with fig y label
p2.set(ylabel=None)
p1.set(ylabel=None)
fig.supylabel('Percentage Change (%)',weight='bold')

# remove the ticks in top plot
p2.tick_params(bottom=False)  # remove the ticks

# add fig y label
fig.supxlabel('Time-series Data',weight='bold')

# save and show the plot
plt.savefig(path+f'discontinued_yaxis.png', bbox_inches='tight',facecolor='white',dpi=600) # for transparent bkg use: transparent=True
plt.show()
plt.close()
