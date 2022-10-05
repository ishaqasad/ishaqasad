import matplotlib.pyplot as plt
import jax
import jax.numpy as jnp
from jax import grad, jit, vmap
from jax import random
from functools import partial

def update_assignment(samples, centroids):
    assignment = vmap(lambda point: find_min(point,centroids))(samples)
    distortions = (vmap(jnp.linalg.norm)(centroids[assignment,:] - points))
    return assignment, distortions

def find_min(centroids,point):
  return jnp.argmin(vmap(jnp.linalg.norm)(centroids - point))

def improve_centroids(values, k):
    centroids , distortions , _ = values
    points_assignments, _ = update_assignment(points,centroids)
    new_centroids = vmap( lambda cluster_id : jnp.sum(jnp.where(points_assignments[:,jnp.newaxis] == cluster_id,points,0) , axis = 0) /
        jnp.sum(jnp.where(points_assignments == cluster_id[0] , jnp.ones(points.shape[0]) , 0))) (jnp.arange(k).T[:,jnp.newaxis])
    points_assignments , new_distortions = update_assignment(points,new_centroids)
    return new_centroids, new_distortions.mean(), jnp.mean(distortions)

key = random.PRNGKey(0)
key, *subkeys = random.split(key, 4)
points = jnp.concatenate([
    jax.random.normal(subkeys[0], (400, 2)) + jnp.array([6, 0]),
    jax.random.normal(subkeys[1], (200, 2)) + jnp.array([.5, 1]),
    jax.random.normal(subkeys[2], (200, 2)) + jnp.array([-4, -1]),
])

num_clusters = 4
key, subkey = random.split(key)

id = random.choice(subkey, points.shape[0] , (4,), replace = False)
id

initial_centroids = points[id]

_, initial_distortion =  update_assignment(points,initial_centroids)
values = improve_centroids((initial_centroids, initial_distortion, jnp.inf), 4)
values[2].dtype

thresh=1e-5

while(values[2] - values[1] > thresh):
  values = improve_centroids(values, 4)

centroids = values[0]

# Perform the final assignment
final_assignments, _ = update_assignment(points, centroids)
plt.plot(points[:,0] , points[:,1], "b.")
plt.plot(centroids[:,0] , centroids[:,1] , "r.")

