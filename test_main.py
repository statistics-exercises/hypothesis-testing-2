import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_xvals(self) :
        fighand = plt.gca()
        figdat = fighand.get_lines()[1].get_xydata()
        this_x, this_y = zip(*figdat)
        for i in range(len(this_x)) :
            self.assertTrue( np.fabs( minv+(i+0.5)*delx - this_x[i] )<1e-7, "the x-coordinates of your points are incorrect" )
            
    def test_normalisation(self) : 
        ssum = 0.
        fighand = plt.gca()
        figdat = fighand.get_lines()[1].get_xydata()
        this_x, this_y = zip(*figdat)
        for i in range(len(this_x)) : ssum = ssum + this_y[i]*delx
        self.assertTrue( np.fabs(ssum - 1.)<1e-7, "the histogram you have plotted is not normalised" )
