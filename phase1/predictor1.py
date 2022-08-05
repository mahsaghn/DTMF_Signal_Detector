from scipy.io import wavfile as wav
from DTMF1 import DTMF
import numpy as np
import os


def save_as_csv(results):
    with open("Results1.csv", "w") as resFile:
        resFile.write("Id,Predicted\n")
        for sample in results:
            resFile.write("{},'{}'\n".format(sample[0], "".join(sample[1])))

results = []
for sample in os.listdir('Phase1-Unlabeled'):
    rate, data = wav.read(os.path.join('Phase1-Unlabeled', sample))
    sample = sample.split('.')[0]
    if len(data.T.shape) > 1:
        data = data.T[0]  # Extracting the main channel of the sound
    result = DTMF(data, rate)
    results.append((sample, result))


save_as_csv(results)