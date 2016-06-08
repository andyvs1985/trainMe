# This program is for reading the data from excel sheet and serilization through JSON

# What DATA are ?
# What are the program variable to store the value in DATA
# what are the program statements to manipulate the DATA.

# DATA : excel files with records
# variable : excel_file

# Imports
import os, xlrd, json

class Reader:
	"""This is the reader class to read the data"""

	def __init__(self):
		""" """

	def excel_dict_reader(self):
		import pdb; pdb.set_trace()
		currentPath = os.getcwd()
		csv_file = os.path.join(currentPath, "untitle.xls")
		try:
			reader = xlrd.open_workbook(csv_file)
			for line in reader:
				json_string = json.dumps(line)

		except Exception, e:
			raise
		else:
			pass
		finally:
			pass




# instance of a class Reader
my_obj = Reader() # Constructor
my_obj.excel_dict_reader()

