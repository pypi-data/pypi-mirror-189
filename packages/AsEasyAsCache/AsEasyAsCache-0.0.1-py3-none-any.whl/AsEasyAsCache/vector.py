import numpy as np
from .abstractClasses import BaseArrayNP

#import sympy as sp

class VectorNP(BaseArrayNP):
    def __init__(self, capacity, arr=[], _dtype=np.int8):
        try:
            self.arr = np.array(arr, dtype=_dtype)
        except:
            raise Exception("Data type is not recognized")

        self.size = len(self.arr)
        self.capacity = capacity

    def dimensions(self):
        return super().dimensions(self.arr)

    def typeID(self):
        return super().typeID(self.arr)

    def __len__(self):
        return len(self.arr)

    def __mul__(self, other):
        return self.arr * other.arr

    def __sub__(self, other):
        return self.arr - other.arr

    def __add__(self, other):
        return self.arr + other.arr

    def concat(self, other, _return=False):
        self.arr = np.concatenate((self.arr, other.arr))
        if _return:
            return self.arr

    def linearCombination(self, other):
        """
        With same VectorNP it becomes the sum of squares!
        """
        return np.sum(np.multiply(self.arr, other.arr))

    def innerProduct(self, other):
        """
        <a, b>
        <a | b>
        (a, b)
        a * b
        a^T * b = b^T * a
        """
        return np.sum(np.multiply(np.transpose(self.arr), other.arr))

    """
    def getLambdify(self, function, variable):
        return sp.lambdify(variable, function, "numpy")
    
    def affinePrediction(self, formula, variable):
        functionSP = self.getLambdify(formula, variable)
        return functionSP(self.arr)
    """

    def affinePrediction(self, weights):
        return np.sum(np.multiply(np.transpose(self.arr), weights))

    def regressionModel(self, weights, b):
        return self.affinePrediction(weights) + b

    def norm(self, root=2):
        """
        Euclidean norm is 2
        Others here later
        """
        return np.power(np.sum(np.power(self.arr, root)), 1 / root)

    def rms(self, divisor, root=2):
        """
        RMS = Root Mean Square
        """
        return self.norm(root=root) / np.power(divisor, 1 / root)

    def normOfSum(self, other, root=2):
        intermediate = (
            np.power(self.norm(root=root), root)
            + np.sum(2 * np.transpose(self.arr) * other.arr)
            + np.power(other.norm(root=root), root)
        )
        return np.power(intermediate, 1 / root)

    def distance(self, other, root=2):
        return np.power(np.sum(np.power(self.arr - other.arr, root)), 1 / root)

    def rmsDeviation(self, other, divisor=2, root=2):
        return self.distance(other, root=root) / np.power(divisor, 1 / root)

    def triangleInequality(self, other1, other2, root=2):
        """
        Triangle inequality: || x + y || <= || x || + || y ||
        """
        values = sorted(
            [self.distance(other1), self.distance(other2), other1.distance(other2)]
        )

        return values[-1] <= (values[0] + values[1])

    def standardDeviation(self):
        avg = np.average(self.arr)
        return (sum([(x - avg) ** 2 for x in self.arr]) / len(self.arr)) ** (1 / 2)

    def standardizedVersion(self, x):
        """
                Its entries are sometimes called the z-scores associated with the
        original entries of x. For example, z4 = 1.4 means that x4 is 1.4 standard deviations
        above the mean of the entries of x.
        """
        return (x - np.average(self.arr)) / self.standardDeviation()

    def angleBetweenVectors(self, other, degrees=True):
        result = np.arccos(self.innerProduct(other) / (self.norm() * other.norm()))

        return result * 60 if degrees else result

    def innerProductWithAngle(self, other, angle, degrees=False):
        if degrees:
            angle /= 60

        return self.norm() * other.norm() * np.cos(angle)

    def normOfSumViaAngles(self, other, angle, degrees=False):
        if degrees:
            angle /= 60

        x_norm = self.norm()
        y_norm = other.norm()

        return np.sqrt(x_norm**2 + 2 * x_norm * y_norm * np.cos(angle) + y_norm**2)

    def correlationCoefficient(self, other):
        """
                For example, ρ = 30% means ρ = 0.3. When ρ = 0, we say the vectors
        are uncorrelated.
        """
        a_avg = np.average(self.arr)
        b_avg = np.average(other.arr)
        a_demeaned = np.array([x - a_avg for x in self.arr])
        b_demeaned = np.array([x - b_avg for x in other.arr])
        innerProduct = np.sum(np.multiply(np.transpose(a_demeaned), b_demeaned))

        def norm(arr, root=2):
            return np.power(np.sum(np.power(arr, root)), 1 / root)

        return innerProduct / (norm(a_demeaned) * norm(b_demeaned))

    def correlationCoefficient2(self, other):
        """
                For example, ρ = 30% means ρ = 0.3. When ρ = 0, we say the vectors
        are uncorrelated.
        """
        a_avg = np.average(self.arr)
        b_avg = np.average(other.arr)
        a_demeaned = np.array([x - a_avg for x in self.arr])
        b_demeaned = np.array([x - b_avg for x in other.arr])
        u = a_demeaned / self.standardDeviation()
        v = b_demeaned / other.standardDeviation()

        innerProduct = np.sum(np.multiply(np.transpose(u), v))
        return innerProduct / len(v)
