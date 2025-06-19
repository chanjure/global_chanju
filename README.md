Global Chanju Settings
======================

Make nice plots using matplotlib.
Some useful statistics functions.

Installation
------------
```$ pip install .```

Example
-------
```
import matplotlib.pyplot as plt

from global_chanju.paulplot.rc_setter import set_rc
from global_chanju.paulplot.rc_setter import get_rc
from global_chanju.paulplot.styles import nice_style

set_rc(scale=1)

n_fig = 2
fig_width = n_fig * get_rc()['W']
fig_hight = get_rc()['W'] * get_rc()['r']
fig, axs = plt.subplots(1, n_fig, figsize=(fig_width, fig_hight))

axs[0].plot(something)
nice_style(axs[0],
           xlim=(-1,1), ylim=(-2,2),
           xlabel="X-axis", ylabel="Y-axis",
           ...
        )

axs[1].plot(something else)
nice_style(axs[1],
           xlim=(-1,1), ylim=(-2,2),
           xlabel="X-axis", ylabel="Y-axis",
           ...
        )

plt.savefig(plot dir)
plt.show()
```
