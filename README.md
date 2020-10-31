# The need for hypothesis testing

When you looked at the graph from the previous exercise you will have seen that the histogram and the probability density function look similar.  They are not identical but they are probably similar enough for you to guess that the sampled variable and the distribution that was plotted are the same.

There is an obvious problem with this line of reasoning.  The statement "the two graphs look similar" is not at all quantitative.  If we to write in a paper "this graph looks similar to that one," we would thus look silly.  Hypothesis testing is thus, fundamentally, about ensuring that we quantitatively compare the data that we get from an experiment with a model distribution.  If we use hypothesis testing properly we thus no longer need to say data set X looks like what would be predicted by model Y.  We can instead put a numerical value on their degree of similarity. 

__To see why this is important I want you to construct a second histogram.__  This time I have generated 200  normal random variables with expectation 0.5 and variance 1 for you and stored them in the array called `samples`.  The variable we have sampled here is another continuous random variable.  Your histogram will thus be an estimate of the probability density function for the underlying random variable.

As in the previous task to pass the test your histogram should have 15 bins (`nbins`).  The first of these bins should start at -4 (`minv`) and the last of them should end at +4 (`maxv`).  The width of each bin should be equal to `delx`.  I have also created two numpy arrays for you:

1. `xvals` - will eventually hold the midpoints of all the bins
2. `counts` - will eventually hold the estimate of the probability density at the midpoint 

I have plotted the probability density function for a standard normal random variable with you.  If you compare the histogram that you generate with this pdf would you be able to tell that the distribution that was sampled from is different from the distribution that has been plotted?
