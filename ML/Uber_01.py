import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("uber.csv")
df.head()
print(df.info())
print("------------------")
print(df.isnull().sum())
df= df.dropna()

# Cal dist using Euclidean formula
df['distance'] = (
    (
        (df['dropoff_latitude']-df['pickup_latitude']) ** 2 +
        (df['dropoff_longitude']-df['pickup_longitude']) ** 2
    ) * 0.5
)

# filter for reasonable fare, passenger count, and distance (OUTLIERS)
df = df[(df['fare_amount']>0) & (df['fare_amount']<100)]
df = df[(df['passenger_count']>0) & (df['passenger_count']<=6)]
df = df[df['distance']<5]

# extract time features
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
df['hour']= df['pickup_datetime'].dt.hour
df['day_of_week'] = df['pickup_datetime'].dt.dayofweek

# boxplot for fare amount
sns.boxplot(x=df['fare_amount'])
plt.title("Boxplot for Fare Amount (Outliers)")
plt.show()

# correlation heatmap
corr = df[['fare_amount', 'distance', 'passenger_count', 'hour', 'day_of_week']].corr()
sns.heatmap(corr, annot = True, cmap = "coolwarm")
plt.title("Correlation Matrix")
plt.show()

# feature and target selection
X= df[['distance', 'passenger_count', 'hour', 'day_of_week']] #independent var (input)
y = df['fare_amount'] # dependent var

# train_test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.2, random_state = 42
)

# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

# Random Forest
rf = RandomForestRegressor(n_estimators = 100, random_state = 42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

# Evaluation Function
def evaluate(y_true, y_pred, model_name):
  rmse = np.sqrt(mean_squared_error(y_true, y_pred))
  r2 = r2_score(y_true, y_pred)
  print(f"{model_name} Results:")
  print(f"R2 Score: {r2:.4f}")
  print(f"RMSE: {rmse:.4f}\n")

evaluate(y_test, y_pred_lr, "Linear Regression")
evaluate(y_test, y_pred_rf, "Random Forest")