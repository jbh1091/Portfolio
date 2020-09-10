# -*- coding: utf-8 -*-

# Now we want to tweak the parameters of a single sine wave by modifying
# the values that define it. These are:
# Amplitude (A)
# Frequency (f)
# time (t)

# Not that although sine waves are typically used in time series,
# t doesn't have to always be time. It can be any dimension along
# which you measure an oscillation. We'll stick with time here for ease.

# We'll start by importing the same packages as before:
import numpy as np
import matplotlib.pyplot as plt

# And create our time vector similar to the last example:
t_start = 0
t_end = 4*np.pi
dt = 0.1

# We'll arbitrarily say these are in seconds for convenience.
t = np.arange(t_start,t_end,dt)

# Let's set up some subplots to compare the figures we generate.
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1,ncols=3,sharey=True)

# Now if we were to use the basic sin(t) function, we would get a sine wave
# with an amplitude and frequency of 1. Our units here are arbitrary since
# we are working with made-up data. An example would be amplitude in voltage
# and frequency in Hz (1/s) in EEG data.
y = np.sin(t)
ax1.plot(t,y)
ax1.set_title('f = 1, A = 1')
ax1.set_ylim(-2,2)

# To change the peak amplitude of a sine wave, multiply it by A.
A = 2
y = A*np.sin(t)
ax2.plot(t,y)
ax2.set_title('f = 1, A = 2')

# Strictly speaking, the amplitude is constantly changing in this wave.
# What we call A here is the peak amplitude, and scales the amplitude value at
# each timepoint.

# Frequency is similarly changed by multiplying inside the sine function.
f = 2
y = np.sin(f*t)
ax3.plot(t,y)
ax3.set_title('f = 2, A = 1')

# Now we can compare these waves to each other visually.
plt.show
