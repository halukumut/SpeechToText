import json
import tensorflow as tf
import numpy as np
import os
import glob

directory_path = "./data"
def tokenizer_train(tokenizer, data):
    tokenizer.fit_on_texts(data)
    sequences = tokenizer.texts_to_sequences(data)
    padded = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=5)

    return padded, len(tokenizer.word_index)

def tokenize(tokenizer, data):
    tokenized_data = tokenizer.texts_to_sequences(data)
    sequeneces = tf.keras.preprocessing.sequence.pad_sequences(tokenized_data, maxlen=5)

    return sequeneces

def fetch_data(tokenizer, directory_path=directory_path):
    content = []
    column_size = []
    index = -1
    txt_files = glob.glob(os.path.join(directory_path, '*.txt'))

    for txt_file in txt_files:
        line_index = 0
        index += 1
        with open(txt_file, 'r', encoding='utf-8') as file:
            for line in file:
                line_index += 1
                content.append(line.strip())
        column_size.append(line_index)


    padded, word_index = tokenizer_train(tokenizer, content)
    label = 0
    for i in range(3):
        temp_arr = np.zeros((column_size[i],1))
        temp_arr.fill(i)
        if i == 0:
            label = temp_arr
        else:
            label = np.vstack((label, temp_arr))
    reshaped = np.hstack((padded, label))
    reshaped = reshaped.astype('int32')
    return reshaped, word_index + 1, reshaped.shape[1]