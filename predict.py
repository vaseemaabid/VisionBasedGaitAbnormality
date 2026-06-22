from sklearn.ensemble import RandomForestClassifier

X = [
    [45, 1.2],
    [50, 1.1],
    [48, 1.3],
    [52, 1.0],
    [47, 1.25]
]

y = [0, 1, 0, 1, 0]

model = RandomForestClassifier()

model.fit(X, y)

prediction = model.predict([[46, 1.2]])

if prediction[0] == 0:
    print("Normal Gait")
else:
    print("Abnormal Gait")
