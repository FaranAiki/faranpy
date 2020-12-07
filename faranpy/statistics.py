"""
	(C) Copyright 2020-2021 Muhammad Faran Aiki
	
	FaranPy module for 'statistic.py'
	
	Include
		DataStatistics			-> d
		MultipleDataStatistics	-> md
		
	This file is not for data table or something like that this file
	is for statistics, you can convert 'data.Table' into 'DataStatistics' format
	or into 'MultipleDataStatistics'
		
	Type help(object) for more information
"""

from random import randint

class DataStatistics():
	"""
		Singular data for statistics
	"""
	
	# init
	def __init__(self, sample=[], *args, **kwargs):
		""" initialize """
		if (type(sample) == dict):
			self.sample = [i*sample[i] for i in sample]
		elif (type(sample) == DataStatistics):
			self.sample = sample.sample
		else:
			self.sample = [*sample, *args] if (type(sample) in (str, list, set, tuple)) else [sample, *args]
		self.file = None
		self.repr = True
	
	# operator
	def __add__(self, data):
		if type(data) in (list, set, tuple): return DataStatistics(self.sample + list(data))
		return DataStatistics(self.sample + data.sample)
	
	# operator with equal
	def __radd__(self, data):
		if type(data) in (list, set, tuple): self.sample += list(data)
		else: self.sample += data.sample
	
	# comparison
	def __eq__(self, data):
		if (type(data) is not self): return False
		return self.sample == data.sample
	
	def __ne__(self, data):
		if (type(data) is not self): return True
		return self.sample != data.sample
	
	def __lt__(self, data):
		return sum(self.sample) < sum(data.sample)
	
	def __le__(self, data):
		return sum(self.sample) <= sum(data.sample)
	
	def __gt__(self, data):
		return sum(self.sample) > sum(data.sample)
	
	def __ge__(self, data):
		return sum(self.sample) >= sum(data.sample)
	
	# getter
	def __getitem__(self, index):
		return self.sample[index]
	
	# representation
	def __str__(self):
		return f"DataStatistics<{self.count()}>"
	
	def __repr__(self):
		if not self.repr: return self.__str__() 
		return f"""Information about the data

Mean\t\t\t: {self.mean()}
Median\t\t\t: {self.median()}
Mode\t\t\t: {self.mode()}

Variance\t\t: {self.variance()}
Deviation (Standard)\t: {self.stdev()}
Deviation (Mean)\t: {self.mdev()}

Minimum\t\t\t: {self.min()}
Maximum\t\t\t: {self.max()}
Range\t\t\t: {self.range()}"""
	
	# function	
	def min(self):
		""" get the minimum value of the data """
		return min(self.sample)
	
	def max(self):
		""" get the maximum value of the data """
		return max(self.sample)
	
	def range(self):
		""" get the range value of the data """
		return max(self.sample) - min(self.sample)
	
	def mean(self):
		""" get the mean of the data """
		return sum(self.sample)/len(self.sample)
		
	def median(self):
		""" get the median of the data """
		_sorted = sorted(self.sample)
		_len	= len(self.sample)
		return _sorted[(_len - 1)//2] if _len % 2 == 1 else (_sorted[(_len - 1)//2] + _sorted[(_len//2)])/2
	
	def mode(self):
		""" get the mode of the data """
		_set	= set(self.sample)
		_list	= [self.sample.count(i) for i in _set]
		return list(_set)[_list.index(max(_list))]
	
	def mean_deviation(self):
		""" get the mean deviation value of the data """
		_mean = sum(self.sample)/len(self.sample)
		return sum(map(lambda x: abs(x - _mean), self.sample))/len(self.sample)
	
	def standard_deviation(self):
		""" get the standard deviation value of the data """
		return self.variance()**(1/2)
	
	def variance(self):
		""" return the variance of the data """
		_mean = sum(self.sample)/len(self.sample)
		return sum(map(lambda x: (x - _mean)**2, self.sample))/(len(self.sample) - 1)
	
	def count(self, value=None):
		""" return frequency of all or the value """
		_set = list(set(self.sample))
		if value == None: return {_set[i]: self.sample.count(_set[i]) for i in range(len(_set))}
		else:
			try: return {_set[i]: self.sample.count(_set[i]) for i in range(len(_set))}[value]
			except: return 0
		
	def single(self):
		""" set all value to only appear once (each has one frequency) """
		return list(set(self.sample))
	
	def sort(self):
		""" get the sorted value of the data """
		return sorted(self.sample)
	
	def replace(self, data, *args):
		""" change the data """
		self.sample = [data, *args]
		return self.sample
		
	def random(self=None, sample=100, min=0, max=100):
		""" Generate random data using 'd().random() or d.random()' """
		return DataStatistics([randint(min, max) for i in range(sample)])
		
	def save(self, file=None):
		if file == None: file = "data.txt"
		open(file, 'w').write(self.__repr__())
	
	# only used in declaration
	def repr_as(self, repr=False):
		""" Change __repr__ function and change it into the same as __str__ """
		self.repr = repr
		return self
	
	# simplification
	mdev, dmean	= (mean_deviation,)*2
	stdev		= standard_deviation
	ndup		= (single,)*2
	frequency	= count
	var			= variance

class MultipleDataStatistics():
	"""
		Multiple data 
	"""
	def __init__(self, data=[], *args, **kwargs):
		""" initialize """
		if type(data) == dict:
			pass
		else:
			self.data = [DataStatistics(data).repr_as()]+[DataStatistics(i).repr_as() for i in args] if (type(data) in (list, set, tuple)) else [data.repr_as()]+[DataStatistics(i).repr_as() for i in args]
	
	# getter
	def __getitem__(self, index):
		return self.data[index]
	
	# representation
	def __str__(self):
		return f"MultipleDataStatistics<{self.data}>"
	
	def __repr__(self):
		return "Index\tData\n"+'\n'.join([f"[{i}]\t{self.data[i]}" for i in range(len(self.data))])

# simplification
d	= DataStatistics
md	= MultipleDataStatistics