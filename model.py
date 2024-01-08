'''
LSTM Encoder-Decoder Model that trains on language pairs, using keras
deep-learning.
'''


import csv
from pickle import dump, load

from keras.callbacks import ModelCheckpoint
from keras.layers import LSTM, Dense, Embedding, RepeatVector, TimeDistributed
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.utils.vis_utils import plot_model
from numpy import array
from numpy.random import rand, shuffle


# load a clean dataset
def load_clean_sentences(filename):
    return load(open(filename, 'rb'))

# save a list of clean sentences to file
def save_clean_data(sentences, filename):
    dump(sentences, open(filename, 'wb'))
    print('Saved: %s' % filename)


# load dataset
raw_dataset = load_clean_sentences('ita.pkl')

# reduce dataset size
n_sentences = 10000
training_split = n_sentences * 0.9
dataset = raw_dataset[:n_sentences, :]
# random shuffle
shuffle(dataset)
# split into train/test
train, test = dataset[:training_split], dataset[training_split:]
# save
save_clean_data(dataset, 'ita-shuffled.pkl')
save_clean_data(train, 'ita-train.pkl')
save_clean_data(test, 'ita-test.pkl')