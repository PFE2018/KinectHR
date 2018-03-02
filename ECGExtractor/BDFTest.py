from pybdf import bdfRecording
import pandas as pd
import numpy as np
from matplotlib import pyplot
from biosppy import ecg

bdfRec = bdfRecording("../Dataset/Sessions/789/Part_7_N_Trial5_emotion.bdf")
ECG_idx = bdfRec.dataChanLabels.index('EXG2')
rec = bdfRec.getData()
sampling_rate = bdfRec.sampRate[ECG_idx]
signal = np.array(rec['data'][ECG_idx,:])
rec_s = pd.Series(rec['data'][ECG_idx,:])
rec_s.plot()
pyplot.pause(0.1)
hr = ecg.ecg(signal=signal, sampling_rate=sampling_rate, show=True)[6]


print('noice')
