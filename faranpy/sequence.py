"""
	(C) Copyright 2020-2021 Muhammad Faran Aiki
	
	FaranPy module for 'sequence.py'
	
	Include
		BasicSequence
		ArithmeticSequence	-> ars
		GeometricSequence	-> grs
	
	Type help(object) for more information
"""

from faranpy.statistics import DataStatistics

class BasicSequence():
	"""
		Basic class for sequence
	"""
	def sequence_sample(self, n):
		return DataStatistics(self.sequence(n))
		
	data, sample	= (sequence_sample,)*2

class ArithmeticSequence(BasicSequence):
	"""
		Arithmetic Sequence
	"""
	
	# init
	def __init__(self, a=1, b=1, *args, **kwargs):
		""" Initialization """
		self.a		= a
		self.b		= b
		self.args	= args
		self.kwargs	= kwargs
	
	# get
	def __getitem__(self, n):
		""" get item equivalent term(n - 1) with respect to n """
		return (self.a + self.b * (n - 2))
	
	# representation
	def __str__(self):
		return f"ArithmeticSequence<a={self.a}, b={self.a}, {self.args}, {self.kwargs}>"
	
	def __repr__(self):
		return f"ArithmeticSequence<a={self.a}, b={self.a}, {self.args}, {self.kwargs}>"
	
	# function
	def term(self, n):
		""" return the term using the formula with respect to n """
		return self[n+1]
	
	def sum(self, n):
		""" return the sum using the formula with respect to n """
		return (self.a + self.term(n))*(n/2)
	
	def sequence(self, n):
		""" return the sequence with respect to n """
		return [self.term(i) for i in range(1, n+1)]
	
	def t_formula(self):
		""" return the formula for term """
		return f"{self.a} + {self.b} * (n - 1)"
	
	def s_formula(self):
		""" return the formula for sum """
		return f"({2*self.a} + {self.b} * (n - 1)) * (n / 2)"
	
	#simplification
	seq		= sequence
	t_form	= t_formula
	s_form	= s_formula

class GeometricSequence(BasicSequence):
	"""
		Geometric Sequence
	"""
	
	# init
	def __init__(self, a=1, r=2, *args, **kwargs):
		""" Initialization """
		self.a		= a
		self.r		= r
		self.args	= args
		self.kwargs	= kwargs
	
	# get
	def __getitem__(self, n):
		""" get item equivalent term(n - 1) with respect to n """
		return self.a * self.r ** (n)
	
	# representation
	def __str__(self):
		return f"GeometricSequence<a={self.a}, r={self.a}, {self.args}, {self.kwargs}>"
	
	def __repr__(self):
		return f"GeometricSequence<a={self.a}, r={self.r}, {self.args}, {self.kwargs}>"
	
	# function
	def term(self, n):
		""" return the term using the formula with respect to n """
		return self[n+1]
	
	def sum(self, n):
		""" return the sum using the formula with respect to n """
		return self.a*(self.r**n - 1)/(self.r - 1)
	
	def sequence(self, n):
		""" return the sequence with respect to n """
		return [self.term(i) for i in range(1, n+1)]
	
	def t_formula(self):
		""" return the formula for term """
		return f"{self.a} * {self.r} ** (n)"
	
	def s_formula(self):
		""" return the formula for sum """
		return f"{self.a} * ({self.r}**n - 1) / ({self.r} - 1)"
	
	# simplification
	seq		= sequence
	t_form	= t_formula
	s_form	= s_formula

# simplification
ars	= ArithmeticSequence
grs	= GeometricSequence