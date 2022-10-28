import unittest
import python_code

class TestPythonCode(unittest.TestCase):

    def test_summa_one (self):
        self.assertEqual(python_code.summa(23), 5, "при сложении двухначного числа 23 получается 5")

    def test_summa_two (self):
        self.assertEqual(python_code.summa(234), 9, "при сложении трёхначного числа 234 получается 9")

    def test_summa_three (self):
        self.assertEqual(python_code.summa(0), 0, "при введении параметра 0 получается 0")
        
    def test_summa_four (self):
        self.assertRaises(TypeError, python_code, "4")

    def test_summa_five (self):
        self.assertRaises(TypeError, python_code, -5)
    
    def test_summa_six (self):
        self.assertRaises(TypeError, python_code, 2.5)

if __name__ == '__main__':
    unittest.main()