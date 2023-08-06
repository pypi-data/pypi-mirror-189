import numpy as np
import unittest
from sklearn.datasets import make_blobs, make_moons
from .vector import VectorNP
from .clustering import ClusteringNP

# generate 2d classification dataset|

class TestClusteringNP(unittest.TestCase):
    def setUp(self):
        X, y = make_blobs(n_samples=200, centers=2, n_features=2, random_state=1)
        self.X_np = [VectorNP(2, X[idx], _dtype=np.float64) for idx in range(len(X))]
        self.y_np = VectorNP(len(y), y, _dtype=np.float64)

        self.clusteringAlgo = ClusteringNP(self.X_np, self.y_np)

    def test_x_length(self):
        self.assertEqual(len(self.X_np), 200, "Initial X should be 200")

    def test_y_length(self):
        self.assertEqual(len(self.y_np), 200, "Initial Y should match number of X entries")

    def test_cluster_points(self):
        new_point1 = VectorNP(2, [-8, -2], _dtype=np.float64)
        new_point2 = VectorNP(2, [-1, 5], _dtype=np.float64)

        self.assertEqual(self.clusteringAlgo.newPoint(new_point1), 0, "First point should be classified as 0")
        self.assertEqual(self.clusteringAlgo.newPoint(new_point2), 1, "Second point should be classified as 1") 
        self.assertEqual(len(self.clusteringAlgo.X), len(self.clusteringAlgo.y), "Lengths should be equal")
        self.assertEqual(len(self.clusteringAlgo.X), 202, "Lenghts should be 2 more than at the start")
