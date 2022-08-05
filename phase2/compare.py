import os
from scipy.io import wavfile as wav
from Levenshtein import distance as levenshtein_distance
from termcolor import colored

from DTMF2 import DTMF

predict_file1 = 'Results2.csv'
# predict_file2 = 'Results23.csv'
# predict_file3 = 'Results22.csv'
predict_f1 = open(predict_file1)
# predict_f2 = open(predict_file2)
# predict_f3 = open(predict_file3)
correct1 = predict_f1.readlines()[1:]
# correct2 = predict_f2.readlines()[1:]
# correct3 = predict_f3.readlines()[1:]
for i in range(len(correct1)):
        print(correct1[i].split(',')[0])
        print(correct1[i].split(',')[1])
        # print(correct2[i].split(',')[1])
        # print(correct3[i].split(',')[1])
        # print("__________")
#         if correct[i]!=correct[-1]:
#                 correct[i] = correct[i][:-1]
#         correct[i] = correct[i].split(',')
#         correct[i][0] = int(correct[i][0])
# correct_f.close()
# loss = 0
# count = 0
# all_point = 0
# for sound_file in sound_files:
#         rate, data = wav.read(os.path.join(sound_path, sound_file))
#         result = str("'")+DTMF(data, rate)+str("'")
#         (file, ext) = os.path.splitext(sound_file)
#         file = int(file)
#         correct_result = correct[file-1][1]
#         if len(result) != len(correct_result):
#                 print(colored(sound_file, 'red'),'\n',result,'-->',len(result)-2,'\n',correct_result,'-->',len(correct_result)-2,'\n')
#         else:
#                 print(sound_file,'\n',result,'-->',len(result)-2,'\n',correct_result,'-->',len(correct_result)-2,'\n')
#         # print(levenshtein_distance(result, correct_result))
#         if result == correct_result:
#                 count+=1
#         loss += levenshtein_distance(result, correct_result)
# print(len(correct))
# a = ''
# for i in correct:
#         # print(i)
#         a +=i[1]

# print('your loss is:',loss/len(correct))

