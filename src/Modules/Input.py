import requests
import sys
import re, os
import tkinter as tk
from tkinter import filedialog
from itertools import chain, combinations
from urllib.parse import urlparse
from urllib.parse import unquote, unquote_plus

def Input(): 

	try:


		VALUE=str(input('\n\n\033[38;5;51mEnter your url \033[38;5;46m>\033[38;5;226m  ')) #--------Data entry

		print('\033[0m')

		List_params_1= re.split(r'(\s+)',VALUE) 

		URL = None

		Proof = [] # List for proving that there are no more than 1 links.


		for url in List_params_1:#Selecting links using a regular expression.

			list_url = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',url)

			if bool(list_url):

				Proof.append(list_url[0])

				URL = url


		if len(Proof) == 1:# Permutation with url and element
						   # for later use in the mechanism.
			List_params_1[List_params_1.index(URL) ],List_params_1[0] = List_params_1[0],List_params_1[List_params_1.index(URL)]

		if len(Proof) != 1:

			print('\n\033[38;5;196mInvalid data entered.\033[0m')

			sys.exit(0)


		Base_URL= str('{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(List_params_1[0])))#Getting_the_root_URL.

		response = requests.head(List_params_1[0]) #Request to check the validity of the link.

		Dict_values = {}#Main dictionary.


		if re.findall(r'..$',Base_URL)[0][0] != '\\' and re.findall(r'..$',Base_URL)[0][1] != '\\' and response.status_code != 404 :#Checking for a backslash
																																	#at the end of the root url.
			Dict_values['url'] = Base_URL																									

		else:

			print('\n\033[38;5;196mYou may have used at the end of the root url \033[37m[\033[38;5;196m\\\033[37m]\033[38;5;196m instead \033[37m[\033[38;5;46m/\033[37m]\033[38;5;196m.\033[0m')

			print('\n\033[38;5;196mThis page may not exist <Response [404]>.\033[0m')

			sys.exit(0)



		Dict_values['Path'] = None

		Path = [] # List to add found directories.

		Del_Path_combination = [] 

																														#       Lists_combinations
							                                                                                            #---------------------------------
		All_combinations = chain(*map(lambda x: combinations(List_params_1[1:], x), range(0, len(List_params_1[1:])+1)))# All possible combinations of data
																													    # entered by the user to
																													    # check for the directory name.

		for subset in All_combinations:		

			A = ''.join(subset) #Convert each combination as a list back to a 
								#readable string to find the directory.

			if os.path.isdir(A) and A[-1] != ' ' and A not in Path:

				Path.append(A)

				Del_Path_combination.append(subset) # Append_to_list_elements_for_next_deleted.


		if len(Path) == 1:# If there are no more than two directories,
						  # add them to the dictionary.

			if re.findall(r'..$',Path[0])[0] != '//' and re.findall(r'..$',Path[0])[0] != '\\\\' and \
			re.findall(r'..$',Path[0])[0] != '/\\' and re.findall(r'..$',Path[0])[0] != '\\/':

				Dict_values['Path'] = Path[0].replace('\\', '/')

				for i in Del_Path_combination[0]:

					List_params_1.remove(i)



		elif len(Path) > 1: # If there is more than one directory,
							# you will get an error.


			print('\n\033[38;5;196mInvalid data entered.\033[0m')

			print('\n\033[38;5;196mYou may have entered the names of two directories.\033[0m')

			sys.exit(0)

		

		List_params_1.remove(str(List_params_1[0])) # Remove the found link from the list of entered data.

		List_prms = list(List_params_1)

		[List_prms.remove(i) for i in List_params_1 if i.isspace() or i == '']



		#----------------------------------------------------------------------------


		if len(List_prms) == 1 and bool(List_prms) and List_prms[0] == '-g':

			Dict_values['-g'] = 'graph'

			List_prms.remove('-g')



		if len(List_prms) == 1 and bool(List_prms) and '-p' in List_prms and Dict_values['Path'] == None:

			root = tk.Tk()

			root.update()#################

			root.withdraw()

			directory_path = filedialog.askdirectory()

			root.quit()########################################

			root.destroy()#############################################################

			

			if directory_path!= '' and not directory_path.isspace() and bool(directory_path) != False:

				Dict_values['Path'] = directory_path.replace('\\', '/')


			List_prms.remove('-p')



		if len(List_prms) == 1 and List_prms[0] == '-p' and Dict_values['Path'] != None:

			print('\n\033[38;5;196mInvalid data entered.\033[0m')

			print("\n\033[38;5;196mYou can't simultaneously call the graphical window dialog \033[38;5;51mWindows \
				Explorer\033[38;5;196m (\033[38;5;46m-p\033[38;5;196m) and write the directory name.\n\033[0m")



		if len(List_prms) == 2 and '-p' in List_prms and '-g' in List_prms and Dict_values['Path'] == None:


			Dict_values['-g'] = 'graph'

			List_prms.remove('-g')

			List_prms.remove('-p')

			root = tk.Tk()

			root.update()#################

			root.withdraw()

			directory_path = filedialog.askdirectory()

			root.quit()########################################

			root.destroy()#############################################################


			if directory_path!= '' and not directory_path.isspace() and bool(directory_path) != False:

				Dict_values['Path'] = directory_path.replace('\\', '/')



		elif len(List_prms) == 2 and '-p' in List_prms and '-g' in List_prms and Dict_values['Path'] != None:


			print('\n\033[38;5;196mInvalid data entered.\033[0m')

			print("\n\033[38;5;196mYou can't simultaneously call the graphical window dialog \033[38;5;51mWindows \
				Explorer\033[38;5;196m (\033[38;5;46m-p\033[38;5;196m) and write the directory name.\n\033[0m")

			sys.exit(0)

		



		if len(List_prms) >= 1 and Dict_values['Path'] == None: 

			print('\n\033[38;5;196mInvalid data entered.\033[0m')

			sys.exit(0)



		if len(List_prms) >= 1 and Dict_values['Path'] != None and '-p' not in List_prms:

			print('\n\033[38;5;196mInvalid data entered.\033[0m')

			sys.exit(0)



		if len(List_prms) == 0: # Main___save_dict__in__Input()

			return Dict_values  



	except KeyboardInterrupt:

		print('\033[0m')

		print('\n\n\033[31mProgram exit.\033[0m')

		sys.exit(0)


	except SystemExit:

		sys.exit(0)


	except:

		print('\n\033[38;5;196mInvalid data entered.\033[0m')

		sys.exit(0)