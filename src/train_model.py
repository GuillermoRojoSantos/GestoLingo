import os
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.utils import pad_sequences, to_categorical
from tensorflow.keras import layers, callbacks
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
import joblib

# words = [x[0:-3] for x in os.listdir("../data/dataFrames")]
words = [x for x in os.listdir("../data/treatedDF")]
max_frames = 60
word_keypoints = []  # Keypoint sequence for each sample
word_nums = []  # Words represented by numbers

for num, word in enumerate(words):
    df = pd.read_hdf(f"../data/treatedDF/{word}")
    for num_sample in df.n_sample.unique():
        word_keypoints.append([data["keypoints"] for _, data in df[df.n_sample == num_sample].iterrows()])
        word_nums.append(num)

# word_keypoints len is the total number of samples
word_keypoints = pad_sequences(word_keypoints, maxlen=max_frames, padding="post", truncating="post", dtype='float32')
# word_keypoints shape = (355,60) = (total_n_samples,max_frames)

y_train, X_train = shuffle(word_nums, word_keypoints)
X_train = np.array(X_train)
y_train = to_categorical(y_train, num_classes=4, dtype="int")

early_stoping = callbacks.EarlyStopping(min_delta=0.001,
                                        patience=5,
                                        restore_best_weights=True,
                                        monitor="loss")
model = keras.Sequential(
    [layers.LSTM(64, return_sequences=True, activation="relu", input_shape=(60, 126)),
     layers.LSTM(128, return_sequences=True, activation="relu"),
     layers.LSTM(128, return_sequences=False, activation="relu"),
     # Use tanh with Nvidia (enabled cudnn) for faster processing
     # layers.LSTM(64, return_sequences=True, activation="tanh", input_shape=(60, 126)),
     # layers.LSTM(128, return_sequences=True, activation="tanh"),
     # layers.LSTM(128, return_sequences=False, activation="tanh"),
     layers.BatchNormalization(),
     layers.Dense(70, activation="sigmoid"),
     layers.Dropout(0.2),
     layers.Dense(70, activation="relu"),
     layers.Dense(70, activation="relu"),
     layers.Dropout(0.2),
     layers.Dense(70, activation="relu"),
     layers.Dense(70, activation="relu"),
     layers.Dropout(0.2),
     layers.Dense(64, activation="relu"),
     layers.Dense(64, activation="relu"),
     layers.BatchNormalization(),
     layers.Dropout(0.2),
     layers.Dense(32, activation="relu"),
     layers.Dense(32, activation="relu"),
     layers.Dense(4, activation="softmax")]
)
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

history = model.fit(X_train, y_train, epochs=100, callbacks=[early_stoping])
history_df = pd.DataFrame(history.history)
history_df.loc[:, ['loss']].plot()
plt.show()

if not os.path.exists("../data/model/"):
    os.mkdir("../data/model/")
joblib.dump(model, "../data/model/GestoLingo.pkl")

# # Uncomment bellow prints if you need clarification of the structure of word_keypoints
# # print(word_keypoints[0][0])
# # print(word_keypoints[21][-1])
# # print(len(word_keypoints[0]))
# # print(len(word_keypoints))
# # print(len(word_keypoints[0][0]))
# # print(word_nums)
# # print(len(word_keypoints))
# # print(len(word_nums))

# acceptable model:
# model = keras.Sequential(
#     [layers.LSTM(64, return_sequences=True, activation="relu", input_shape=(60, 126)),
#     layers.LSTM(128, return_sequences=True, activation="relu"),
#     layers.LSTM(128, return_sequences=False, activation="relu"),
#     layers.Dense(64, activation="relu"),
#     layers.Dropout(0.2),
#     layers.Dense(64, activation="relu"),
#     layers.Dense(64, activation="relu"),
#     layers.Dropout(0.2),
#     layers.Dense(64, activation="relu"),
#     layers.Dense(64, activation="relu"),
#     layers.Dropout(0.2),
#     layers.Dense(32, activation="relu"),
#     layers.Dense(32, activation="relu"),
#     layers.Dense(4,activation="softmax")]
# )

# am_2:
# model = keras.Sequential(
#     [layers.LSTM(64, return_sequences=True, activation="tanh", input_shape=(60, 126)),
#     layers.LSTM(128, return_sequences=True, activation="tanh"),
#     layers.LSTM(128, return_sequences=False, activation="tanh"),
#     layers.Dense(64, activation="relu"),
#     layers.Dropout(0.2),
#     layers.Dense(64, activation="relu"),
#     layers.Dense(64, activation="relu"),
#     layers.Dropout(0.2),
#     layers.Dense(64, activation="relu"),
#     layers.Dense(64, activation="relu"),
#     layers.Dropout(0.2),
#     layers.Dense(32, activation="relu"),
#     layers.Dense(32, activation="relu"),
#     layers.Dense(4,activation="softmax")]
# )
