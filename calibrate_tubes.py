from achrolab.eyeone.eyeone import EyeOne
from achrolab.calibtubes import CalibTubes

eyeone = EyeOne()
caltub = CalibTubes(eyeone)
caltub.calibrate(imi=0.5, n=500, each=5)
caltub.saveParameter("tube_calibration_75_absorption.pkl")

