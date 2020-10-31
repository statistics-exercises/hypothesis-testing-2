import matplotlib.pyplot as plt
import numpy as np

# These three lines plot the probability density function we 
# are sampling from
xvals = np.linspace(-4,4,100)
yvals = np.exp(-xvals*xvals/2) / np.sqrt(2*np.pi)
plt.plot( xvals, yvals, 'k-')

# This generates your samples from the random variable
samples = np.random.normal(0.5,1,size=200)
# This is the number of bins in your histogram
nbins = 15
# This is the maximum and minimum of the range
minv, maxv = -4, 4 
# and this is the size of each of the bins in the histogram
delx = ( maxv - minv ) / nbins

# Use these two array to hold the midpoints of the bins and the counts 
# in each of the bins 
xvals, counts = np.zeros( nbins ), np.zeros( nbins )
# Your code to calculate the histogram goes here



# This will plot the histogram eventually.  I have plotted points rather than 
# a smooth curve to make the comparison with the smooth curve I plotted that 
# shows the distribution that has been sampled from more clear.
plt.plot( xvals, counts, 'bo')
plt.savefig("histogram.png")
