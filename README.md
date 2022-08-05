# DTMF Signal Decoder
detect key pressed by signal analysis
this project has 3 phase:

1. **One key detection on a recorded signal**
    
    At this phase, frequencies in each audio file are extracted. The domain of each frequency is calculated. Finally, due to DTMF table, the correct key will be detected. 
    
2. **Pressed keys detection on a recorded signal**: 

    In this phase, an audio file is partitioned into 0.11 sec periods. Then the same algorithm as the previous method will be applied to each time stamp. There may be some consequent time stamp containing the same key; this does not indicate any new key. Furthermore, between each successive key, there should be at least one other key or empty.
    
    For more details see [here](https://github.com/mahsaghn/DTMF_Signal_Detector/blob/master/phase2/phase2_fa.pdf).

3. **Realtime pressed keys detection**:
    
    For more details see [here](https://github.com/mahsaghn/DTMF_Signal_Detector/blob/master/phase3/DTMF_phase3.pdf).
