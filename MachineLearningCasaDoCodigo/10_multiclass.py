from collections import Counter
import pandas as pd

from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsOneClassifier, OneVsRestClassifier


def get_dummies():
    df = pd.read_csv('csv/status_client.csv')
    samples_df = df[['recencia', 'frequencia', 'semanas_de_inscricao']]
    markeds_df = df['situacao']

    samples = pd.get_dummies(samples_df)
    markeds = markeds_df

    return samples, markeds


def fit_and_test(model, sampleFit, markedFit, sampleTest, markedTest):
    model.fit(sampleFit, markedFit)
    test = model.predict(sampleTest)
    countTest = len(markedTest)
    hits = sum(test == markedTest) / countTest * 100

    print('Algorithm "{}" hits {}% tests number {}'.format(
        type(model).__name__,
        hits,
        countTest
    ))

    return hits


# constants
porcFit = 0.8
porcTest = 0.1

# datas
samples, markeds = get_dummies()

# calc separete datas
countTotal = len(samples)
countFit = int(countTotal * porcFit)
countTest = int(countTotal * porcTest)
#countReal = countTotal - countFit - countTest

# separete datas
sampleFit = samples[: countFit]
markedFit = markeds[: countFit]
sampleTest = samples[countFit: countFit + countTest]
markedTest = markeds[countFit: countFit + countTest]
sampleReal = samples[countFit + countTest:]
markedReal = markeds[countFit + countTest:]

# Algorithms
nb = MultinomialNB()
ada = AdaBoostClassifier()
oneVsOne = OneVsOneClassifier(LinearSVC(random_state=0))
oneVsRest = OneVsRestClassifier(LinearSVC(random_state=0))

# Fit and Test Algorithms
hits_nb = fit_and_test(
    nb, sampleFit, markedFit, sampleTest, markedTest)
hits_ada = fit_and_test(
    ada, sampleFit, markedFit, sampleTest, markedTest)
hits_oneVsOne = fit_and_test(
    oneVsOne, sampleFit, markedFit, sampleTest, markedTest)
hits_oneVsRest = fit_and_test(
    oneVsRest, sampleFit, markedFit, sampleTest, markedTest)

# kick
dumb_kick = max(Counter(markedTest).values())

hits_dumb = dumb_kick / countTest * 100
print('Algorithm "Dumb" hits {}% tests number {}'.format(
    hits_dumb,
    countTest
))

dic = {
    hits_nb : nb,
    hits_ada : ada,
    hits_oneVsOne : oneVsOne,
    hits_oneVsRest : oneVsRest
}

winner_model = dic[max(dic)]
print('\nWinning Algorithm')
fit_and_test(winner_model, sampleFit, markedFit, sampleReal, markedReal)
