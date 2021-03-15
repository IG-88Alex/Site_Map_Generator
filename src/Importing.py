import re
import os 
from pathlib import Path
import importlib.util	


def Import(Main_Program):

	#Wrapper-function, import decorator.
	def imported():

		modules_dict={key:importlib.util.spec_from_file_location(

		key, str(Path(__file__).parent)+'/Modules/'+key+'.py'

		) for key in 

		['Search','Graph','Input','Results','Welcome']

		}


		for key in modules_dict:

			for_activate=importlib.util.module_from_spec(modules_dict[key])

			spec=modules_dict[key]

			spec.loader.exec_module(for_activate)

			modules_dict[key]=for_activate
		
		return modules_dict

	'''
	→  Main wrappable function.
	Calling the main branch of the program. ←'''
	Main_Program(imported())

	'''
	Return the wrapper-function, 
	in accordance with the rules for creating decorators.'''
	return imported
