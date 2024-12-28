import unittest

from main import generate_factorials

class TestGenerateFactorials(unittest.TestCase):

    def test_generate_factorials_valid(self):
        self.assertEqual(generate_factorials(1), [1])
        self.assertEqual(generate_factorials(3), [1, 2, 6])
        self.assertEqual(generate_factorials(5), [1, 2, 6, 24, 120])

    def test_generate_factorials_edge_cases(self):
        self.assertEqual(generate_factorials(2), [1, 2])
        self.assertEqual(generate_factorials(10), [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800])

    def test_generate_factorials_invalid(self):
        # Тестируем некорректные входные данные
        with self.assertRaises(ValueError):
            generate_factorials(0)  # n должно быть >= 1
        with self.assertRaises(ValueError):
            generate_factorials(-5)  # n должно быть >= 1
        with self.assertRaises(ValueError):
            generate_factorials("abc")  # n должно быть целым числом
        with self.assertRaises(ValueError):
            generate_factorials(3.5)  # n должно быть целым числом

if __name__ == "__main__":
    unittest.main()
