import numpy as np
import random

class numpy_kmeans:
    def __init__(self, k=10, max_iterations=100):
        self.k = k
        self.max_iterations = max_iterations
        self.centroids = None

    def fit(self, data):
        data = np.array(data)
        sample = data.shape[0]
        indices = random.sample(range(sample), self.k)
        self.centroids = data[indices, :]

        for i in range(self.max_iterations):
            distances = np.zeros((sample, self.k))
            for i, centroid in enumerate(self.centroids):
                distances[:, i] = np.sum((data - centroid) ** 2, axis=1)
            closest_centroids = np.argmin(distances, axis=1)
            newCentroid = np.array([data[closest_centroids == i].mean(axis=0) for i in range(self.k)])
            
            if np.allclose(self.centroids, newCentroid):
                break
            self.centroids = newCentroid

