from numpy import *
import eizoGS320

from psychopy import visual
import Image

a = repeat(750, 2048*1536).reshape(1536, 2048)

h = 200
a_stim = transpose(repeat(repeat([750, 600, 750, 650, 750], [804, h, 40, h,
    804]), h).reshape(2048, h))

bg = 750
inf1 = 200
sur1 = 650
inf2 = 300
sur2 = 550

size_inf = 80    # about 1deg, ca. 2cm
size_sur = 190   # about 8deg, ca. 5cm
size_diff = 20
size_bg = (2048 - 2*size_sur - size_diff)/2     # 824px

a_stim = transpose(array(transpose([repeat(repeat([bg, sur1, bg, sur2, bg],
    [size_bg, size_sur, size_diff, size_sur, size_bg]),
    (size_sur-size_inf)/2),
    repeat(repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg],
    [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2,
    size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2,
    size_bg]), 55),
    repeat(repeat([bg, sur1, bg, sur2, bg], [size_bg, size_sur, size_diff,
    size_sur, size_bg]), (size_sur-size_inf)/2)])).reshape(2048,
    165))

#tile(a_stim, (size_sur, 2048))
print(a_stim)
print(a)

print(rank(a_stim))
# the same in shorter: a.ndim

print(a_stim.shape)
print(a.shape)
# print(a.dtype)
# print(a.itemsize)
# print(a.data)

#np_bg = eizoGS320.encode_np_array(a)
np_stim = eizoGS320.encode_np_array(a_stim)
#
#print(np_stim)
#print(np_stim.shape)
#
#pil_bg = Image.fromarray(np_bg)
pil_stim = Image.fromarray(np_stim)
#
#pil_bg.save("background.bmp")
pil_stim.save("stim.bmp")

