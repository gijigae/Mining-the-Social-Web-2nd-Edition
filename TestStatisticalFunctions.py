import unittest

class TestStatisticalFunctions(unittest.TestCase):

	def average(values, precision):
	    """ Computes the arithmetic mean of a list of numbers.
	    >>> average([20, 30, 70])
	    40
	    """
	    return sum(values, precision) / len(values)


	def test_average(self):
		self.assertEqual(self.average([20, 30, 70]), 40)
		self.assertEqual(round(self.average([1, 5, 7]), 1), 4.3)
		with self.assertRaises(ZeroDivisionError):
			self.average([])
		with self.assertRaises(TypeError):
			self.average(20, 30, 70)

unittest.main() # Calling from the command line invokes all tests