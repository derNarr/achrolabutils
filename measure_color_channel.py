from achrolab.calibtubes import CalibTubes
from achrolab.eyeone.eyeone import EyeOne
import time
import random
eyeone = EyeOne(dummy=False)
caltub = CalibTubes(eyeone)
caltub.setVoltages((0xFFF, 0xFFF, 0xFFF))


voltages_g = []
xyY_g = []
spectra_g = []
random.seed(4)

for i in range(1):
    #measure_green=caltub.measureOneColorChannel(color="green", n=50, each=1)
    #voltages_g=voltages_g+measure_green[0]
    #xyY_g=xyY_g+measure_green[1]
    #spectra_g=spectra_g+measure_green[2]

    #def fun(self,step, i,n):
    #    return ((0xFFF - step * n)+(step*i))

    def fun(self,step, i,n):
        return random.randint(1024, 4095)
 
    measure_green=caltub.measureOneColorChannel(color="green", insertfunction=fun,
        n=1200,each=1)

    voltages_g=voltages_g+measure_green[0]
    xyY_g=xyY_g+measure_green[1]
    spectra_g=spectra_g+measure_green[2]

    with open('calibdata/measurements/measure_green_channel_' +
            time.strftime("%Y%m%d_%H%M") +  '.txt', 'w') as calibFile:
        calibFile.write("voltage, xyY, spectra\n") # TODO not just with 3 values but with 3 + 3 + 36
        voltages = (voltages_g)
        xyY = (xyY_g)
        spectra = (spectra_g)
        for i in range(len(voltages)):
            calibFile.write(", ".join([str(x) for x in voltages[i]]) +
                            ", " + ", ".join([str(x) for x in
                                xyY[i]]) +
                            ", " + ", ".join([str(x) for x in
                                spectra[i]]) +
                            "\n")
