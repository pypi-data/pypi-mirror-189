import numpy as np
from sympy import *
import matplotlib.pyplot as plt

class SGD_NP:
    def __init__(self, vector, formula, variables, learningRate):
        self.array = vector
        self.formula = formula
        self.variables = variables
        self.learningRate = learningRate
    
    def start(self, display = True):
        array, plot_values = self.gradientDescent()
        if display: 
            t = [x[0] for x in plot_values]
            z = [x[1] for x in plot_values]

            plt.plot(t, z, 'r', t, z, 'b^')

            plt.xlim([max(t), min(t)])
            plt.ylim([min(z), max(z)])
        else:
            return array.tolist()
        
    def gradientFunction(self, option, equation, variables):
        if option == "derivative":
            return diff(equation, *variables)
        else:
            return equation

    def gradient(self, equation, variables, option):
        derivedEquation = self.gradientFunction(option, equation, variables)
        return lambdify(*variables, derivedEquation, "numpy"), derivedEquation

    def gradientDescent(self, option="derivative", numIterations=50, tolerance=1e-06):
        array = self.array
        original = lambdify(*self.variables, self.formula, "numpy")
        f, derivedEquation = self.gradient(self.formula, self.variables, option)
        plot_values = []
        for _ in range(numIterations):
            plot_values.append((array[0], original(array)[0]))
            diff = -1 * self.learningRate * f(array)
            if np.all(np.abs(diff) <= tolerance):
                break
            array = np.add(array, diff)
        return array, plot_values
