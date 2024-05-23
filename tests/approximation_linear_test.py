import unittest
import numpy as np

from approximation import linear_approximation

class Test_linear_approximation(unittest.TestCase):
    
    # список наборов x
    Xs = [np.array([1,2,3,4,5,6,7,8,9,10]), 
          np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
          np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]),
          np.array([-2, -1, 0, 1, 2, 3, 4]),
          np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])]
    
    # список наборов y
    Ys = [np.array([1,2,3,4,5,6,7,8,9,11]),
          np.array([1.5, 3.6, 4.2, 6.4, 7.0, 8.9, 10.3, 12.6, 14.2, 16.3, 18.3, 20.5, 22.3, 24.1, 26.5, 28.1, 30.2, 32.4, 35.0, 36.7]),
          np.array([0.25, 1.0, 2.25, 4.0, 6.25, 9.0, 12.25, 16.0, 20.25]),
          np.array([4, 1, 0, 1, 4, 9, 16]),
          np.array([0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100])]
    
    # список соответстующих значений первого коэффициента
    As = [1.05, 1.87, 5.0, 2.0, 10.0]
    
    # список соответстующих значений второго коэффициента
    Bs = [-0.2, -1.71, -4.58, 3.0, -15.0]
    
    # список соответстующих значений коэффициента детерминации
    Rs = [0.9929, 0.995, 0.9512, 0.5714, 0.9276]
    
    def test_linear_approximation_coefficient_a(self):
        for index in range(len(self.Xs)):
            # получение данных из функции
            a, _, _ = linear_approximation(self.Xs[index], self.Ys[index])
            self.assertAlmostEqual(self.As[index], a, 2) # проверка на соответствие значения первого коэффициента
    
    def test_linear_approximation_coefficient_b(self):
        for index in range(len(self.Xs)):
            _, b, _ = linear_approximation(self.Xs[index], self.Ys[index])
            self.assertAlmostEqual(self.Bs[index], b, 2) # проверка на соответствие значения второго коэффициента
            
    def test_linear_approximation_coefficient_r(self):
        for index in range(len(self.Xs)):
            _, _, r = linear_approximation(self.Xs[index], self.Ys[index])
            self.assertAlmostEqual(self.Rs[index], r, 4) # проверка на соответствие значения коэффициента детерминации

if __name__ == '__main__':
    unittest.main()
        
