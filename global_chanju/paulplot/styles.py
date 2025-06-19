from matplotlib.ticker import AutoMinorLocator, FuncFormatter, LogLocator, LogFormatter
from matplotlib.ticker import FuncFormatter
import numpy as np

def neat_style(ax, n_ticks=2):
    ax.xaxis.set_minor_locator(AutoMinorLocator(n_ticks))
    ax.yaxis.set_minor_locator(AutoMinorLocator(n_ticks))
    ax.figure.tight_layout()

def nice_style(ax, logx=False, logy=False, xlim=None, ylim=None, xlabel=None, ylabel=None, xticks=None, yticks=None, xtick_label=None, ytick_label=None):
    
    # Set labels
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)
    
    # Set ranges
    if xlim is not None:
        ax.set_xlim(xlim)
    if ylim is not None:
        ax.set_ylim(ylim)

    if logx:
        ax.set_xscale('log')
        ax.xaxis.set_major_locator(LogLocator(base=10.0))
        ax.xaxis.set_minor_locator(LogLocator(base=10.0, subs='auto', numticks=100))
    else:
        ax.xaxis.set_minor_locator(AutoMinorLocator(2))
    if logy:
        ax.set_yscale('log')
        ax.yaxis.set_major_locator(LogLocator(base=10.0))
        ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs='auto', numticks=100))
    else:
        ax.yaxis.set_minor_locator(AutoMinorLocator(2))

    if xticks is not None:
        ax.set_xticks(ticks=xticks)
    if xtick_label is not None:
        ax.set_xticklabels(labels=xtick_label)
    if yticks is not None:
        ax.set_yticks(ticks=yticks)
    if ytick_label is not None:
        ax.set_yticklabels(labels=ytick_label)

    try:
        ax.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
    except:
        pass

    ax.figure.tight_layout()

def base_ten(x):
    if x <= 1e-15:
        return r"$0.0$"
    else:
        top = np.floor(np.log10(np.abs(x)))
        res = x / 10**top
        return r"$%.1f \times 10^{%d}$"%(res, top)
