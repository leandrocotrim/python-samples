#MultinomialNB
#todas 75.0% -> (7 testes) -> 10%
#busca 75.0% -> (7 testes) -> 10%
import pandas as pd
from collections import Counter
#from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier

search_df = pd.read_csv('csv/search2.csv')

amostra_df = search_df[['home', 'busca', 'logado']]
result_df = search_df['comprou']

dummies_amostra = pd.get_dummies(amostra_df)
dummies_result = result_df #pd.get_dummies(result_df)

porc = 0.9
amostraLen = len(dummies_amostra)
amostraFitLen = int(amostraLen * porc)
amostraTestLen = (amostraLen - amostraFitLen)

amostraFit = dummies_amostra[:amostraFitLen].values
resultFit = dummies_result[:amostraFitLen].values

amostraTest = dummies_amostra[-amostraTestLen:].values
resultTest = dummies_result[-amostraTestLen:].values

#model = MultinomialNB()
model = AdaBoostClassifier()

model.fit(amostraFit, resultFit)
test = model.predict(amostraTest)

dumb = max(Counter(test).values())

print("Total hits {}%".format(sum(test==resultTest)/len(resultTest)*100))
print("Total hits Dumb {}%".format(dumb/len(resultTest)*100))
