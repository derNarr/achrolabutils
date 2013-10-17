#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# fittubesmanual.py
#
# (c) 2012 Konstantin Sering <konstantin.sering [aet] gmail.com>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content:
#
# input: --
# output: --
#
# created 2012-08-28 KS
# last mod 2012-08-30 16:01 KS

"""
fittubesmanual collects code that can be used to fit functions the voltage -
luminance data.

"""

import pickle
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

f = open("../../calibration_tubes_raw_20120827_1858.pkl")
f = open("calibration_tubes_raw_20120829_1404.pkl")

voltages_r   = pickle.load(f)
voltages_g   = pickle.load(f)
voltages_b   = pickle.load(f)
voltages_all = pickle.load(f)
xyY_r        = pickle.load(f)
xyY_g        = pickle.load(f)
xyY_b        = pickle.load(f)
xyY_all      = pickle.load(f)
spectra_r    = pickle.load(f)
spectra_g    = pickle.load(f)
spectra_b    = pickle.load(f)
spectra_all  = pickle.load(f)

f.close()

# fit a luminance function -- non-linear regression model based
# on Pinheiro & Bates (2000)

def func(x, a, b, c):
    x = np.array(x)
    return a + (b - a)*np.exp(-np.exp(c)*x)

# red channel
Y_r = np.array([x[2] for x in xyY_r])
v_r = np.array([x[0] for x in voltages_r])
# clip the last data, because the tubes make something weired in the beginning
Y_r = Y_r[v_r<3500]
v_r = v_r[v_r<3500]
popt_r, pcov_r = curve_fit(func, v_r, Y_r, p0=[67.8, -6.7, -9.0])

# green channel
Y_g = np.array([x[2] for x in xyY_g])
v_g = np.array([x[1] for x in voltages_g])
# clip the last data, because the tubes make something weired in the beginning
Y_g = Y_g[v_g<3500]
v_g = v_g[v_g<3500]
popt_g, pcov_g = curve_fit(func, v_g, Y_g, p0=[138.7, -16.4, -8.9])

# blue channel
Y_b = np.array([x[2] for x in xyY_b])
v_b = np.array([x[2] for x in voltages_b])
# clip the last data, because the tubes make something weired in the beginning
Y_b = Y_b[v_b<3500]
v_b = v_b[v_b<3500]
popt_b, pcov_b = curve_fit(func, v_b, Y_b, p0=[58.2, -2.7, -9.8])

plt.plot(range(1000, 4000), func(range(1000, 4000), *popt_r), 'r-')
plt.plot(v_r, Y_r, 'r.')
plt.plot(range(1000, 4000), func(range(1000, 4000), *popt_g), 'g-')
plt.plot(v_g, Y_g, 'g.')
plt.plot(range(1000, 4000), func(range(1000, 4000), *popt_b), 'b-')
plt.plot(v_b, Y_b, 'b.')
plt.ylabel("Luminance in cd/m^2")
plt.xlabel("Voltages (input to wasco card)")
plt.title("Luminance-voltages functions for all three colours")
plt.show()

filename = "parameter_tubes_75_abs.pkl"

with open(filename, 'wb') as f:
    pickle.dump(float(popt_r[0]), f)
    pickle.dump(float(popt_r[1]), f)
    pickle.dump(float(popt_r[2]), f)
    pickle.dump(float(popt_g[0]), f)
    pickle.dump(float(popt_g[1]), f)
    pickle.dump(float(popt_g[2]), f)
    pickle.dump(float(popt_b[0]), f)
    pickle.dump(float(popt_b[1]), f)
    pickle.dump(float(popt_b[2]), f)

