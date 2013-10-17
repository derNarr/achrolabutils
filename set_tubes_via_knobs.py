import sys
sys.path.append("D:\\software\\achrolabutils")

from achrolab import devtubes
from achrolab import devknobs

knobs = devknobs.DevKnobs()
devtub = devtubes.DevTubes()

#devtub.setVoltages(knobs.getStates()[0:3])

print knobs.state


