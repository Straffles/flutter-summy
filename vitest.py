import nltk
import numpy as np
from gensim.models.keyedvectors import KeyedVectors
from pyvi import ViTokenizer
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
import fasttext
import fasttext.util

w2v = KeyedVectors.load_word2vec_format('C:\\Users\\Admin\\Documents\\WeTech\\back-end\\baomoi.model.bin', binary=True)
vocab = w2v.vocab

n_clusters = 5
kmeans = KMeans(n_clusters=n_clusters)

def summary(content):

        contents_parsed = content.lower()
        contents_parsed = contents_parsed.replace('\n', '. ')
        contents_parsed = contents_parsed.strip()

        sentences = nltk.sent_tokenize(contents_parsed)

        X = []
        for sentence in sentences:
            sentence_tokenized = ViTokenizer.tokenize(sentence)
            words = sentence_tokenized.split(" ")
            sentence_vec = np.zeros((400))
            for word in words:
                if word in vocab:
                    sentence_vec = sentence_vec + w2v[word]
            X.append(sentence_vec)


        _kmeans = kmeans.fit(X)


        avg = []
        for j in range(n_clusters):
            idx = np.where(_kmeans.labels_ == j)[0]
            avg.append(np.mean(idx))
        closest, _ = pairwise_distances_argmin_min(_kmeans.cluster_centers_, X)
        ordering = sorted(range(n_clusters), key=lambda k: avg[k])
        summary = ' '.join([sentences[closest[idx]] for idx in ordering])

        return summary