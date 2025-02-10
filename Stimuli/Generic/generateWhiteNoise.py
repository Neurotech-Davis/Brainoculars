# This file generates the sequences of modulated white noise that will be loaded in the actual experiments
# Do NOT re-generate the noise unless absolutely necessary since all of the trials need to use the SAME sequence of noise for the cVEPs to work!!!

import numpy as np

frameRate = 60 # Framerate of experiment
length = 1 # Length of noise (seconds)
numSegments = 8 # Number of sequences to generate

def generateWhiteNoise():
    return np.random.rand(frameRate * length, 1)

def generateAllNoise():
    return [generateWhiteNoise() for _ in range(numSegments)]
    
noise = generateAllNoise()
np.save("noiseSequences.npy", noise)