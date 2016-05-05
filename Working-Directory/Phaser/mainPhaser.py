"""
Filename: mainPhaser.py

See README.md

Developed under the Apache License 2.0
"""
#______________________________________________________________________________
#Header Imports
import array
import contextlib
import wave
import matplotlib.pyplot as plt
import numpy as np
import math
import copy
import sys
import scipy.signal as ss 

sys.path.append('../Utilities')
import utilities as ut

#______________________________________________________________________________
#Start mainPhaser.py

# Global parameters
dirIn = "../../Original-Audio-Samples/"
dirOut = "../../Output-Audio-Samples/Phaser/"

numChannels = 1                      # mono
sampleWidth = 2                      # in bytes, a 16-bit short
sampleRate = 44100


#______________________________________________________________________________
        
def phaser(signal, ratio = .5, trim = False):

    signal = [int(x) for x in signal]

    if trim:
        signal = signal[:441000]    
    length = len(signal)
    print(len(signal))
    
    signal1 = [int(ratio*x) for x in signal]
    signal2 = [(1-ratio)*x for x in signal]
        
    signal2_np = np.array(signal2)    
    
    
    
    signal2_modified_np = np.imag(ss.hilbert(signal2_np))        

    signal2_modified_list = np.ndarray.tolist(signal2_modified_np)

#    signal2_modified_list = [int(x.imag) for x in signal2_modified_list]
    signal2_modified_list = [int(x) for x in signal2_modified_list]
         
         
         
         
         
    outputSignal = [int(signal1[i] + signal2_modified_list[i]) for i in range(length)]
    print(len(outputSignal)) 
    return outputSignal 



def phaserDemo():
    
     obama       = ut.readWaveFile(dirIn+"ObamaAcceptanceSpeech.wav")
     obamaPhaser = phaser(obama)
     ut.writeWaveFile(dirOut + "Obama_Phaser.wav", obamaPhaser)

     jfk       = ut.readWaveFile(dirIn+"jfk.wav")
     jfkPhaser = phaser(jfk)
     ut.writeWaveFile(dirOut + "JFK_Phaser.wav", jfkPhaser)

     piano       = ut.readWaveFile(dirIn+"piano.wav")
     pianoPhaser = phaser(piano)
     ut.writeWaveFile(dirOut + "Piano_Phaser.wav", pianoPhaser)
    
     print("Phaser Demo Complete.")


phaserDemo()
        
        
        
        