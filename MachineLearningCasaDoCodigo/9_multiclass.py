from collections import Counter

import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsOneClassifier, OneVsRestClassifier


def get_dummies():
    search_df = pd.read_csv('csv/status_client.csv')
    #search_df = pd.read_csv('csv/search2.csv')

    sample_df = search_df[['recencia', 'frequencia', 'semanas_de_inscricao']]
    marked_df = search_df['situacao']

    dummies_sample = pd.get_dummies(sample_df)
    dummies_marked = marked_df

    return dummies_sample, dummies_marked


def fit_and_test(model, sampleFit, markedFit, sampleTest, markedTest):

    name = type(model).__name__

    model.fit(sampleFit, markedFit)
    test = model.predict(sampleTest)
    lenTest = len(markedTest)
    hits = sum(test == markedTest) / lenTest * 100

    print('Algorithm "{}" hits {}% test number {}'.format(name, hits, lenTest))
    return hits


dummies_sample, dummies_marked = get_dummies()

porcFit = 0.8
procTest = 0.1
sampleLen = len(dummies_sample)
sampleFitLen = int(sampleLen * porcFit)
sampleRest = (sampleLen - sampleFitLen)
sampleTestLen = int(sampleRest/2)
sampleRealLen = sampleRest - sampleTestLen

sampleFit = dummies_sample[:sampleFitLen].values
markedFit = dummies_marked[:sampleFitLen].values

sampleTest = dummies_sample[sampleFitLen: sampleFitLen + sampleTestLen].values
markedTest = dummies_marked[sampleFitLen: sampleFitLen + sampleTestLen].values

sampleReal = dummies_sample[-sampleRealLen:].values
markedReal = dummies_marked[-sampleRealLen:].values

nb = fit_and_test(MultinomialNB(), sampleFit,
                  markedFit, sampleTest, markedTest)
ada = fit_and_test(AdaBoostClassifier(), sampleFit,
                   markedFit, sampleTest, markedTest)

oneVsOne = fit_and_test(OneVsOneClassifier(LinearSVC(random_state=0)), sampleFit,
                        markedFit, sampleTest, markedTest)
oneVsRest = fit_and_test(OneVsRestClassifier(LinearSVC(random_state=0)), sampleFit,
                         markedFit, sampleTest, markedTest)

lenTest = len(markedReal)
dumb = max(Counter(markedTest).values())
print('Algorithm "Dumb" hits {}% test number {}'.format(
    dumb / lenTest * 100, lenTest))

dic = {
    nb: MultinomialNB,
    ada: AdaBoostClassifier,
    oneVsOne: OneVsOneClassifier(LinearSVC(random_state=0)),
    oneVsRest: OneVsRestClassifier(LinearSVC(random_state=0))
}
#dic = {}
#dic[nb] = MultinomialNB
#dic[ada] = AdaBoostClassifier

algorithm = dic[max(dic)]

print('\nWinning algorithm')
fit_and_test(algorithm, sampleFit, markedFit, sampleReal, markedReal)
