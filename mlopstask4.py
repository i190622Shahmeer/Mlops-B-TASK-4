#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd

# Load your dataset
data = pd.read_excel('Dataset.xlsx')

# Extract the "salary" column as a NumPy array
salaries = data['Salary'].values

# Number of clusters (K)
K = 10

# Initialize random cluster centers
initial_centers = np.random.choice(salaries, K)

# Define a function to assign each data point to the nearest cluster
def assign_to_clusters(data, centers):
    # Calculate the squared distance from each data point to each cluster center
    distances = np.square(data[:, np.newaxis] - centers)

    # Assign each data point to the cluster with the closest center
    labels = np.argmin(distances, axis=1)

    return labels

# Define a function to update cluster centers based on the assigned data points
def update_centers(data, labels, K):
    centers = np.zeros(K)
    for k in range(K):
        cluster_data = data[labels == k]
        if len(cluster_data) > 0:
            centers[k] = np.mean(cluster_data)
    return centers

# Define a convergence threshold
tolerance = 1e-4

# Initialize cluster centers
cluster_centers = initial_centers

# Convergence flag
converged = False

# Maximum number of iterations (you can change this if needed)
max_iterations = 100

for i in range(max_iterations):
    # Assign data points to clusters
    labels = assign_to_clusters(salaries, cluster_centers)

    # Update cluster centers
    new_centers = update_centers(salaries, labels, K)

    # Check for convergence
    if np.all(np.abs(new_centers - cluster_centers) < tolerance):
        converged = True
        break

    cluster_centers = new_centers

if converged:
    # Create a DataFrame to display the clusters
    clustered_data = pd.DataFrame({'Salary': salaries, 'Cluster': labels})

    # Print the clustered data
    print(clustered_data)
else:
    print("K-means clustering did not converge within the specified number of iterations.")


# In[ ]:





# In[ ]:




