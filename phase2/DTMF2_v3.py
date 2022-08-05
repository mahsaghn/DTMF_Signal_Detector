from scipy.io import wavfile as wav
from scipy import fft
import numpy as np
from matplotlib import pyplot as plt
import os
import soundfile as sf
import math
from scipy import signal

def find_key(lowerBound,amp_freqs,prevkey):
    row_freqs = {
        4:{0:'1',1:'4',2:'7',3:'*'},
        5:{0:'2',1:'5',2:'8',3:'0'},
        6:{0:'3',1:'6',2:'9',3:'#'},
        7:{0:'A',1:'B',2:'C',3:'D'} 
    }
    keies = []
    # print (amp_freqs)
    max1v = max(amp_freqs[:4])
    max1 = amp_freqs.index(max1v)
    max2v = max(amp_freqs[4:])
    max2 = amp_freqs.index(max2v)
    key = ''
    # lowfreq = 10 * np.log10(max1v)
    # highfreq = 10 * np.log10(max2v)
    if max1v>30 and max2v>30:
    # print(lowfreq,highfreq)
        # print(max1v,max2v)
        # print("max1,max2",10*np.log(max1v*max1v),10*np.log(max2v*max2v))
        key = row_freqs[max2][max1]
    return key


def find_freq(signal,rate):
    X = fft.fft(signal)/len(signal)
    freqs = fft.fftfreq(len(signal))*rate
    X = np.abs(X)
    freqs = freqs.astype(int)

    range_freqs = []
    def get_freq(freq):
        befor = np.argmin(abs(freqs - freq))
        if freq < befor:
            before = befor -1
        range_freqs.append(befor)
        Xf.append(max(X[befor],X[befor+1]))

    Xf = []
    get_freq(697)
    get_freq(770)
    get_freq(852)
    get_freq(941)
    get_freq(1209)
    get_freq(1336)
    get_freq(1477)
    get_freq(1633)


    range_freqs = np.array(range_freqs)
    lowerBound = (np.average(X)-(np.max(X)/len(X)))*18
    # print(Xf)
    # print(max(signal))
    # print(np.average(X))
    key = find_key(lowerBound,Xf,'')
    # print('_________________',key)
    return key


def DTMF(signal, rate):
    # signal, rate = sf.read('12.wav')
    # print(rate)
    x=  np.linspace(0,len(signal)-1,len(signal))
    # X = fft.fft(signal)/len(signal)
    # freqs = fft.fftfreq(len(signal))*rate
    # X = np.abs(X)       
    # freqs = freqs.astype(int)
    # plt.plot(x,signal)
    # plt.show()
    # print(rate)
    num_subsignal = int(len(signal)/(rate*0.11))
    # print(num_subsignal)
    subsignals = np.array_split(signal,num_subsignal)
    keies = ''
    pp =''
    prevkey = ''
    for subsignal in subsignals:
        key =find_freq(subsignal,rate)
        # print(len(subsignal))
        # print(key)
        if (key=='' and prevkey!='' and pp==''):
            keies+= prevkey
        elif (key==prevkey and pp != key):
            keies+=key
        pp = prevkey
        prevkey = key
    # print(keies)
    return keies


# DTMF(1,2)