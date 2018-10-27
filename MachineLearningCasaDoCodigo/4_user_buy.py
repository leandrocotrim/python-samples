from sklearn.naive_bayes import MultinomialNB
from csv_import_access import load_data

data, result = load_data()

porc = 0.8
amostraLen = len(data)
sampleLen = int(amostraLen * porc)
testLen = -(amostraLen - sampleLen)

sampleDataFit = data[:sampleLen]
sampleResultFit = result[:sampleLen]

sampleDataTest = data[testLen:]
sampleResultTest = result[testLen:]

model = MultinomialNB()
model.fit(sampleDataFit, sampleResultFit)
test = model.predict(sampleDataTest)

hits = sum(sampleResultTest==test)
print("Total hits {}%".format(hits/len(test) * 100))
