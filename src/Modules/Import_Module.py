from pathlib import Path
import importlib.util

def Import():

	modules_dict={key:importlib.util.spec_from_file_location(

	key, str(Path(__file__).parent)+'/'+key+'.py'

		) for key in 

	['Get_File_Map','Exist_https','Log_info']

	}# ['Module_1','Module_2','Module_3'] : list name main modules


	for key in modules_dict:

		for_activate=importlib.util.module_from_spec(modules_dict[key])

		spec=modules_dict[key]

		spec.loader.exec_module(for_activate)

		modules_dict[key]=for_activate


	return modules_dict