#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./setTubesToMax.py
#
# (c) 2010 Konstantin Sering, Nora Umbach, Dominik Wabersich
# <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content: Set all tubes on maximum before switching them on!
#
# input: --
# output: --
#
# created
# last mod 2010-12-02, KS

from achrolab.wasco.wasco import wasco, boardId
from achrolab.wasco.WascoConstants import DAOUT1_16, DAOUT2_16, DAOUT3_16

wasco.wasco_outportW(boardId, DAOUT1_16, 0xFFF)
wasco.wasco_outportW(boardId, DAOUT2_16, 0xFFF)
wasco.wasco_outportW(boardId, DAOUT3_16, 0xFFF)
