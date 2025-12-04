# Week 10 – Customer Segmentation using K-Means & PCA
# ---------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# ------------------------------------
# 1. Load dataset
# ------------------------------------
data = pd.read_csv("customer_churn.csv")
print("Original shape:", data.shape)

# We'll use numerical columns for clustering
# Drop non-numeric or ID columns
data = data.drop(columns=['CustomerID'])

# Encode categorical columns (one-hot)
cat_cols = data.select_dtypes(include='object').columns
data_encoded = pd.get_dummies(data, columns=cat_cols, drop_first=True)

print("Encoded shape:", data_encoded.shape)

# ------------------------------------
# 2. Standardize features
# ------------------------------------
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data_encoded)

# ------------------------------------
# 3. Find optimal number of clusters (Elbow Method)
# ------------------------------------
wcss = []  # within-cluster sum of squares
K = range(2, 11)
for k in K:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(scaled_data)
    wcss.append(km.inertia_)

plt.figure(figsize=(6,4))
plt.plot(K, wcss, 'bo-')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('WCSS')
plt.title('Elbow Method for Optimal k')
plt.show()

# ------------------------------------
# 4. Fit final K-Means model
# ------------------------------------
optimal_k = 4   # <- choose after checking elbow plot
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(scaled_data)

data_encoded['Cluster'] = cluster_labels
print(data_encoded[['Cluster']].value_counts())

# ------------------------------------
# 5. PCA for 2-D Visualization
# ------------------------------------
pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_data)
pca_df = pd.DataFrame(data=pca_result, columns=['PC1', 'PC2'])
pca_df['Cluster'] = cluster_labels

plt.figure(figsize=(7,5))
sns.scatterplot(x='PC1', y='PC2', hue='Cluster',
                palette='Set2', data=pca_df, s=60)
plt.title('Customer Segments visualized via PCA')
plt.legend(title='Cluster')
plt.show()

# ------------------------------------
# 6. Save segmented data
# ------------------------------------
data_encoded.to_csv("customer_segments.csv", index=False)
print("\nCustomer segmentation complete! Saved as customer_segments.csv")
