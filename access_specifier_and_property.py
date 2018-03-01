import sys

#understanding get_tempters and set_tempters in python

#Create a basic class for the temperature 
#Basic Class   Temp 1.0

class Temp:

	def __init__(self,temp=0):
		self.temp=temp;

	def convert(self):
		return (self.temp*1.8+32.0)

#change the class with few modifications 
# Class Temp 1.1 

class Temp1 :
	
	def __init__(self,temp=0):
		self.set_temp(temp)
	
	def convert(self):
		return(self.get_temp()*1.8+32.0)

	#new updates
	#get_tempter and set_tempter way
	def get_temp(self):
		print ("get_temp the value")
		return self.__temp

	def set_temp(self,temp):
		if temp<0:
			raise  ValueError("Temp is less < 0");
		else :
			self.__temp=temp;
			print ("set_temp the value")

#pythonic way to use get_temp and set_temp function using 
#@property in classes

# class Temp2 

class Temp2:
	
	def __init__(self,temp=0):
		self.temp=temp;

	def convert(self):
		return(self.temp*1.8+32)

	def get_temp(self):
		print ("get_temp the temperature")
		return self.__temp
	
	def set_temp(self,temp):
		print ("set_temp the temperature")
		if temp<0:
			raise ValueError("can't be negative")
		else:
			self.__temp=temp
	def del_temp(self):
		del self.__temp

##defining the property of temperature by oroperty(fget,fset,fdel,doc)

	temp=property(get_temp,set_temp,del_temp,"property of temp")

##class Temp3.0 using decorator for class property

class Temp3:
	def __init__(self,temp=0):
		self.temp=temp;

	def convert(self):
		return(self.temp*1.8+32)

	@property
	def temp(self):
		##doc is writter here
		"this is the doc of property"
		return self.__temp
	@temp.setter
	def temp(self,x):
		if temp<0:
			raise ValueError("negative value not allowed")
		print ("Value is set")
		self.__temp=x
	@temp.deleter
	def temp(self):
		del self.__temp;

	




## main function

if __name__=="__main__":

	##class Temp3
	print ("Class Temp3 ")
	t=Temp3()
	t.temp=59
	t.convert()
	

	#class Temp2

	print ("Class Temperature 2")

	t=Temp2(1)
	print (t.convert())

	#class Temp1

	print ("Class Temperature 1")

	t=Temp1(45)
	print(t.convert())
	t.get_temp()

	#raise value error

	#t=Temp1(-12)
	#t=Temp()

	##accessing private variables
	t=Temp1()
	t._Temp1__temp=300
	t.get_temp()
	t.temp=45;
	print (t.convert())

	#class Temp
	print ("Class Temperature 1")
	t=Temp(45)
	print (t.convert())

