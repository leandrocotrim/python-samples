from collections import Counter
import pandas as pd
import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsOneClassifier, OneVsRestClassifier
from sklearn.model_selection import cross_val_score


def get_dummies():
    df = pd.read_csv('csv/status_client.csv')
    samples_df = df[['recencia', 'frequencia', 'semanas_de_inscricao']]
    markeds_df = df['situacao']

    samples = pd.get_dummies(samples_df)
    markeds = markeds_df

    return samples, markeds


def fit_and_test_cross(model, sampleFit, markedFit, k):
    hits = np.mean(cross_val_score(model, sampleFit, markedFit, cv=k))

    print('Algorithm "{}" mean hits {} with k={}'.format(
        type(model).__name__,
        hits,
        k
    ))

    return hits


def fit_and_test_winner(model, sampleFit, markedFit, sampleReal, markedReal):
    model.fit(sampleFit, markedFit)
    count = len(markedReal)
    predict = model.predict(sampleReal)
    hits = sum(predict==markedReal)/count * 100
    print('Algorithm "{}" hits {}% number tests {}'.format(
        type(model).__name__,
        hits,
        count
    ))

    return hits

# constants
porcFit = 0.8
k = 3

# datas
samples, markeds = get_dummies()

# calc separete datas
countTotal = len(samples)
countFit = int(countTotal * porcFit)
#countReal = countTotal - countFit - countTest

# separete datas
sampleFit = samples[: countFit]
markedFit = markeds[: countFit]
sampleReal = samples[countFit:]
markedReal = markeds[countFit:]

# Algorithms
nb = MultinomialNB()
ada = AdaBoostClassifier()
oneVsOne = OneVsOneClassifier(LinearSVC(random_state=0))
oneVsRest = OneVsRestClassifier(LinearSVC(random_state=0))

# Fit and Test Algorithms
hits_nb = fit_and_test_cross(nb, sampleFit, markedFit, k)
hits_ada = fit_and_test_cross(ada, sampleFit, markedFit, k)
hits_oneVsOne = fit_and_test_cross(oneVsOne, sampleFit, markedFit, k)
hits_oneVsRest = fit_and_test_cross(oneVsRest, sampleFit, markedFit, k)

# kick
dumb_kick = max(Counter(markedReal).values())

hits_dumb = dumb_kick / (countTotal - countFit) * 100
print('Algorithm "Dumb" hits {}% tests number {}'.format(
    hits_dumb,
    (countTotal - countFit)
))

dic = {
    hits_nb: nb,
    hits_ada: ada,
    hits_oneVsOne: oneVsOne,
    hits_oneVsRest: oneVsRest
}

winner_model = dic[max(dic)]
print('\nWinning Algorithm')
fit_and_test_winner(winner_model, sampleFit, markedFit, sampleReal, markedReal)
