import os
import numpy as np
import pandas as pd
from tensorflow import keras
from tensorflow.keras.utils import pad_sequences, to_categorical
from tensorflow.keras import layers, callbacks
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# words = [x[0:-3] for x in os.listdir("../data/dataFrames")]
words = [x for x in os.listdir("../data/treatedDF")]
max_frames = 30
word_keypoints = []  # Keypoint sequence for each sample
word_nums = []  # Words represented by numbers

for num, word in enumerate(words):
    df = pd.read_hdf(f"../data/treatedDF/{word}")
    for num_sample in df.n_sample.unique():
        word_keypoints.append([data["keypoints"] for _, data in df[df.n_sample == num_sample].iterrows()])
        word_nums.append(num)

# word_keypoints len is the total number of samples
word_keypoints = pad_sequences(word_keypoints, maxlen=30, padding="post", truncating="post", dtype='float32')
# word_keypoints shape = (355,60) = (total_n_samples,max_frames)

X_train, X_test, y_train, y_test = train_test_split(word_keypoints, word_nums, test_size=0.30)
X_train = np.array(X_train)
y_train = to_categorical(y_train, num_classes=4, dtype="int")
X_test = np.array(X_test)
y_test = to_categorical(y_test, num_classes=4, dtype="int")

early_stoping = callbacks.EarlyStopping(min_delta=0.001,
                                        patience=5,
                                        restore_best_weights=True,
                                        monitor="loss")
model = keras.Sequential(
    [layers.LSTM(64, return_sequences=True, activation="tanh", input_shape=(30, 126)),
     layers.LSTM(128, return_sequences=True, activation="tanh"),
     layers.LSTM(128, return_sequences=False, activation="tanh"),
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
     layers.Dense(32, activation="sigmoid"),
     layers.Dense(32, activation="relu"),
     layers.Dense(4, activation="softmax")]
)
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

history = model.fit(X_train,
                    y_train,
                    epochs=100,
                    validation_data=(X_test, y_test),
                    callbacks=[early_stoping])
history_df = pd.DataFrame(history.history)
history_df.loc[:, ['loss', 'val_loss']].plot()
plt.show()

if not os.path.exists("../data/model/"):
    os.mkdir("../data/model/")
print(model.summary())
model.save("../data/model/GestoLingo.keras")
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
