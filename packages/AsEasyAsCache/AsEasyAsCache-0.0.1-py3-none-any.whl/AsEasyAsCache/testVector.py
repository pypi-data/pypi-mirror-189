from .vector import VectorNP
import numpy as np
import unittest

class TestVectorNP(unittest.TestCase):
    def setUp(self):
        self.vec1 = VectorNP(10, arr = [i for i in range(10)], _dtype = np.float64)
        self.vec2 = VectorNP(10, arr = [i+1 for i in range(10)])
        self.vec3 = VectorNP(3, arr = [0.12,0.31,0.26], _dtype=np.float64)
        self.vec4 = VectorNP(3, arr = [2, -1, 2], _dtype = np.float64)
        self.vec5 = VectorNP(3, arr = [1,2,3], _dtype = np.float64)
        self.vec6 = VectorNP(4, arr = [1.8, 2.0, -3.7, 4.7], _dtype = np.float64)
        self.vec7 = VectorNP(4, arr = [0.6, 2.1, 1.9, -1.4], _dtype = np.float64)
        self.vec8 = VectorNP(4, arr = [2.0, 1.9, -4.0, 4.6], _dtype = np.float64)
        self.vec9 = VectorNP(4, arr = [1, -2, 3, 2])
        self.vec10 = VectorNP(3, arr = [1, 2, -1])
        self.vec11 = VectorNP(3, arr = [2, 0, -3])
    
    def test_length(self):
        self.assertEqual(len(self.vec1), 10, "Length should be 10")

    def test_dimensions(self):
        self.assertEqual(len(self.vec1.dimensions()), 1, "Vectors only have 1 dimension")
        
    def test_type(self):
        self.assertEqual(str(self.vec1.typeID()), 'float64', "Data type should be np.float64")
    
    def test_multiplication(self):
        self.assertEqual((self.vec2 * self.vec1).tolist(), [0.0, 2.0, 6.0, 12.0, 20.0, 30.0, 42.0, 56.0, 72.0, 90.0], "Multiplication result should be equal!")

    def test_subtraction(self):
        self.assertEqual(np.sum(self.vec2 - self.vec1), 10.0, "Subtraction should be 10")
        
    def test_addition(self):
        self.assertEqual(np.sum(self.vec2 + self.vec1), 100.0, "Addition should be 100")
    
    # Need to Test
    def test_linear_combination(self):
        self.assertEqual(self.vec1.linearCombination(self.vec2), 330.0, "Linear combination should be 330")
        
    def test_concat(self):
        self.assertEqual(len(self.vec1), len(self.vec1.concat(self.vec2, _return = True)) - len(self.vec2), "Vectors should be of equal length")
        
    def test_affine_prediction(self):
        self.assertEqual(self.vec3.affinePrediction([0.5, 1.1, 0.3]), 0.47900000000000004, "Affine test should match equation")
        
    def test_regression_model(self):
        self.assertEqual(round(self.vec3.affinePrediction([1.5, 0.8, 1.2])), round(self.vec3.regressionModel([1.5, 0.8, 1.2], 2) - 2), "Regression model is 2 above affine prediction/equation")
        
    def test_norm(self):
        self.assertEqual(self.vec4.norm(), 3.0, "Norm should be 3")
        
    def test_rms(self):
        self.assertEqual(round(self.vec4.rms(2)), 2, "RMS should be close to 2")
        
    def test_norm_of_sum(self):
        self.assertEqual(round(self.vec4.normOfSum(self.vec5)), 6, "Norm of sum should be close to 6")
        
    def test_distance(self):
        self.assertEqual(round(self.vec4.distance(self.vec5), 2), 3.32, "Distance should be rounded to 3.32")
        
    def test_rms_deviation(self):
        self.assertEqual(round(self.vec4.rmsDeviation(self.vec5), 2), 2.35, "RMS deviation should be rounded to 2.35")

    def test_triangle_inequality(self):
        self.assertEqual(self.vec6.triangleInequality(self.vec7, self.vec8), True, "Triangle inequality should be true")
    
    def test_standard_deviation(self):
        self.assertEqual(round(self.vec9.standardDeviation()), 2, "Standard deviation should be close to 2")
        
    def test_standardized_version(self):
        self.assertEqual(round(self.vec9.standardizedVersion(2)), 1, "Standardized version should be close to 1")
    
    def test_angle_between_vectors(self):
        self.assertEqual(round(self.vec10.angleBetweenVectors(self.vec11) / 60), 1, "Angle should be close to 1 radians")
    
    def test_inner_product_with_angle(self):
        self.assertEqual(self.vec10.innerProductWithAngle(self.vec11, 58.138953095498294, degrees = True), 5.0, "Inner product with angle should be 5")
    
    def test_norm_of_sum(self):
        self.assertEqual(round(self.vec10.normOfSum(self.vec11)), 5, "Norm of sum should be close to 5")
        
    def test_norm_of_sum_via_angles(self):
        self.assertEqual(round(self.vec10.normOfSumViaAngles(self.vec11, 58.138953095498294, degrees = True)), 5, "Norm of sum via angles should be close to 5")
        
    def test_correlation_coefficient(self):
        self.assertEqual(round(self.vec10.correlationCoefficient(self.vec11)), 1, "Correlation coefficient should be close to 1")
