from collections import Counter
import pandas as pd
import numpy as np
import nltk

from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsOneClassifier, OneVsRestClassifier
from sklearn.model_selection import cross_val_score


def split(text): return nltk.tokenize.word_tokenize(text)


def get_data():
    emails = pd.read_csv('csv/emails.csv')
    lines = emails['email'].str.lower()
    classification = emails['classificacao']

    texts = []
    for t in lines:
        t_list = split(t)
        t_valid = filter(lambda w: len(w) > 2 and w not in stop_words, t_list)
        t_root = map(lambda w: stemmer.stem(w), t_valid)
        texts.append(list(t_root))

    setEmail = set()
    for lst_t in texts:
        setEmail.update(lst_t)

    totalWords = len(setEmail)

    lst = zip(setEmail, range(totalWords))
    dic = {word: index for word, index in lst}

    return texts, dic, classification


def get_vector_base(num):
    return num * [0]


def vector_text_in_dic(text, dic):
    num = len(dic)
    vector_base = get_vector_base(num)
    for t in text:
        if t in dic.keys():
            vector_base[dic[t]] += 1
    return vector_base


def fit_predict_score(model, data_fit, marked_fit, k):
    name = type(model).__name__
    score = np.mean(cross_val_score(model, data_fit, marked_fit, cv=k)) * 100
    print('Score of "{}" Algorithm is {}.'.format(name, score))
    return score


def fit_predict(model, data_fit, marked_fit, data_test, marked_test):
    model.fit(data_fit, marked_fit)
    predict = model.predict(data_test)
    hits = sum(predict == marked_test)
    return hits / len(marked_test) * 100


#
stemmer = nltk.stem.RSLPStemmer()
stop_words = nltk.corpus.stopwords.words('portuguese')

# configuration
texts, dic, classification = get_data()

# all registers
vectors = [vector_text_in_dic(text, dic) for text in texts]

# constants
porc_fit = 0.8
k = 10
len_vectors = len(vectors)
len_fit = int(len_vectors * porc_fit)

# variables
vectors_fit = vectors[:len_fit]
vectors_test = vectors[-len_fit:]

classification_fit = classification[:len_fit]
classification_test = classification[-len_fit:]

# algorithms
nb = MultinomialNB()
ada = AdaBoostClassifier()
one_one = OneVsOneClassifier(LinearSVC(random_state=0))
one_rest = OneVsRestClassifier(LinearSVC(random_state=0))

dumb_value = max(Counter(classification_test).values())
print('Score of "dumb" Algorithm is {}.'.format(
    dumb_value / len(classification_test) * 100))

dic_score = {
    fit_predict_score(nb, vectors_fit, classification_fit, k): nb,
    fit_predict_score(ada, vectors_fit, classification_fit, k): ada,
    fit_predict_score(one_one, vectors_fit, classification_fit, k): one_one,
    fit_predict_score(one_rest, vectors_fit, classification_fit, k): one_rest
}

winer_algorithm = dic_score[max(dic_score)]
name = type(winer_algorithm).__name__
score = fit_predict(winer_algorithm, vectors_fit,
                    classification_fit, vectors_test, classification_test)

print('Algorithm "{}" is Winer, score real world is {}.'.format(name, score))
