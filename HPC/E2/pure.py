import random

class kmeans:
    def __init__(self, k=10, max_iterations=100):
        self.k = k
        self.max_iterations = max_iterations
        self.centroids = []  
        self.clusters = [[] for _ in range(k)]  

    def convergence(self, new_centroids):
        return new_centroids == self.centroids
    
    def fit(self, data):
        self.centroids = random.sample(data, self.k)              
        for _ in range(self.max_iterations):           
            self.clusters = self.addPoints(data)             
            new_centroids = self.update()             
            if self.convergence(new_centroids):
                break  
            self.centroids = new_centroids  

    def euclideanDistance(self, point1, point2):
        return sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)) ** 0.5

    def addPoints(self, data):
        clusters = [[] for _ in self.centroids]
        for point in data:
            closest_centroid = min(range(len(self.centroids)),
                                    key=lambda i: self.euclideanDistance(point, self.centroids[i]))
            clusters[closest_centroid].append(point)
        return clusters

    def update(self):
        return [
            [sum(dim) / len(cluster) for dim in zip(*cluster)]  
            if cluster else random.choice(self.centroids)  
            for cluster in self.clusters
        ]

