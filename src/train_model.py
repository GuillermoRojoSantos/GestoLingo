import os
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras

words = [x[0:-3] for x in os.listdir("data/dataFrames")]
max_frames = 50

for word in words:
    pass