# A program to calculate an individual gross pay.

# How : Gross pay equals to hourly pay rate times number of hourly worked.

# Example:
# Hourly pay rate = Rs.100
# Number of hours worked = 35 hours

# Calculation :
# Gross Pay = hourly pay rate * hours worked.
# So Gross pay = 100 times 35 => Rs.3500

# What we need to Decide :
# => what the DATA is ?
# => what are the program variable to store DATA values?
# => what are the program statements to perform/calculate?

class GrossPay:
	"""This is the GrossPay class object"""

	def __init__(self, hourly_pay_rate, hours_worked):
		"""Docsrting"""
		self.hourly_pay_rate = hourly_pay_rate
		self.hours_worked = 

	def calculate_gross_pay(self):
		"""This method witll calculate the Gross pay"""
		gross_pay = self.hourly_pay_rate * self.hours_worked
		return gross_pay

# Lets create an instance of a class GrossPay
my_instance_1 = GrossPay(35,100)
total = my_instance_1.calculate_gross_pay()
print total





