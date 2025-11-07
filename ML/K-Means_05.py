# ------------------------------------------------------------
# K-Means Clustering – Sales Dataset
# ------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings("ignore")

# ------------------------------------------------------------
# 1) Load Dataset
# ------------------------------------------------------------
df = pd.read_csv("sales_data_sample.csv", encoding="ISO-8859-1")
print("Original Data:")
print(df.head())

# ------------------------------------------------------------
# 2) Select only required numerical columns
# ------------------------------------------------------------
data = df[['ORDERLINENUMBER', 'SALES']]
print("\nSelected Columns:")
print(data.head())

# ------------------------------------------------------------
# 3) Scaling
# ------------------------------------------------------------
scaler = StandardScaler()
scaled_values = scaler.fit_transform(data)

# ------------------------------------------------------------
# 4) Find optimal number of clusters → Elbow Method
# ------------------------------------------------------------
wcss = []
for i in range(1, 11):
    model = KMeans(n_clusters=i, init='k-means++', random_state=42)
    model.fit(scaled_values)
    wcss.append(model.inertia_)

plt.figure(figsize=(6, 4))
plt.plot(range(1, 11), wcss, 'ro-')
plt.title("Elbow Method")
plt.xlabel("No. of Clusters")
plt.ylabel("WCSS")
plt.grid()
plt.show()

# ------------------------------------------------------------
# 5) Apply K-Means with chosen clusters
# ------------------------------------------------------------
optimal_k = 7   # from elbow curve
kmeans = KMeans(n_clusters=optimal_k, init='k-means++', random_state=42)
clusters = kmeans.fit_predict(scaled_values)

# ------------------------------------------------------------
# 6) Add cluster labels to dataframe
# ------------------------------------------------------------
df['Cluster'] = clusters

print("\nClustered Data:")
print(df[['ORDERLINENUMBER', 'SALES', 'Cluster']].head())

# ------------------------------------------------------------
# 7) Visualization
# ------------------------------------------------------------
plt.figure(figsize=(7, 5))
plt.scatter(
    df['ORDERLINENUMBER'], df['SALES'],
    c=df['Cluster'], cmap='rainbow'
)
plt.xlabel("ORDERLINENUMBER")
plt.ylabel("SALES")
plt.title("K-Means Clustering Visualization")
plt.grid()
plt.show()



