#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import unittest

from exercice import *


class TestExercice(unittest.TestCase):
	def setUp(self):
		pass

	def test_dissipated_power(self):
		data = [(69, 420),
		        (42, 9000)]
		expected = [1_999_620,
		            15_876_000]
		output = [dissipated_power(d[0], d[1]) for d in data]
		self.assertEqual(
			expected,
			output,
			"Calcul incorrect"
		)

	def test_orthogonal(self):
		data = [((1, 1), (-1, 1)),
		        ((0, 0), (1, 1)),
		        ((0, 0), (0, 0)),
		        ((1, 1), (1, 1)),
		        ((-1, -1), (1, 1))]
		expected = [True,
		            True,
		            True,
		            False,
		            False]
		output = [orthogonal(d[0], d[1]) for d in data]
		self.assertEqual(
			expected,
			output,
			"Calcul incorrect"
		)
	
	def test_average(self):
		data = [[1, 4, -2, 10],
		        [1, 4, -1, 10, 0],
		        [-12, -42, 1],
		        [0xDEAD, 0xBEEF, 420, 69]]
		expected = [5.0,
		            3.75,
		            1.0,
		            26593.25]
		output = [average(d) for d in data]
		self.assertEqual(
			expected,
			output,
			"Calcul incorrect"
		)

	def test_bills(self):
		data = [0,
		        1,
		        5,
		        10,
		        20,
		        420,
		        69,
		        137,
		        0xBABE]
		expected = [(0, 0, 0, 0),
		            (0, 0, 0, 1),
		            (0, 0, 1, 0),
		            (0, 1, 0, 0),
		            (1, 0, 0, 0),
		            (21, 0, 0, 0),
		            (3, 0, 1, 4),
		            (6, 1, 1, 2),
		            (2390, 0, 1, 1)]
		output = [bills(d) for d in data]
		self.assertEqual(
			expected,
			output,
			"Calcul incorrect"
		)
		


if __name__ == "__main__":
	if not os.path.exists("logs"):
		os.mkdir("logs")
	with open("logs/tests_results.txt", "w") as f:
		loader = unittest.TestLoader()
		suite = loader.loadTestsFromModule(sys.modules[__name__])
		unittest.TextTestRunner(f, verbosity=2).run(suite)
	# Pour mettre le résultat du log dans la console (plus pratique).
	print(open("logs/tests_results.txt", "r").read())
