# -*- coding: utf-8 -*-
# @Time    : 2019/8/31 21:47
# @Author  : Solinari
# @Email   : deeper1@163.com
# @File    : rnn.py
# @Software: PyCharm

import torch.nn as nn
import torch
from torch.autograd import Variable
import torch.nn.functional as F

import numpy as np


def weights_init(m):
    """

    :param m:
    :return:
    """
    classname = m.__class__.__name__  # obtain the class name
    if classname.find('Linear') != -1:
        weight_shape = list(m.weight.data.size())
        fan_in = weight_shape[1]
        fan_out = weight_shape[0]
        w_bound = np.sqrt(6. / (fan_in + fan_out))
        m.weight.data.uniform_(-w_bound, w_bound)
        m.bias.data.fill_(0)
        print("inital  linear weight ")


class word_embedding(nn.Module):
    """
    word embedding: map a high-dimension space of all words to a low-dimension vector space
    each word map into a vecotr in the space
    """
    def __init__(self, vocab_length, embedding_dim):
        super(word_embedding, self).__init__()
        w_embeding_random_intial = np.random.uniform(
            -1, 1, size=(vocab_length, embedding_dim))
        self.word_embedding = nn.Embedding(vocab_length, embedding_dim)
        self.word_embedding.weight.data.copy_(
            torch.from_numpy(w_embeding_random_intial))

    def forward(self, input_sentence):
        """
        :param input_sentence:  a tensor ,contain several word index.
        :return: a tensor ,contain word embedding tensor
        """
        sen_embed = self.word_embedding(input_sentence)
        return sen_embed


class RNN_model(nn.Module):
    """

    """
    def __init__(self, batch_sz, vocab_len, word_embedding, embedding_dim, lstm_hidden_dim):
        """
        @param batch_sz: batch size
        @param vocab_len vocaboary length
        @param word_embedding: word embedding function
        @param lstm_hideen_dim:
        """
        super(RNN_model,self).__init__()
        
        # print (batch_sz)    # 10
        # print (vocab_len)   # 61
        # print (embedding_dim)   # 100
        # print (lstm_hidden_dim) # 128
        self.word_embedding_lookup = word_embedding
        self.batch_size = batch_sz
        self.vocab_length = vocab_len
        self.word_embedding_dim = embedding_dim
        self.lstm_dim = lstm_hidden_dim
        #########################################
        # here you need to define the "self.rnn_lstm"  the input size is "embedding_dim" and the output size is "lstm_hidden_dim"
        # the lstm should have two layers, and the  input and output tensors are provided as (batch, seq, feature)
        # ???
        self.rnn_lstm = nn.LSTM(self.word_embedding_dim, self.lstm_dim)   # (input_size,hidden_size,num_layers)

        ##########################################
        self.fc = nn.Linear(lstm_hidden_dim, vocab_len)
        self.apply(weights_init)  # call the weights initial function.

        self.softmax = nn.LogSoftmax()  # the activation function.
        # self.tanh = nn.Tanh()

    def forward(self, sentence, is_test= False):
        batch_input = self.word_embedding_lookup(
            sentence).view(1, -1, self.word_embedding_dim)
        # print(batch_input.size()) # print the size of the input # size 1, 7, 100
        ################################################
        # here you need to put the "batch_input"  input the self.lstm which is defined before.
        # the hidden output should be named as output, the initial hidden state and cell state set to zero.
        # ???

        ################################################
        output = self.rnn_lstm(batch_input)
        # print (output)
        print (type(output))

        out = output.contiguous().view(-1, self.lstm_dim)

        out = F.relu(self.fc(out))

        out = self.softmax(out)

        if is_test:
            prediction = out[-1, :].view(1, -1)
            output = prediction
        else:
            output = out
        # print(out)
        return output
