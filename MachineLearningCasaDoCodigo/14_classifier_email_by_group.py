import pandas as pd
import numpy as np
import nltk
import random

from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.multiclass import OneVsOneClassifier, OneVsRestClassifier
from sklearn.model_selection import cross_val_score


def split(text):
    return nltk.tokenize.word_tokenize(text)


def split_root_filter(text):
    vector = split(text)
    vector_f = filter(lambda w: len(w) > 2 and w not in stop_words, vector)
    vector_r = map(lambda w: stemmer.stem(w), vector_f)

    return list(vector_r)


def read_data():
    df = pd.read_csv('csv/emails.csv')

    population = list(df.index)
    len_population = len(population)
    len_test_real = int(len_population * 0.2)    
    test_real = random.sample(population, len_test_real) # o ideal seria extratificar no pandas sem repetir
    
    test_real_df = df.ix[test_real]
    sample_df = df.drop(test_real)
    
    grouped_sample_df = sample_df.groupby('classificacao')
    
    lst_dic = []
    for name, group in grouped_sample_df:
        emails = list(group['email'])
        lst = set()
        for index, e in enumerate(emails):      
            srf = split_root_filter(e)
            lst.update(srf)

        dic = { word : index for index, word in enumerate(lst) }
        lst_dic.append((name, dic))

    test_real_marked = [e for e in test_real_df['classificacao']]
    test_real_sample = [e for e in test_real_df['email']]

    return lst_dic, sample_df[['email', 'classificacao']], test_real_sample, test_real_marked


def fit_predict_score(model, sample, marked, k=None):
    if k is None: k = int(len(marked) * 0.2)
    
    name = type(model).__name__
    score = np.mean(cross_val_score(model, sample, marked, cv=k))
    print('Algorithm "{}" score is {}, number test {} and variation {}'.format(name, score, len(marked), k))
    return score


def fit_predict(model, sample, marked, real_sample, real_marked):
    name = type(model).__name__
    model.fit(sample, marked)
    predict = model.predict(real_sample)
    score = sum(predict == real_marked) / len(real_marked) * 100
    print('Algorithm "{}" effectivity is {}%, number real test {}'.format(name, score, len(real_marked)))
    return score


def text_to_vectors(text, marked, lst_dic):
    text_vector = split_root_filter(text)
    max_vector = max([len(dic) for m, dic in lst_dic])

    v = [0] * max_vector

    for m, dic in lst_dic:
        if marked != m: continue
        for d in dic:
            index = dic[d]
            v[index] = int(d in text_vector)

    return v


# const
k = 2
stop_words = nltk.corpus.stopwords.words('portuguese')

# objects
stemmer = nltk.stem.RSLPStemmer()

nb = MultinomialNB()
ada = AdaBoostClassifier()
one_one = OneVsOneClassifier(SVC(random_state=0))
one_rest = OneVsRestClassifier(SVC(random_state=0))

# data
lst_dic, sample, test_real_sample, test_real_marked = read_data()

# text to bit
fit_sample = []
fit_marked = []
for e, c in sample.to_records(index=False):
    fit_marked.append(c)
    fit_sample.append(text_to_vectors(e, c, lst_dic))

dic_algorithm = {
    nb       : fit_predict_score(nb, fit_sample, fit_marked, k),
    ada      : fit_predict_score(ada, fit_sample, fit_marked, k),
    one_one  : fit_predict_score(one_one, fit_sample, fit_marked, k),
    one_rest : fit_predict_score(one_rest, fit_sample, fit_marked, k),
}

print(fit_marked)

# print(len(fit_marked))
# print(len(fit_sample))

# print(lst_dic)
# print(sample)
# print(test_sample)
# print(test_marked)
