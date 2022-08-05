import alsaaudio, time, audioop
import sys
import struct
from scipy.io import wavfile as wav
from scipy import fft
import numpy as np
from matplotlib import pyplot as plt
import os
import soundfile as sf
import math
from scipy import signal

def find_key(amp_freqs):
	row_freqs = {
		4:{0:'1',1:'4',2:'7',3:'*'},
		5:{0:'2',1:'5',2:'8',3:'0'},
		6:{0:'3',1:'6',2:'9',3:'#'},
		7:{0:'A',1:'B',2:'C',3:'D'} 
	}
	amp_freqs = amp_freqs
	max1v = max(amp_freqs[:4])
	max1 = np.where(amp_freqs[:4] == max1v)[0][0]
	max2v = max(amp_freqs[4:])
	max2 = np.where(amp_freqs[4:] == max2v)[0][0]+4
	# lowerBound = lowerBound * 18
	if max1v>0.005 and max2v>0.005:
		# print(amp_freqs)
		# print ("{:.4f}".format(max1v),"{:.4f}".format(max2v))
		return row_freqs[max2][max1]
	return ''


def find_freq(signal,rate):
    X = fft.fft(signal)/len(signal)
    freqs = fft.fftfreq(len(signal))*rate
    X = np.abs(X)
    freqs = freqs.astype(int)

    def get_freq(freq):
        befor = np.argmin(abs(freqs - freq))
        if freq < befor:
            before = befor -1
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
    Xf = np.array(Xf)
    key = find_key(Xf)

    return key

inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)

inp.setchannels(1)
inp.setrate(8000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)

inp.setperiodsize(660)
keies = ''
pp =''
prevkey = ''
rate = 8000
while 1:
	l,signal = inp.read()
	if l:
		b = '<	'+ 'H'*int(len(signal)/2)
		signal = np.array(struct.unpack(b,signal))
		signal = signal*6 / (100 * max(signal))
		signal = signal.astype(float)
		key =find_freq(signal,rate)
		if (key=='' and prevkey!='' and pp==''):
			print(prevkey)
			# print('_________________________',prevkey)
		elif (key==prevkey and pp != key and key!=''):
			print(key)
			# print('_________________________',key)
		# if key !='':
		# 	print(key)
		pp = prevkey
		prevkey = key
	time.sleep(460/8000)	
