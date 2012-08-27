from stimuliclass import Mondrian
import numpy as np
import Image
import time
import eizoGS320
import sys

sys.path.append("../achrolabutils/")
k=0
stimulilist=[(376, 456), (396, 476), (416, 496), (436, 516), (456, 536), (436, 476), (396, 516)]
timeset=time.strftime("%Y%m%d_%H%M", time.localtime())
fileoutac=open("stimulilistac"+str(timeset)+".txt", "w")
fileoutnc=open("stimulilistnc"+str(timeset)+".txt", "w")
i=0
j=0
while k<len(stimulilist):
    while j<len(stimulilist):
        monitorsize=[2048, 1536]
        # mondheight=monitorsize[1]/2.0
        # mondwidth=monitorsize[0]/4.0
        bggray=621
        separation=40
        infieldsize=80
        surroundsize=454
        mondrianlength=40

        leftweightsvar=10
        #leftweightsmean=512+k
        leftweightsmean=stimulilist[k][1]
        rightweightsvar=10
        #rightweightsmean=512+k
        rightweightsmean=stimulilist[j][1]

        leftpatchgray=stimulilist[k][0]
        rightpatchgray=stimulilist[j][0]

        leftgrayminus=stimulilist[k][1]-stimulilist[k][0]
        rightgrayminus=stimulilist[j][1]-stimulilist[j][0]

        seedleft=1
        seedright=1

        leftweights=[]
        for i in range(1023):
            leftweights.append(((1.0/(leftweightsvar * np.sqrt(2*np.pi))) * np.exp(-0.5*(((i-leftweightsmean)/leftweightsvar)**2))))

        rightweights=[]
        for i in range(1023):
            rightweights.append(((1.0/(rightweightsvar * np.sqrt(2*np.pi))) * np.exp(-0.5*(((i-rightweightsmean)/rightweightsvar)**2))))


        rightweights=rightweights/sum(rightweights)
        leftweights=leftweights/sum(leftweights)

        bigarray=np.ones((monitorsize[1], monitorsize[0]))
        bigarray=bggray*bigarray

        #Draw Mondrian surrounds
        mymondleft=Mondrian(usingeizo=False, imagesize=[surroundsize, surroundsize], meanlength=mondrianlength, encode=False, weights=leftweights, saveimage=False, seed=seedleft)

        bigarray[(monitorsize[1]/2.0)-surroundsize/2.0:(monitorsize[1]/2.0)+surroundsize/2.0,(monitorsize[0]/2.0)-surroundsize-separation/2.0:(monitorsize[0]/2.0)-separation/2.0] = mymondleft.mondrianarray

        mymondright=Mondrian(usingeizo=False, imagesize=[surroundsize, surroundsize],  meanlength=mondrianlength, encode=False, weights=rightweights, saveimage=False, seed=seedright)

        bigarray[(monitorsize[1]/2.0)-surroundsize/2.0:(monitorsize[1]/2.0)+surroundsize/2.0,(monitorsize[0]/2.0)+separation/2.0:(monitorsize[0]/2.0)+surroundsize+separation/2.0] = mymondright.mondrianarray

        #Overlay transparent insets
        bigarray[(monitorsize[1]/2.0)-(infieldsize/2.0):(monitorsize[1]/2.0)+(infieldsize/2.0),(monitorsize[0]/2.0)-(surroundsize/2.0)-(separation/2.0)-(infieldsize/2.0):(monitorsize[0]/2.0)-(separation/2.0)-(surroundsize/2.0)+(infieldsize/2.0)] -= leftgrayminus
        bigarray[(monitorsize[1]/2.0)-(infieldsize/2.0):(monitorsize[1]/2.0)+(infieldsize/2.0),(monitorsize[0]/2.0)+(separation/2.0)+(surroundsize/2.0)-(infieldsize/2.0):(monitorsize[0]/2.0)+(surroundsize/2.0)+(separation/2.0)+(infieldsize/2.0)] -= leftgrayminus

        bigarray[bigarray>1023]=1023
        bigarray[bigarray<0]=0

        # (N, M) = np.shape(bigarray)
        # newarray = np.zeros((N, M, 3), dtype=np.uint8)
        # newarray[:,:,0]=np.uint8(bigarray[:,:]/4)
        # newarray[:,:,1]=np.uint8(bigarray[:,:]/4)
        # newarray[:,:,2]=np.uint8(bigarray[:,:]/4)
        newarray=eizoGS320.encode_np_array(bigarray)
        pil_im = Image.fromarray(newarray)
        pngfile="stimuli/ac"+str(leftweightsmean)+"_"+str(leftweightsvar)+"_"+str(leftgrayminus)+"_"+str(rightweightsmean)+"_"+str(rightweightsvar)+"_"+str(rightgrayminus)+"_"+str(bggray)+"_"+str(seedleft)+"_"+str(seedright)+".png"

        fileoutac.write("trial(['"+str(pngfile)+"', "+str(leftweightsmean)+","+str(leftweightsvar)+","+str(leftgrayminus)+","+str(rightweightsmean)+","+str(rightweightsvar)+","+str(rightgrayminus)+","+str(bggray)+","+str(seedleft)+","+str(seedright)+"], 'left', outputFile)\n")
        pil_im.save(pngfile)

        #do NC image
        bigarray[(monitorsize[1]/2.0)-(infieldsize/2.0):(monitorsize[1]/2.0)+(infieldsize/2.0),(monitorsize[0]/2.0)-(surroundsize/2.0)-(separation/2.0)-(infieldsize/2.0):(monitorsize[0]/2.0)-(separation/2.0)-(surroundsize/2.0)+(infieldsize/2.0)] = leftpatchgray
        bigarray[(monitorsize[1]/2.0)-(infieldsize/2.0):(monitorsize[1]/2.0)+(infieldsize/2.0),(monitorsize[0]/2.0)+(separation/2.0)+(surroundsize/2.0)-(infieldsize/2.0):(monitorsize[0]/2.0)+(surroundsize/2.0)+(separation/2.0)+(infieldsize/2.0)] = rightpatchgray

        bigarray[bigarray>1023]=1023
        bigarray[bigarray<0]=0

        # (N, M) = np.shape(bigarray)
        # newarray = np.zeros((N, M, 3), dtype=np.uint8)
        # newarray[:,:,0]=np.uint8(bigarray[:,:]/4)
        # newarray[:,:,1]=np.uint8(bigarray[:,:]/4)
        # newarray[:,:,2]=np.uint8(bigarray[:,:]/4)
        newarray=eizoGS320.encode_np_array(bigarray)
        pil_im = Image.fromarray(newarray)
        pngfile="stimuli/nc"+str(leftweightsmean)+"_"+str(leftweightsvar)+"_"+str(leftgrayminus)+"_"+str(rightweightsmean)+"_"+str(rightweightsvar)+"_"+str(rightgrayminus)+"_"+str(bggray)+"_"+str(seedleft)+"_"+str(seedright)+".png"

        fileoutnc.write("trial(['"+str(pngfile)+"', "+str(leftweightsmean)+","+str(leftweightsvar)+","+str(leftgrayminus)+","+str(rightweightsmean)+","+str(rightweightsvar)+","+str(rightgrayminus)+","+str(bggray)+","+str(seedleft)+","+str(seedright)+"], 'left', outputFile)\n")
        pil_im.save(pngfile)

        j+=1
    k+=1
    j=0

fileoutac.close()
fileoutnc.close()
