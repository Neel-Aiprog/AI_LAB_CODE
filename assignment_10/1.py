import numpy as np
import pandas as pd
# assign city nearest airport
# update airport locations
# repeat
data = pd.read_csv("assignment_10/cities.csv")
points = data.values   
# first we load the data from the csv file and we create a numpy array from the data
k = 3  
# k is equal to 3 is basically the number of locations i want to find that is basically the number of airports
# now assign clusters is basically for assigning each city to its nearest airport
def assign_clusters(points, centers):
    clusters = [[] for _ in range(k)] #these are for creating empty clusters
    for p in points:
        distances = [np.linalg.norm(p - c) for c in centers] #this is for calculating distance between point and city 
        idx = np.argmin(distances) #this is for finding nearest airport index
        clusters[idx].append(p) #this is for assigning that city to that cluster
    return clusters

def compute_loss(clusters, centers):
    loss = 0
    for i in range(k):
        for p in clusters[i]:
            loss += np.sum((p - centers[i])**2) #we calculate the squared distance of each point of each cluster to calculate the loss
            # as the loss is the sum of the squared distance
    return loss

def gradient_descent(points, k, lr=0.01, iterations=100):
    centers = points[np.random.choice(len(points), k, replace=False)]
    #here we have a learning rate number of iterations and points
    # we randomly select centers from the points
    for _ in range(iterations):
        clusters = assign_clusters(points, centers)

        new_centers = []
        for i in range(k):
            if len(clusters[i]) == 0:
                new_centers.append(centers[i])
                continue

            cluster_points = np.array(clusters[i])


            gradient = -2 * np.sum(cluster_points - centers[i], axis=0) #which direction reduces error fastest

            
            new_center = centers[i] - lr * gradient #moves center slightly towards cluster points
            new_centers.append(new_center)

        centers = np.array(new_centers)

    clusters = assign_clusters(points, centers)
    loss = compute_loss(clusters, centers)

    return centers, clusters, loss


def newton_method(points, k, iterations=10):
    centers = points[np.random.choice(len(points), k, replace=False)].astype(float)

    for _ in range(iterations):
        clusters = assign_clusters(points, centers)
        new_centers = []

        for i in range(k):
            if len(clusters[i]) == 0:
                new_centers.append(centers[i])
                continue

            cluster_points = np.array(clusters[i])
            n_i = len(cluster_points)

            gradient = 2 * (n_i * centers[i] - cluster_points.sum(axis=0))  
            hessian  = 2 * n_i                                                
            new_center = centers[i] - gradient / hessian                  

            new_centers.append(new_center)

        new_centers = np.array(new_centers)
        if np.allclose(centers, new_centers):
            break
        centers = new_centers

    

    clusters = assign_clusters(points, centers)
    loss = compute_loss(clusters, centers)
    return centers, clusters, loss
gd_centers, gd_clusters, gd_loss = gradient_descent(points, k)
nm_centers, nm_clusters, nm_loss = newton_method(points, k)


print("Gradient Descent Centers:\n", gd_centers)
print("Gradient Descent Loss:", gd_loss)

print("\nNewton Method Centers:\n", nm_centers)
print("Newton Method Loss:", nm_loss)