from numpy import *
import eizoGS320

from psychopy import visual
import Image

a = repeat(750, 2048*1536).reshape(1536, 2048)

h = 200
a_stim = transpose(repeat(repeat([750, 600, 750, 650, 750], [804, h, 40, h,
    804]), h).reshape(2048, h))

print(a_stim)

print(rank(a))
# the same in shorter: a.ndim

print(a_stim.shape)
print(a.shape)
# print(a.dtype)
# print(a.itemsize)
# print(a.data)

np_bg = eizoGS320.encode_np_array(a)
np_stim = eizoGS320.encode_np_array(a_stim)

print(np_stim)
print(np_stim.shape)

pil_bg = Image.fromarray(np_bg)
pil_stim = Image.fromarray(np_stim)

pil_bg.save("background.bmp")
pil_stim.save("stim.bmp")

