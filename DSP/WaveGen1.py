# -*- coding: utf-8 -*-

# Here we want to walk through the basic process of generating
# and visualizing sinusoids of various amplitudes, lengths,
# and frequencies.

# First, import a few necessary packages:
import numpy as np
import matplotlib.pyplot as plt

# Sine waves complete one full cycle (or one trip around the unit circle)
# every 2pi radians. So for one oscillation, we can create our x values
# from 0 to 2pi, and our y values as a function of the x values.

# Set a few constants to make things easier to change later.
# Avoid hard coding whenever possible!
x_start = 0
x_end = 2*np.pi
dx_len = 100

# For ease we just want 100 points in x, but you could just as
# easily define a set interval without doing any math here.
dx = (x_end - x_start)/dx_len #step size

x = np.arange(x_start,x_end,dx)
y = np.sin(x)

# Now a basic plot of our values:
plt.plot(x,y)
plt.show