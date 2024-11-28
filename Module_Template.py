#########################################################################################################################
#															#
#	Module Name: 			Template module
#															#
#	Creation date:			26-Nov-2024
#	Revision code:			0.0
#	Creator:			medmede7
#	Description:			this is the template for python module. It defines standards and 
#					rules to write python code and element
#															#
#########################################################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#########################################################################################################################
#					--SCRIPTING RULES--								#
#					  ---------------								#
#===============================|===============================|===============================|=======================#
#	Element			|		style		|	example			|	comment		#
#===============================|===============================|===============================|=======================#
#	Module			|	Upper_Snake_Case	|	My_Module.py		|			#
#-------------------------------|-------------------------------|-------------------------------|-----------------------#
#	Class:			|	lower_snake_case	|	class my_class		|			#
#		Attribute:	|	lowerCamelCase		|	myAttribute		|			#
#		Method:		|	UpperCamelCase		|	MyMethod		|			#
#-------------------------------|-------------------------------|-------------------------------|-----------------------#
#	Object			|	lower_snake_case	|	my_object		| same format as class	#
#-------------------------------|-------------------------------|-------------------------------|-----------------------#
#	Function:		|	UpperCamelCase		|	MyFunction		|			#
#-------------------------------|-------------------------------|-------------------------------|-----------------------#
#	Variable:		|	lowerCamelCase		|	myVar			|			#
#-------------------------------|-------------------------------|-------------------------------|-----------------------#
#	Constant:		|	ALL_UPPER_SNAKE_CASE	|	CONST_MY_CONST		|			#
#-------------------------------|-------------------------------|-------------------------------|-----------------------#
#	Global:			|	upper_snake_case	|	Global_My_Global_Var	|			#
#-------------------------------|-------------------------------|-------------------------------|-----------------------#
#	Import alias:		|	lower			|	myalias			|	avoid it	#
#===============================|===============================|===============================|=======================#
#
#########################################################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#	
#########################################################################################################################
#					-- IMPORT SECTION --								#  
#
from pathlib import Path 
#
#					-- END OF IMPORT SECTION --							#
#########################################################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#########################################################################################################################
#					-- GLOBAL SECTION --								#
#
Global_My_Global_Var = 0
#
#					-- END OF GLOBAL SECTION --
#########################################################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#########################################################################################################################					
#      					-- CLASS SECTION --								#
#															#
#	========================================================	#	
#			--CLASS my_class--				#
#	Class docString: define the class here
#	
class my_class:

#docString:
	"""
	NAME
		my_class
	SYNOPSYS
		my_object = myclass()
	DESCRIPTION
		Describe here help for the class
	AUTHOR
		name/alias
	REPORTING BUGS
		Date - bug description
	EXAMPLE
		my_object = myclass
	SEE ALSO
	
	"""
#	Attribute
# - define attribute here -
#	
# 	Constructor
	def __init__(self):
		pass
#	Method
# ' define other method here
#
#			-- END OF CLASS my_class --			#
#	========================================================	#						
#########################################################################
#															#
#					-- END OF CLASS SECTION --
#########################################################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#########################################################################################################################
#					-- SECTION CLASS TEST FUNCTION --						#
#															#
#	========================================================	#	
#			-- CLASS TEST FUNCTION my_class			#
#	Class docString: define the test function of my_class here
def TestFunction_my_class():

#docString:
	"""
	NAME
		TestFunction_my_class
	SYNOPSYS
		def TestFunction_my_class():
	DESCRIPTION
		Describe here help for the function
	AUTHOR
		name/alias
	REPORTING BUGS
		Date - bug description
	EXAMPLE
		returnValue = TestFunction_my_class()                
	SEE ALSO                                   
	"""    	                                       
#variable
#	declare your variable here	
	myVar = 0
#process

	my_object = my_class()
	if isinstance(my_object,my_class):
		return 'my_object is well created :)'
#return	
	return 'my_object is not created :('

#
#		-- END OF CLASS TEST FUNCTION my_class	--		#
#	========================================================	#	
#########################################################################
#															#
#					-- END OF SECTION CLASS TEST FUNCTION --					#
#########################################################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#########################################################################################################################
#					-- SECTION FUNCTION --								#
#															#
#	========================================================	#	
#			-- FUNCTION MyFunction --			#
#	Function  docString: define usages of the function
def MyFunction(param0, param1):

#docString:
	"""
	NAME
		MyFunction	
	SYNOPSYS
		MyFunction(param0, param1)
	DESCRIPTION
		Describe here help for the function
	AUTHOR
		name/alias
	REPORTING BUGS
		Date - bug description
	EXAMPLE
		returnValue = MyFunction(param0, param1)                
	SEE ALSO                                   
	"""                                           

#variable
#	declare your variable here
	myVar = 0
#process
	pass
# return
	return 0
#
#			--  END OF FUNCTION MyFunction --		#
#	========================================================	#	
#########################################################################
#															#
#					-- END OF SECTION FUNCTION --							#
#########################################################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#########################################################################################################################
#					-- SECTION TEST FUNCTION --							#
#															#
#	========================================================	#	
#		-- TEST FUNCTION TestMyFunction --			#
#	Test Function  docString: define usages of the test function
def TestMyFunction():

#docString:
	"""
	NAME
		TestMyFunction	
	SYNOPSYS
		TestMyFunction()
	DESCRIPTION
		Describe here help for the test function
	AUTHOR
		name/alias
	REPORTING BUGS
		Date - bug description
	EXAMPLE
		TestMyFunction()                
	SEE ALSO                                   
	"""                                       
                                                                                                                        
# Variable                                                                                                               	
#	declare your variable here                                                                                      	
	myVar = 0                                                                                                        	
#process
	if not MyFunction(1,2):
		return 'test of Myfunction is pass :)'                                                                                                        
# return
	return 'test of MyFunction is fail :(' 
#
#		--  END OF TEST FUNCTION TestMyFunction --		#
#	========================================================	#	
#########################################################################
#															#
#					-- END OF SECTION TEST FUNCTION --						#
#########################################################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#########################################################################################################################
#						-- MAIN SECTION --							#
#															#

if __name__=="__main__":
	module = Path(__file__)
	print('module ', module.name, ' start process ', __name__)
#main process
	print(TestFunction_my_class())
	print(TestMyFunction())	











#end of main process
	print('module ', module.name, ' end process ', __name__)
#															#
#						-- END OF MAIN --							#
#########################################################################################################################
