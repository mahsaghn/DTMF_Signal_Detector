from scipy.io import wavfile as wav
from scipy import fft
import numpy as np
from matplotlib import pyplot as plt
import os
import soundfile as sf
import math

def find_key(signal,key_freqs):
	row_freqs = {
		697:{1209:'1',1336:'2',1477:'3',1633:'A'},
		770:{1209:'4',1336:'5',1477:'6',1633:'B'},
		852:{1209:'7',1336:'8',1477:'9',1633:'C'},
		941:{1209:'*',1336:'0',1477:'#',1633:'D'} 
	}
	keies = []
	key_freqs = sorted(key_freqs,key=lambda l:l[1], reverse=True)
	for row_freq in key_freqs:
		if row_freq[0] in row_freqs and  row_freq[1]!=0:
			col_freqs = row_freqs[row_freq[0]]
			for  col_freq in key_freqs:
				if col_freq[0] in col_freqs and col_freq[1]!=0:
					keies.append([col_freqs[col_freq[0]],row_freq[1],col_freq[1]])
	try:
		maxki = keies[0]
		for m in keies:
			if m[1]*m[2]>maxki[1]*maxki[2]:
				maxki = m 
		return maxki[0]
	except:
		return ''


def find_freq(signal,rate):
	step = rate/len(signal)
	X = fft.fft(signal)
	freqs = fft.fftfreq(len(signal))*rate
	X = np.abs(X)
	freqs = freqs.astype(int)

	key_freqs = []
	def get_freq(freq):
		befor = freq - freq%step
		befor = np.where(freqs==befor)[0][0]
		after = befor + 1
		val = max(X[after] , X[befor])
		if val >= LowerBound :
			key_freqs.append([freq,val/1000])
		else : 
			key_freqs.append([freq,0])



                
	LowerBound =15*np.average(X)
	get_freq(697)
	get_freq(770)
	get_freq(852)
	get_freq(941)
	get_freq(1209)
	get_freq(1336)
	get_freq(1477)
	get_freq(1633)
	# plt.plot(freqs,X)
	# plt.show()
	return key_freqs
			

def DTMF(signal, rate):
	print(len(signal),rate,len(signal)/rate)
	# signal, rate = sf.read('33.wav')
	# print('\n',len(signal),rate)
	lis =find_freq(signal,rate)
	key = find_key(signal,lis)
	# print(key)
	return key  # An example of your final result. it means you have found no key!

# DTMF(1,2)