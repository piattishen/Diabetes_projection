# %%
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale=StandardScaler()

# %%
df = pd.read_csv(r"diabetes.csv")
df

# %%
X = df[["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]]
scaledX = scale.fit_transform(X)
print(scaledX)
y = df["Outcome"]

# %%
regr = linear_model.LinearRegression()
regr.fit(X,y)

# %%
prediction = regr.predict([[1, 80, 80, 22, 10, 27.8, 0.442, 26]])
print(prediction)

# %%
regr2 = linear_model.LinearRegression()
regr2.fit(scaledX,y)

# %%
scaled = scale.transform([[1, 80, 80, 22, 10, 27.8, 0.442, 26]])

# %%
prediction2 = regr2.predict([scaled[0]])
print(prediction2)


