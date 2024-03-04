"""
CHANGING FREQUENCY OF MATPLOTLIB'S AXIS TICK
using ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

from https://www.oreilly.com/library/view/matplotlib-plotting-cookbook/9781849513265/ch03s11.html
in https://stackoverflow.com/a/36229671/23166345
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

x = [0,5,9,10,15]
y = [0,1,2,3,4]

tick_spacing = 1

fig, ax = plt.subplots(1,1)
ax.plot(x,y)
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
plt.show()
