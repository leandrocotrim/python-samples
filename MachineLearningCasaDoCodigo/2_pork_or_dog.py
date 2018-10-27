from sklearn.naive_bayes import MultinomialNB

pork1 = [1, 1, 0]
pork2 = [1, 1, 0]
pork3 = [1, 1, 0]

dog1 = [1, 1, 1]
dog2 = [0, 1, 1]
dog3 = [0, 1, 1]

animals = [pork1, dog1, pork2, dog2, pork3, dog3]
result = [1, 0, 1, 0, 1, 0]

porc = 80
animalsLen = len(animals)

animalsFitIndex = int(animalsLen * porc / 100)
animalsTestIndex =  -(animalsLen - animalsFitIndex)

animalsFit = animals[:animalsFitIndex]
animalsTest = animals[animalsTestIndex:]

resultFit = result[:animalsFitIndex]
resultTest = result[animalsTestIndex:]

model = MultinomialNB()
model.fit(animalsFit, resultFit)

resultPredict = model.predict(animalsTest)

print("Total de acertos {}%".format(sum(resultPredict==resultTest) / len(resultTest) * 100))





