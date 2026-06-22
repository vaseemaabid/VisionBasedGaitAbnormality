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

print("Model Trained Successfully")
