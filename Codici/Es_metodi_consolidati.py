from sklearn.linear_model import LinearRegression

# Dati di esempio (X con 2 feature, y come target)
X = [[0, 1], [1, 1], [2, 2], [2, 3]]
y = [1, 2, 3, 4]

# Istanziazione modello
model = LinearRegression()

# Fase di addestramento con fit
model.fit(X, y)

# Ora model è "addestrato" e contiene i parametri
print(model.coef_)
print(model.intercept_)
