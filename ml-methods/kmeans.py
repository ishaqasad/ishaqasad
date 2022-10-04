from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
import numpy as np


def distortion(dataset,clusters,assignments):
  """
    Calculate distortion of a certain data set and cluster assignments
    Parameters:
  | dataset: an ndarray, containing the data that has been clustered
  | clusters: an ndarray, containing the cluster centroids
  | assignmnets: an ndarray wherin assignmnet[i] = index of 
  |              dataset[i] asigned cluster 
    Returns:
  | a float equaling the distortion of the dataset and the clusters
  """
  distortion = 0  # initialize
  for i in range(dataset.shape[0]):
    # Sum the squared difference between a point and its assigned  centroid
    distortion += np.sum((dataset[i] - clusters[assignments[i]])**2) 
  # Return the sum of squared errors divided by number of points
  return distortion/dataset.shape[0]

def k_means(k, dataset):
  """
    Calculate the k cluster assignments which best fit the dataset
    Parameters:
  | dataset: an ndarray, containing the data that needs to be clustered
  | k: an integer, equaling the number of clusters to assign; k > 2 
    Returns:
  | clusters: an ndarray containing the cluster centroids
  | assignments: an ndarray wherin assignmnet[i] = index of 
  |              dataset[i]'s asigned cluster
  """
  # Initialisation

  size = dataset.shape
  clusters = np.empty((k,size[1])) # initialise k empty clusters
  bucket = {} # initialise a counter dictionary
  prev_clusters = np.empty((k,size[1])) 
  # initialise initial asignment of the datapoints to a cluster
  assignment = np.zeros(size[0], dtype= np.int32) 
  count = 0; 
  max_iter = 100 # initialise max interations the function will perform before exiting

  # initialise cluster counter dictionary to 0
  for i in range(k):
    bucket[i] = 0
  # initialise random clusters in the range of the max and min of the data_set
  for i in range(k):
      for j in range(size[1]):
        clusters[i,]= np.random.random() * (dataset[:,j].max()-dataset[:,j].min()) + dataset[:,j].min()
  
  # loop until max iterations is reached or clusters have not changed
  while(not np.array_equal(clusters, prev_clusters) or count <= max_iter):
    count += 1; # increase counter
    # reset counter dictionary to 0
    for i in range(k):
      bucket[i] = 0

    prev_clusters = np.copy(clusters) # create a copy of previous clusters
    # initialise a mask for each cluster
    cluster_mask = np.zeros((k,size[0],size[1]))  

    # find each data points closest cluster centroid
    for i in range(size[0]):
      min_distance = float('inf')
      # iterate throuh each cluster
      for j in range(k):
        # calculating euclidean distance between tuples
        dist =np.sqrt(np.sum((dataset[i] -clusters[j])**2))
        # finding minimum
        if dist < min_distance:
          min_distance = dist
          assignment[i] = j

    # for each data point change its asigned cluster_mask to 1's to enable averaging
    # and set the counter for each cluster
    for i in range(size[0]):
      cluster = assignment[i]
      bucket[cluster] += 1
      cluster_mask[cluster, i] = np.ones(size[1]);
    # iterate through each cluster and average the data points belonging to the cluster
    # set the new cluster centorid as the average
    for i in range(k):
      # Check if cluster is empty
      if(bucket[i] != 0):
        # Apply the cluster mask to the dataset and average the columns
        clusters_points= np.multiply(dataset,cluster_mask[i]);
        for j in range(size[1]):
          clusters[i,j] = np.sum(clusters_points[:,j])/bucket[i]
    
  return clusters, assignment

