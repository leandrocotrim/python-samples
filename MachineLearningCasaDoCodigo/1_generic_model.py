from sklearn.naive_bayes import MultinomialNB

characteristics = [
    [0,0,1],
    [0,1,0],
    [0,1,1],
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1]
]

result = [1, 0, 1, 0, 1, 0, 1]

count = len(characteristics)
indexFit = int(count * 80 / 100)
indexTest = -(count - indexFit)

characteristicsFit = characteristics[ : indexFit]
characteristicsTest = characteristics[indexTest : ]

resultFit = result[ : indexFit]
resultTest = result[indexTest : ]

model = MultinomialNB()
model.fit(characteristicsFit, resultFit)
test = model.predict(characteristicsTest)

#calculo de número de acertos
correctLen = sum(test == resultTest)

print("Acerto {}%".format(correctLen / len(test) * 100))
