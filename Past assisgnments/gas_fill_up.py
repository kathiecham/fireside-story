class Car:
# created a class called Car

	def __init__(self, gas_level):
		self.gas_level = gas_level
	
# This function will run when I create an instance
# Create an instance when I name it and provide parameter 1 of the 2 parameters.
# first parameter is self, second one is the amount of gas the car currently has
# for this class: example_car = Car(10) which is in the main function
# set parameter "gas_level" to self.gas_level = gas_level. Not sure why. I don't understand.

# Now for the function that indicates
# 1 - If I need to fill up or not - if 13 or higher already full
# 2 - If I do need to fill up .. how much is needed.
	def fill_up(self):
		#self needs no data, 
		# how is parameter gas_level passed from _init_
		#is amt passed as an integer or do I need to change?
		#if the amount of gas is 13 or more, then (new variable) pump is set to 0
		# return pump (which is 0)
		# by using return pump - the value of pump should be available globally.
		# I should be able to print pump from the main function since it is a global variable
		if self.gas_level >= 13:
			return 0
		else:
			pump = 13.0 - float(self.gas_level)
			return pump
		# using else since what is left is a car that needs gae.
		# then (new variable) pump is calculated by subtracting the amt parameter from 13.
		# by using return pump - the value of pump should be available globally.
		# I should be able to print pump from the main function since it is a global variable
		
			
def main():
	example_car = Car(13)
	#how am I calling fill_up
	#name of instance (dot) function (parameters)
	# do I need to put in new parameters or will they pass when the Car class function is initalized.
	print(example_car.fill_up())


if __name__ == "__main__":
    main()