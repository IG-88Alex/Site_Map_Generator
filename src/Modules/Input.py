import sys
import re, os
import requests
import platform
import itertools
import tkinter as tk
from tkinter import filedialog
from itertools import chain, combinations
from urllib.parse import urlparse
from urllib.parse import unquote, unquote_plus


def Input(): 

	try:

		#The data that the user entered.
		VALUE=str(

			input('\n\n\033[38;5;51mEnter your url \033[38;5;46m>\033[38;5;226m  ')

			)

		#Returns the console text color to the original default.
		print('\033[0m')

		'''Splits a string by spaces, forming a list based on the data entered by the user.
		
		Example:
		Enter your url > https://www.google.com/ C:/Users/Administrator/Desktop -g
		List_params_1 = ['https://www.google.com/', 'C:/Users/Administrator/Desktop', '-g']'''
		List_params_1= re.findall(r'(\S+)',VALUE)

		#List for proving that there are no more than 1 links.
		Proof = []

		#Selecting links using a regular expression.
		for url in List_params_1:

			'''Checks whether the link domain name consists of only Latin letters.'''
			list_url = re.findall(

				r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url

				)

			if bool(list_url):

				Proof.append(list_url[0])

				URL = url

		'''Permutation with url and element for later use in the mechanism.'''

		#if bool(url) = True
		if len(Proof) == 1:

			#List_params_1 = [elem,...,url] → permutation ←  [url,...,elem] ¬ [url,...,elem]
			List_params_1[List_params_1.index(URL) ],List_params_1[0] = List_params_1[0],List_params_1[List_params_1.index(URL)]

		#if bool(url) = False
		if len(Proof) != 1:

			print('\n\033[38;5;196mInvalid data entered._129\
				\nThe link contains invalid characters.\033[0m')

			sys.exit(0)

		#Getting_the_root_URL.
		Base_URL= str('{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(List_params_1[0])))

		#Main dictionary.
		Dict_values = {}

		'''Checking for a backslash at the end of the root url.'''
		if re.findall(r'..$',Base_URL)[0][0] != '\\':

			'''Checks whether there are errors in the protocol and in the domain name url.
			   If there is an error, then the transition to an exception will occur:
				
				Example:

			   ┌─requests.header('https://www.bullshit.com')
			   │
			   └─>except:(socket.gaierror,urllib3.exceptions.NewConnectionError,urllib3.exceptions.MaxRetryError....)
				.........'''
			if requests.head(Base_URL):																									
				
				Dict_values['url'] = Base_URL																									

		else:

			print('\n\033[38;5;196mMost likely, this page does not exist.\033[0m')

			sys.exit(0)

		'''Searches for and also checks for validity, 
		   the path to the directory that the user specified.'''
		for subset in List_params_1:

			if os.path.isdir(subset):

				if re.findall(

					r'^[A-Z]:/[^\//:?"<>|\r\n].+[^\\:?"/<>|\r\n]+/?$|^[A-Z]:\\[^\//:?"<>|\r\n].+[^\\:?"/<>|\r\n]+\\?$',subset

					) and 'Windows' in str(platform.platform()) or 'Windows' not in str(platform.platform()) and re.findall(

					r'^/[^/].+[^/]/?$|^\\[^\\].+[^\\]\\?$',subset):

					Dict_values['Path'] = subset.replace('\\', '/')

		#----------------------------------------------------------------------------
		if '-g' in List_params_1:

			Dict_values['-g'] = 'graph'

		#A graphical window for selecting a folder.
		if '-p' in List_params_1 and 'Path' not in Dict_values:

			root = tk.Tk()

			root.update()

			root.withdraw()

			directory_path = filedialog.askdirectory()

			root.quit()

			root.destroy()

			if directory_path!= '' and not directory_path.isspace() and bool(directory_path) != False:

				Dict_values['Path'] = directory_path.replace('\\', '/')

		#----------------------------------------------------------------------------
		List_commands=[i for i in Dict_values]


		if len(List_commands) == len(List_params_1) or len(List_commands) == 1 and len(List_params_1)==1:

			return Dict_values

		else:

			print('\033[38;5;196mData entered incorrectly.\033[0m')  



	except KeyboardInterrupt:

		print('\033[0m')

		print('\n\n\033[31mProgram exit.\033[0m')

		sys.exit(0)


	except SystemExit:

		sys.exit(0)




if __name__ == '__main__':

	import Welcome

	Welcome.Welcome()

	dic_t = Input()