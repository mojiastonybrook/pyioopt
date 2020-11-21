import wcsim_reader

import numpy as np
import matplotlib.pyplot as plt

rd = wcsim_reader.Reader()
print("Initialized reader")

#rd.addFile("/disk/cvilela/WCML/TrainingSampleWCSim/e-/0/WCSim/out/WCSim_TrainingSample_e-_0.root")
rd.addFile("/disk/cvilela/WCML/TrainingSampleWCSim/*/*/WCSim/out/*.root")

top = rd.mask[0]
barrel = rd.mask[1]
bottom = rd.mask[2]

print(len(rd))

print(rd.pmts())

for iev, event in enumerate(rd) :
    print("EVENT {0}".format(iev))
    print(event)
    for isub, sub in enumerate(event) :
        print ("SUB-EVENT {0}".format(isub))
        print(sub)
        print (sub["hits"])

        thisTop_q = np.copy(top).astype(float)
        thisTop_t = np.copy(top).astype(float)

        thisBarrel_q = np.copy(barrel).astype(float)
        thisBarrel_t = np.copy(barrel).astype(float)

        thisBottom_q = np.copy(bottom).astype(float)
        thisBottom_t = np.copy(bottom).astype(float)

        for hit in sub["hits"] :
            if rd.pmts()["location"][hit["pmtNumber"]-1] == 0 :
                thisTop_q[rd.pmts()["column"][hit["pmtNumber"]-1], rd.pmts()["row"][hit["pmtNumber"]-1]] = hit['q']
                thisTop_t[rd.pmts()["column"][hit["pmtNumber"]-1], rd.pmts()["row"][hit["pmtNumber"]-1]] = hit['t']
            elif rd.pmts()["location"][hit["pmtNumber"]-1] == 1 :
                thisBarrel_q[rd.pmts()["column"][hit["pmtNumber"]-1], rd.pmts()["row"][hit["pmtNumber"]-1]] = hit['q']
                thisBarrel_t[rd.pmts()["column"][hit["pmtNumber"]-1], rd.pmts()["row"][hit["pmtNumber"]-1]] = hit['t']
            elif rd.pmts()["location"][hit["pmtNumber"]-1] == 2 :
                thisBottom_q[rd.pmts()["column"][hit["pmtNumber"]-1], rd.pmts()["row"][hit["pmtNumber"]-1]] = hit['q']
                thisBottom_t[rd.pmts()["column"][hit["pmtNumber"]-1], rd.pmts()["row"][hit["pmtNumber"]-1]] = hit['t']
        plt.figure()
        plt.imshow(thisTop_q)
        plt.figure()
        plt.imshow(thisTop_t)
        plt.figure()
        plt.imshow(thisBarrel_q)
        plt.figure()
        plt.imshow(thisBarrel_t)
        plt.figure()
        plt.imshow(thisBottom_q)
        plt.figure()
        plt.imshow(thisBottom_t)
        plt.show()

        del thisTop_q, thisTop_t, thisBarrel_q, thisBarrel_t, thisBottom_q, thisBottom_t
