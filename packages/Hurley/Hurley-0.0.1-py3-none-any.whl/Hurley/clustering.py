from .vector import VectorNP
import numpy as np

class ClusteringNP:
    def __init__(self, X, y, k = 2):
        self.X = X
        self.y = y
        self.k = k if k >= 2 else 2

        if len(self.X) != len(self.y):
            raise Exception("Xs are not mapped to target appropriately!")
     
    def norm(self, arr, root = 2):
        """
        Euclidean norm is 2
        Others here later
        """
        return round(np.power(np.sum(np.power(arr, root)), 1 / root))
    
    def newPoint(self, vec, _return = True):
        if len(vec) != len(self.X[0].arr):
            raise Exception("New vector doesnt match shape of X")
        
        distances = sorted([self.norm([self.X[idx].arr[idy] - vec.arr[idy] for idx in range(len(self.X))]) for idy in range(len(vec.arr))])
        nearest_neighbor_ids = distances[:self.k]
        nearest_neighbor_rings = self.y.arr[nearest_neighbor_ids]
        prediction = sum(nearest_neighbor_rings) // len(nearest_neighbor_rings)
        
        self.X = np.concatenate((self.X, [vec]), axis=0)
        self.y.concat(VectorNP(1, [prediction], _dtype=np.float64))

        if _return:
            return prediction
