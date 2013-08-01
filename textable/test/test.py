
from numpy import *
from uncertainties import *

from textable import table

def test_table():
    x = array([1., 2., 3.])
    y = array([ufloat(2, 0.1), ufloat(4, 0.5), ufloat(2, 0.04)])

    f = open('test.tex', 'w')
    f.write(table(['x', 'y'], [x, y]))
    f.close()

