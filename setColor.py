from psychopy import visual, core

mywin = visual.Window([2048,1536], monitor='mymon', units='deg',
        color=255, colorSpace='rgb255', allowGUI=False, screen=1)

surround1 = visual.PatchStim(win=mywin, units='deg', size=8,
        pos=[4,0], sf=0, color=150, colorSpace='rgb255')
infield1  = visual.PatchStim(win=mywin, units='deg', size=2,
        pos=[4,0], sf=0, color=100, colorSpace='rgb255')
surround2 = visual.PatchStim(win=mywin, units='deg', size=8,
        pos=[-4,0], sf=0, color=100, colorSpace='rgb255')
infield2  = visual.PatchStim(win=mywin, units='deg', size=2,
        pos=[-4,0], sf=0, color=50, colorSpace='rgb255')

surround1.draw()
infield1.draw()
surround2.draw()
infield2.draw()
mywin.flip()
core.wait(.5)

surround1.setColor(255)
infield1.setColor(255)
surround2.setColor(255)
infield2.setColor(255)
mywin.flip()
core.wait(.5)

surround1.setColor(100)
infield1.setColor(90)
surround2.setColor(200)
infield2.setColor(120)
mywin.flip()
core.wait(.5)

surround1.setColor(255)
infield1.setColor(255)
surround2.setColor(255)
infield2.setColor(255)
mywin.flip()
core.wait(5)

surround1.setColor(120)
infield1.setColor(100)
surround2.setColor(180)
infield2.setColor(150)
mywin.flip()
core.wait(1)

