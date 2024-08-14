import io
import unittest.mock
import ada as ex1
import earth as ex2
import change as ex3


class TP2TestCases(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_ada(self, mock_stdout):
        ex1.ada()
        results = mock_stdout.getvalue().splitlines()
        self.assertEqual(results[0], "ada lovelace")
        self.assertEqual(results[1], "Ada Lovelace")
        self.assertEqual(results[2], "ADA LOVELACE")
        self.assertEqual(results[3], "\tada lovelace")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_earth(self, mock_stdout):
        ex2.earth()
        results = mock_stdout.getvalue().splitlines()
        self.assertEqual(results[0], "The result of Bangladesh comes first in the dictionary than Barbados is True.")
        self.assertEqual(results[1], "The result of Barbados comes first in the dictionary than Bangladesh is False.")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_change(self, mock_stdout):
        ex3.change()
        results = mock_stdout.getvalue().splitlines()
        self.assertEqual(results[0], "Ingresar gasto:")
        self.assertEqual(results[1], "23.75")
        self.assertEqual(results[2], "Dinero recibido")
        self.assertEqual(results[3], "100")
        self.assertEqual(results[4], "")
        self.assertEqual(results[5], "Vuelto")
        self.assertEqual(results[6], "")
        self.assertEqual(results[7], "Pesos:")
        self.assertEqual(results[8], "76")
        self.assertEqual(results[9], "Centavos:")
        self.assertEqual(results[10], "25")


if __name__ == '__main__':
    unittest.main()
