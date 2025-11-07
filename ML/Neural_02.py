import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

from sklearn.metrics import accuracy_score, confusion_matrix


# 1. Read Dataset
df = pd.read_csv("Churn_Modelling.csv")
print(df.head())


# 2. Split into features + target
X = df.iloc[:, 3:13]     # independent variables
y = df.iloc[:, 13]       # Exited


# Encode Geography & Gender
le = LabelEncoder()
X['Geography'] = le.fit_transform(X['Geography'])
X['Gender']    = le.fit_transform(X['Gender'])


# Train-Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)


# 3. Normalize
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test  = sc.transform(X_test)


# 4. Build ANN model
model = Sequential()

model.add(Dense(10, activation='relu', input_dim=X_train.shape[1]))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))   # output -> binary

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train
model.fit(X_train, y_train, epochs=20, batch_size=32)


# 5. Evaluate
y_pred = model.predict(X_test)
y_pred = (y_pred > 0.5)   # convert to 0/1

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
