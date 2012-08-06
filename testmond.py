"""
testmond.py:
Produces Mondrian stimuli using functions from TU Berlin's TUBvision code. The functions called are in TUBvision's mondrian.py
"""
if __name__=='__main__':

    from mondrian import *
    import numpy as np
    import matplotlib.pyplot as ppl
    import pylab
    import eizoGS320

    i=0
    colorlist=[]
    for i in range(1023):
        colorlist.append(i)

    nparray=create_mondrian((1536, 2048), 5, colorlist, weights=None, accuracy=.05, max_cycles=1000, write=False)

    ppl.imshow(nparray)
    pylab.show()

    import Image
    newarray=eizoGS320.encode_np_array(nparray)
    # # ppl.imshow(newarray)
    # # pylab.show()

    pil_im = Image.fromarray(newarray)
    pil_im.save("mondtest2.png")
