import unittest
import pandas as pd
from UP02.UP02 import dynamic_series_calculations

class TestDynamicSeriesCalculations_NormalValuesWithDivision(unittest.TestCase):
    def setUp(self):
        self.years = [2010, 2011, 2012, 2013]
        self.values = [100, 110, 121, 133.1]

    def test_dynamic_series_calculations_output_shape(self):
        df, y, delta_y, T = dynamic_series_calculations(self.years, self.values)
        self.assertEqual(df.shape, (len(self.years)-1, 7))

    def test_dynamic_series_calculations_correctness(self):
        df, avg_y, avg_dy, avg_t = dynamic_series_calculations(self.years, self.values)

        expected_df = pd.DataFrame({
            'год': [2010, 2011, 2012, 2013],
            'Δy<sub>бi</sub>': [None, 10.0, 21.0, 33.1],
            'Δy<sub>цi</sub>': [0.0, 10.0, 11.0, 12.1],
            'T<sub>Пбi</sub>': [None, 10.0, 21.0, 33.1],
            'T<sub>Пцi</sub>': [0.0, 10.0, 10.0, 10.0],
            'T<sub>Рбi</sub>': [None, 1.1, 1.21, 1.331],
            'T<sub>Рцi</sub>': [0.0, 1.1, 1.1, 1.1],
        })
        expected_df = expected_df.drop(0)
        expected_avg_y = 116.03
        expected_avg_dy = 11.03
        expected_avg_t = 1.1

        pd.testing.assert_frame_equal(df, expected_df)
        self.assertEqual(round(avg_y, 2), expected_avg_y)
        self.assertEqual(round(avg_dy, 2), expected_avg_dy)
        self.assertEqual(round(avg_t, 1), expected_avg_t)


class TestDynamicSeriesCalculations_SameValues(unittest.TestCase):
    def setUp(self):
        self.years = [0, 1, 2, 3]
        self.values = [1, 1, 1, 1]

    def test_dynamic_series_calculations_correctness(self):
        df, avg_y, avg_dy, avg_t = dynamic_series_calculations(self.years, self.values)

        expected_df = pd.DataFrame({
            'год': [0, 1, 2, 3],
            'Δy<sub>бi</sub>': [None, 0, 0, 0],
            'Δy<sub>цi</sub>': [0.0, 0, 0, 0],
            'T<sub>Пбi</sub>': [None, 0, 0, 0],
            'T<sub>Пцi</sub>': [0.0, 0, 0, 0],
            'T<sub>Рбi</sub>': [None,1,1 ,1],
            'T<sub>Рцi</sub>': [0.0, 1, 1, 1],
        })
        expected_df = expected_df.drop(0)
        expected_avg_y = 1
        expected_avg_dy = 0
        expected_avg_t = 1

        df = df.astype(int)
        expected_df = expected_df.astype(int)


        pd.testing.assert_frame_equal(df, expected_df)
        self.assertEqual(round(avg_y, 2), expected_avg_y)
        self.assertEqual(round(avg_dy, 2), expected_avg_dy)
        self.assertEqual(round(avg_t, 1), expected_avg_t)

class TestDynamicSeriesCalculations_NormalValues1(unittest.TestCase):
    def setUp(self):
        self.years = [1, 2, 3, 4,5,6]
        self.values = [1, 2, 3, 4,5,6]

    def test_dynamic_series_calculations_correctness(self):
        df, avg_y, avg_dy, avg_t = dynamic_series_calculations(self.years, self.values)

        expected_df = pd.DataFrame({
            'год': [1, 2, 3, 4,5,6],
            'Δy<sub>бi</sub>': [None, 1, 2,3,4,5],
            'Δy<sub>цi</sub>': [0.0, 1, 1, 1,1,1],
            'T<sub>Пбi</sub>': [None, 100, 200, 300,400,500],
            'T<sub>Пцi</sub>': [0.0, 100, 50, 33.3333,25,20],
            'T<sub>Рбi</sub>': [None,2,3 ,4,5,6],
            'T<sub>Рцi</sub>': [0.0, 2, 1.5, 1.3333,1.25,1.2],
        })
        expected_df = expected_df.drop(0)
        expected_avg_y = 3.5
        expected_avg_dy = 1.0
        expected_avg_t = 1.3

        df = df.astype(float)
        expected_df = expected_df.astype(float)
        pd.testing.assert_frame_equal(df, expected_df)
        self.assertEqual(round(avg_y, 2), expected_avg_y)
        self.assertEqual(round(avg_dy, 2), expected_avg_dy)
        self.assertEqual(round(avg_t, 1), expected_avg_t)


class TestDynamicSeriesCalculations_NormalValues2(unittest.TestCase):
    def setUp(self):
        self.years = [2018, 2019, 2020, 2021,2022]
        self.values = [1, 10, 30, 5,25]

    def test_dynamic_series_calculations_correctness(self):
        df, avg_y, avg_dy, avg_t = dynamic_series_calculations(self.years, self.values)

        expected_df = pd.DataFrame({
            'год': [2018, 2019, 2020, 2021,2022],
            'Δy<sub>бi</sub>': [None, 9, 29,4,24],
            'Δy<sub>цi</sub>': [0.0, 9, 20, -25,20],
            'T<sub>Пбi</sub>': [None, 900, 2900, 400,2400],
            'T<sub>Пцi</sub>': [0.0, 900, 200, -83.3333,400],
            'T<sub>Рбi</sub>': [None,10,30,5,25],
            'T<sub>Рцi</sub>': [0.0, 10, 3, 0.1667,5],
        })
        expected_df = expected_df.drop(0)
        expected_avg_y = 14.2
        expected_avg_dy = 6.0
        expected_avg_t = 1.9

        df = df.astype(float)
        expected_df = expected_df.astype(float)
        pd.testing.assert_frame_equal(df, expected_df)
        self.assertEqual(round(avg_y, 2), expected_avg_y)
        self.assertEqual(round(avg_dy, 2), expected_avg_dy)
        self.assertEqual(round(avg_t, 1), expected_avg_t)

class TestDynamicSeriesCalculations_NegativeValues(unittest.TestCase):
    def setUp(self):
        self.years = [1, 2, 3, 4, 5]
        self.values = [1, -30, 20, -45, 25]

    def test_dynamic_series_calculations_correctness(self):
        df, avg_y, avg_dy, avg_t = dynamic_series_calculations(self.years, self.values)

        expected_df = pd.DataFrame({
            'год': [1, 2, 3, 4, 5],
                'Δy<sub>бi</sub>': [None, -31, 19, -46, 24],
                'Δy<sub>цi</sub>': [0.0, -31, 50, -65, 70],
                'T<sub>Пбi</sub>': [None, -3100, 1900, -4600, 2400],
                'T<sub>Пцi</sub>': [0.0, -3100, -166.6667, -325, -155.5556],
                'T<sub>Рбi</sub>': [None, -30, 20, -45, 25],
                'T<sub>Рцi</sub>': [0.0, -30, -0.6667, -2.25, -0.5556],
            })
        expected_df = expected_df.drop(0)
        expected_avg_y = -5.8
        expected_avg_dy = 6.0
        expected_avg_t = 1.9

        df = df.astype(float)
        expected_df = expected_df.astype(float)
        pd.testing.assert_frame_equal(df, expected_df)
        self.assertEqual(round(avg_y, 2), expected_avg_y)
        self.assertEqual(round(avg_dy, 2), expected_avg_dy)
        self.assertEqual(round(avg_t, 1), expected_avg_t)
        
        
        
class TestDynamicSeriesCalculations_AbnormalValues(unittest.TestCase):
    def setUp(self):
        self.years = ["a", "a", "a", "a", "a"]
        self.values = ["b", "B","b", "B", "B"]

    def test_dynamic_series_calculations_correctness(self):
        try:
            df, avg_y, avg_dy, avg_t = dynamic_series_calculations(self.years, self.values)

            expected_df = pd.DataFrame({
                'год': [],
                    'Δy<sub>бi</sub>': [None, 0, 0, 0, 0],
                    'Δy<sub>цi</sub>': [0.0, 0, 0, 0, 0],
                    'T<sub>Пбi</sub>': [None, 0, 0, 0, 0],
                    'T<sub>Пцi</sub>': [0.0, 0, 0, 0, 0],
                    'T<sub>Рбi</sub>': [None, 0, 0, 0, 0],
                    'T<sub>Рцi</sub>': [0.0, 0, 0, 0, 0],
                })
            expected_df = expected_df.drop(0)
            expected_avg_y = 0
            expected_avg_dy = 0
            expected_avg_t = 0

            df = df.astype(float)
            expected_df = expected_df.astype(float)
            pd.testing.ass_frame_equal(df, expected_df)
            self.assertNotEqual(round(avg_y, 2), expected_avg_y)
            self.assertNotEqual(round(avg_dy, 2), expected_avg_dy)
            self.assertNotEqual(round(avg_t, 1), expected_avg_t)
        except Exception:
            print(f"Некорректный ввод данных")
            
            
            
class TestDynamicSeriesCalculations_EmptyValues(unittest.TestCase):
    def setUp(self):
        self.years = []
        self.values = []

    def test_dynamic_series_calculations_correctness(self):
        try:
            df, avg_y, avg_dy, avg_t = dynamic_series_calculations(self.years, self.values)

            expected_df = pd.DataFrame({
                'год': [],
                    'Δy<sub>бi</sub>': [None, 0, 0, 0, 0],
                    'Δy<sub>цi</sub>': [0.0, 0, 0, 0, 0],
                    'T<sub>Пбi</sub>': [None, 0, 0, 0, 0],
                    'T<sub>Пцi</sub>': [0.0, 0, 0, 0, 0],
                    'T<sub>Рбi</sub>': [None, 0, 0, 0, 0],
                    'T<sub>Рцi</sub>': [0.0, 0, 0, 0, 0],
                })
            expected_df = expected_df.drop(0)
            expected_avg_y = 0
            expected_avg_dy = 0
            expected_avg_t = 0

            df = df.astype(float)
            expected_df = expected_df.astype(float)
            pd.testing.ass_frame_equal(df, expected_df)
            self.assertNotEqual(round(avg_y, 2), expected_avg_y)
            self.assertNotEqual(round(avg_dy, 2), expected_avg_dy)
            self.assertNotEqual(round(avg_t, 1), expected_avg_t)
        except Exception as e:
            print(f"Некорректный ввод данных")
            print(f"{e}")
            
            

if __name__ == '__main__':
    unittest.main()