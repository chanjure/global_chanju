import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import rc, rcParams

def get_rc():
    return {'W': 6., 'r': 0.75, 'fonts': 18, 'ms': 7}

def set_rc(scale=1.0):
    scale = scale
    W = 6. * scale
    r = 0.75

    fonts = 18
    ms = 7

    rcParams.update({
        'axes.prop_cycle': plt.cycler('marker', ['o','x','^','*','s','p','+','v','P','D','h','X']) + plt.cycler('linestyle', ['-','--', '-.', ':']*3),
        'figure.figsize': (W, W*r),   # 4:3 aspect ratio
        'font.size' : fonts* scale,      # Set font size to 11pt
        'axes.labelsize': fonts* scale,  # -> axis labels
        'xtick.direction':'in',       # xticks
        'xtick.top': True,
        'xtick.major.size': 6 * scale,
        'xtick.major.width': 1 * scale,
        'xtick.minor.visible': True,
        'xtick.minor.size': 3 * scale,
        'xtick.minor.width': 1 * scale,
        'xtick.major.pad': 5.5 * scale,
        'ytick.direction':'in',       # yticks
        'ytick.right': True,
        'ytick.major.size': 6 * scale,
        'ytick.major.width': 1 * scale,
        'ytick.minor.visible': True,
        'ytick.minor.size': 3 * scale,
        'ytick.minor.width': 1 * scale,
        'ytick.major.pad': 5 * scale,
        'legend.fontsize': fonts* scale, # -> legends
        'legend.frameon': False,
        'lines.markersize':ms* scale,
        'lines.markerfacecolor':'none',
        'lines.linewidth':1.*scale,
        'errorbar.capsize':3.*scale,
        'font.family': 'lmodern',
        'text.usetex': True,
        'text.latex.preamble': (      # LaTeX preamble
            r'\usepackage{lmodern}'r'\usepackage{amsmath}'
            r'\usepackage{amsfonts}'
            # ... more packages if needed
                               ),
        })
