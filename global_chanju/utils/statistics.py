import numpy as np

def f_bin(y):
    n = len(y)
    Q1, Q3 = np.percentile(y, [25, 75])
    IQR = Q3 - Q1
    bw = 2. * IQR / np.cbrt(n)
    if bw == 0:
        n_bin = 1
        print("Distribution is delta function")
    else:
        n_bin = int((max(y) - min(y)) // bw)
    return n_bin, (min(y), max(y)), bw

def asym_err(y, axis=-1, mode="median"):
    if mode == "median":
        m = np.median(y, axis=axis)
    else:
        m = np.mean(y, axis=axis)
    lower = m - np.percentile(y, 16, axis=axis)
    upper = np.percentile(y, 84, axis=axis) - m

    err = np.array([lower, upper])
    return m, err
