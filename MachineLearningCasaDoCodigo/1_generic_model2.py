from sklearn.naive_bayes import MultinomialNB

amostra = [
    [0,0,0],#with this, don't correct 1,1,1
    [0,0,1],
    [0,1,0],
    [0,1,1],
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1]
]

result = [0,1,0,1,0,1,0,1]

porc = 0.8
countAmostra = len(amostra)
countAmostraFit = int(countAmostra * porc)
countAmostraTest = -(countAmostra - countAmostraFit)

amostraFit = amostra[:countAmostraFit]
amostraTest = amostra[countAmostraTest:]

resultFit = result[:countAmostraFit]
resultTest = result[countAmostraTest:]

model = MultinomialNB()
model.fit(amostraFit, resultFit)
test = model.predict(amostraTest)

print("Total hits {}%.".format(sum(test==resultTest)/len(amostraTest)*100))