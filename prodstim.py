"""
prodstim.py:

Script used to produce correctly-encoded images of different stimuli from the TUBvision code, for presentation on the black and white monitor.
"""

from stimuli import *
import numpy as np
import matplotlib.pyplot as ppl
import pylab
import eizoGS320

if __name__=='__main__':

    #nparray=cornsweet((8, 8), 16, 1,  mean_lum=511)
    #array2=todorovic(nparray, 6, 8)

    #nparray= whites_illusion_bmcc((3, 4), 512, 1, 2, mean_lum=511,  start='high')
    #nparray=square_wave((3,4), 512, 1, 5, mean_lum=512, period='ignore', start='high')
    nparray=whites_illusion_gil((6,8), 256, 1, 5, mean_lum=512, start='low')
    #ppl.imshow(nparray)
    #pylab.show()

    import Image
    newarray=eizoGS320.encode_np_array(nparray)
    #ppl.imshow(nparray)
    #pylab.show()

    pil_im = Image.fromarray(newarray)
    pil_im.save("whiteillusiongil.png")
