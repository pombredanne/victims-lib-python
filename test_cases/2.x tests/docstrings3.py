"""This is a docstring. Sometimes they get referenced by code..
referenced strings like this one should not be deleted"""

class testobject:
	def __init__(self):
		print "hello world"

if __name__ == '__main__':
	print __doc__
	testobject()
	