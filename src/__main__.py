import requests
import queue
import sys, os
import re
from prettytable import PrettyTable
from elapsedtimer import ElapsedTimer
from itertools import chain, combinations
import tkinter as tk
from tkinter import filedialog
from urllib.parse import urlparse
import asyncio
import aiohttp
import warnings
import platform

import signal
import subprocess

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from src.Modules.Input   import Input
from src.Modules.Classes import Search
from src.Modules.Classes import Get_File_Map
from src.Modules.Classes import Graph_parse



def main():
	
	warnings.filterwarnings("ignore", category=RuntimeWarning)
	

	if 'Windows' in str(platform.platform()):

		os.system('cls')

		import ctypes
		kernel32 = ctypes.windll.kernel32
		kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)  

	else:            #(Linux/GNU)
	    
		os.system('clear')

		

	print('''\033[35m                  


		\033[38;5;200m  _____ _ _                                 _____                           _              \033[0m                           
		\033[38;5;200m / ____(_) |                               / ____|                         | |             \033[0m                           
		\033[38;5;200m| (___  _| |_ ___ _ __ ___   __ _ _ __    | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __  \033[0m \033[37m  \__|__/  \033[0m 
		\033[38;5;200m \___ \| | __/ _ \ '_ ` _ \ / _` | '_ \   | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__| \033[0m \033[37m  /\_|_/\  \033[0m
		\033[38;5;200m ____) | | ||  __/ | | | | | (_| | |_) |  | |__| |  __/ | | |  __/ | | (_| | || (_) | |    \033[0m \033[37m_/_/   \_\_\033[0m   
		\033[38;5;200m|_____/|_|\__\___|_| |_| |_|\__,_| .__/    \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|    \033[0m \033[37m \ \___/ / \033[0m  
		\033[38;5;200m                                 | |                                                       \033[0m \033[37m  \/_|_\/  \033[0m  
		\033[38;5;200m                                 |_|                                                       \033[0m \033[37m  /  |  \  \033[0m''')

	Dict_values=Input()

	URL = Dict_values['url']

	obj1=Search(URL)
	
	Param_Get_Map = None

	

	
	async def base():

		nonlocal obj1

		work_queue = asyncio.Queue()

		await work_queue.put(str(obj1.Base_URL))

		await obj1.searching_links(work_queue)

		
	
	async def Search_All_URL():

		nonlocal obj1

		work_queue = asyncio.Queue()

		tasks=[]


		for url in obj1.Fundament:

			if len(obj1.Fundament) != 46000:

				await work_queue.put(url)

				task = asyncio.ensure_future(obj1.searching_links(work_queue))

				tasks.append(task)

				for tas_k in tasks:

					await tas_k

			if len(obj1.Fundament) >= 46000:

				break

	try:


		URL = Dict_values['url']

		print('\033[0m')

		loop_1= asyncio.get_event_loop()
								
		loop_1.run_until_complete(base())


	except KeyboardInterrupt:

		print('\n\n\033[31mProgram exit._222\033[0m')
		

		if 'Path' in Dict_values:

			site_map = Get_File_Map(obj1.Base_URL,obj1.Netloc,Dict_values['Path'])

		else:
			
			site_map = Get_File_Map(obj1.Base_URL,obj1.Netloc)

			print(f'\nHere is Param_Get_Map_1: {Param_Get_Map}\n')
		

		if Param_Get_Map != None:


			for url, last_mod, page_rank in Param_Get_Map:

				site_map.Gen_site_map(url,last_mod,page_rank)

			site_map.Site_map_close()

		
		elif Param_Get_Map == None:

			

			Param_Get_Map =list(obj1.Rank_0 + obj1.Rank_1 + obj1.Rank_2 + obj1.Rank_3 + obj1.Rank_4 + obj1.Rank_5)

			for url, last_mod, page_rank in Param_Get_Map:

				site_map.Gen_site_map(url,last_mod,page_rank)

			site_map.Site_map_close()



		if Head_List_Table == None and Table_obj == None and List_Table == None and Tbl_data == None:

			Head_List_Table=['\033[38;5;208mLinks\033[0m','\033[38;5;208mQuantity\033[0m','\033[38;5;208mURL\033[0m'] 			 
																															     
			Table_obj = PrettyTable(Head_List_Table)																		     
																															     
			List_Table = ['\033[38;5;200mSum of the  \033[38;5;46mbasic \033[38;5;200mlinks site:\033[0m\n',\
			f'\033[38;5;226m{len(Param_Get_Map)}\033[0m\n',' ',
			'\033[38;5;200mSum of the \033[38;5;46madditional \033[38;5;200mlinks site:\033[0m\n',\
			f'\033[38;5;226m{obj1.len_Additional}\033[0m\n',f'\033[38;5;87m{obj1.Base_URL}\033[0m',
			'\033[38;5;200mSum of the \033[38;5;46mall \033[38;5;200mlinks site:\033[0m\n',\
			f'\033[38;5;226m{int(len(Param_Get_Map)+obj1.len_Additional)}\033[0m\n',' ',
			'\033[38;5;196mTime\033[38;5;200m:\033[0m','\033[38;5;226m %.3f \033[0m' % (et.elapsed),' ']

			Tbl_data = list(List_Table)

			while Tbl_data:

				Table_obj.add_row(Tbl_data[:3])

				Tbl_data = Tbl_data[3:]

			print(end='\n'*3)

			print(Table_obj)

			print('\n\033[38;5;40mFile was received.\033[0m')

			print(f'\n\033[38;5;40mFile Path: {site_map.Path_file_xml} .\033[0m')

			if '-g' in Dict_values:										  

				Graph = Graph_parse()

				Graph.construct_gruph(obj1.Netloc,obj1.Fundament)

			sys.exit(0)


	
	try:
		#----------------------------_TABLE
		Head_List_Table = None

		Table_obj = None

		List_Table = None

		Tbl_data = None
		#----------------------------_TABLE
		
		et = ElapsedTimer()

		et.start()

		loop_2 = asyncio.get_event_loop()

		loop_2.run_until_complete(Search_All_URL())
		
		et.stop()


	




		if 'Path' in Dict_values:

			site_map = Get_File_Map(obj1.Base_URL,obj1.Netloc,Dict_values['Path'])

		else:
			
			site_map = Get_File_Map(obj1.Base_URL,obj1.Netloc)


		Param_Get_Map = list(obj1.Rank_0 + obj1.Rank_1 + obj1.Rank_2 + obj1.Rank_3 + obj1.Rank_4 + obj1.Rank_5)



		for url, last_mod, page_rank in Param_Get_Map:

			site_map.Gen_site_map(url,last_mod,page_rank)

		site_map.Site_map_close()


	#-------------------------------------------------------------------------------------------------------------------------+
																															 
		Head_List_Table=['\033[38;5;208mLinks\033[0m','\033[38;5;208mQuantity\033[0m','\033[38;5;208mURL\033[0m'] 			 
																														     
		Table_obj = PrettyTable(Head_List_Table)																		     
																														     
		List_Table = ['\033[38;5;200mSum of the  \033[38;5;46mbasic \033[38;5;200mlinks site:\033[0m\n',\
		f'\033[38;5;226m{len(Param_Get_Map)}\033[0m\n',' ',
		'\033[38;5;200mSum of the \033[38;5;46madditional \033[38;5;200mlinks site:\033[0m\n',\
		f'\033[38;5;226m{obj1.len_Additional}\033[0m\n',f'\033[38;5;87m{obj1.Base_URL}\033[0m',
		'\033[38;5;200mSum of the \033[38;5;46mall \033[38;5;200mlinks site:\033[0m\n',\
		f'\033[38;5;226m{int(len(Param_Get_Map)+obj1.len_Additional)}\033[0m\n',' ',
		'\033[38;5;196mTime\033[38;5;200m:\033[0m','\033[38;5;226m %.3f \033[0m' % (et.elapsed),' ']

		Tbl_data = list(List_Table)

		while Tbl_data:

			Table_obj.add_row(Tbl_data[:3])

			Tbl_data = Tbl_data[3:]

		print(end='\n'*3)

		print(Table_obj)

		print(end='\n'*2)

		print('\n\033[38;5;40mFile was received.\033[0m')

		print(f'\n\033[38;5;40mFile Path: {site_map.Path_file_xml} .\033[0m')


		#-----------------------------C__R__E__A__T__E----------G__R__A__P__H-----------+
																	  
		if '-g' in Dict_values:										  

			Graph = Graph_parse()

			Graph.construct_gruph(obj1.Netloc,obj1.Fundament)


	except KeyboardInterrupt:

		print('\n\n\033[31mProgram exit._111\033[0m')


		if 'Path' in Dict_values:

			site_map = Get_File_Map(obj1.Base_URL,obj1.Netloc,Dict_values['Path'])

		else:
			
			site_map = Get_File_Map(obj1.Base_URL,obj1.Netloc)

			print(f'\nHere is Param_Get_Map_1: {Param_Get_Map}\n')
		

		if Param_Get_Map != None:


			for url, last_mod, page_rank in Param_Get_Map:

				site_map.Gen_site_map(url,last_mod,page_rank)

			site_map.Site_map_close()

		
		elif Param_Get_Map == None:

			
			Param_Get_Map =list(obj1.Rank_0 + obj1.Rank_1 + obj1.Rank_2 + obj1.Rank_3 + obj1.Rank_4 + obj1.Rank_5)

			for url, last_mod, page_rank in Param_Get_Map:

				site_map.Gen_site_map(url,last_mod,page_rank)

			site_map.Site_map_close()


		if Head_List_Table == None and Table_obj == None and List_Table == None and Tbl_data == None:

			Head_List_Table=['\033[38;5;208mLinks\033[0m','\033[38;5;208mQuantity\033[0m','\033[38;5;208mURL\033[0m'] 			 
																															     
			Table_obj = PrettyTable(Head_List_Table)																		     
																															     
			List_Table = ['\033[38;5;200mSum of the  \033[38;5;46mbasic \033[38;5;200mlinks site:\033[0m\n',\
			f'\033[38;5;226m{len(Param_Get_Map)}\033[0m\n',' ',
			'\033[38;5;200mSum of the \033[38;5;46madditional \033[38;5;200mlinks site:\033[0m\n',\
			f'\033[38;5;226m{obj1.len_Additional}\033[0m\n',f'\033[38;5;87m{obj1.Base_URL}\033[0m',
			'\033[38;5;200mSum of the \033[38;5;46mall \033[38;5;200mlinks site:\033[0m\n',\
			f'\033[38;5;226m{int(len(Param_Get_Map)+obj1.len_Additional)}\033[0m\n',' ',
			'\033[38;5;196mTime\033[38;5;200m:\033[0m','\033[38;5;226m %.3f \033[0m' % (et.elapsed),' ']

			Tbl_data = list(List_Table)


			while Tbl_data:

				Table_obj.add_row(Tbl_data[:3])

				Tbl_data = Tbl_data[3:]

			print(end='\n'*3)

			print(Table_obj)

			print('\n\033[38;5;40mFile was received.\033[0m')

			print(f'\n\033[38;5;40mFile Path: {site_map.Path_file_xml} .\033[0m')

			if '-g' in Dict_values:										  

				Graph = Graph_parse()

				Graph.construct_gruph(obj1.Netloc,obj1.Fundament)

			sys.exit(0)


	#------------------------------------------------------------------------
	except aiohttp.client_exceptions.ClientPayloadError as error:


		print('\n\n\033[31mProgram exit._333\033[0m')


		if 'Path' in Dict_values:

			site_map = Get_File_Map(obj1.Base_URL,obj1.Netloc,Dict_values['Path'])

		else:
			
			site_map = Get_File_Map(obj1.Base_URL,obj1.Netloc)


		if Param_Get_Map != None:

			for url, last_mod, page_rank in Param_Get_Map:

				site_map.Gen_site_map(url,last_mod,page_rank)

			site_map.Site_map_close()

		
		elif Param_Get_Map == None:

			Param_Get_Map =list(obj1.Rank_0 + obj1.Rank_1 + obj1.Rank_2 + obj1.Rank_3 + obj1.Rank_4 + obj1.Rank_5)

			for url, last_mod, page_rank in Param_Get_Map:

				site_map.Gen_site_map(url,last_mod,page_rank)

			site_map.Site_map_close()
						

		Head_List_Table=['\033[38;5;208mLinks\033[0m','\033[38;5;208mQuantity\033[0m','\033[38;5;208mURL\033[0m'] 			 
																														     
		Table_obj = PrettyTable(Head_List_Table)																		     
																														     
		List_Table = ['\033[38;5;200mSum of the  \033[38;5;46mbasic \033[38;5;200mlinks site:\033[0m\n',\
		f'\033[38;5;226m{len(Param_Get_Map)}\033[0m\n',' ',
		'\033[38;5;200mSum of the \033[38;5;46madditional \033[38;5;200mlinks site:\033[0m\n',\
		f'\033[38;5;226m{obj1.len_Additional}\033[0m\n',f'\033[38;5;87m{obj1.Base_URL}\033[0m',
		'\033[38;5;200mSum of the \033[38;5;46mall \033[38;5;200mlinks site:\033[0m\n',\
		f'\033[38;5;226m{int(len(Param_Get_Map)+obj1.len_Additional)}\033[0m\n',' ',
		'\033[38;5;196mTime\033[38;5;200m:\033[0m','\033[38;5;226m %.3f \033[0m' % (et.elapsed),' ']

		Tbl_data = list(List_Table)


		while Tbl_data:

			Table_obj.add_row(Tbl_data[:3])

			Tbl_data = Tbl_data[3:]

		print(end='\n'*3)

		print(Table_obj)

		print('\n\033[38;5;40mFile was received.\033[0m')

		print(f'\n\033[38;5;40mFile Path: {site_map.Path_file_xml} .\033[0m')

		sys.exit(0)




	except OSError as os_error:

		print(f'\n\033[38;5;196m{os_error}\033[0m')


	except ConnectionResetError as connect_error:

		print(f'\n\033[38;5;196m{connect_error}')


	except aiohttp.client_exceptions.ClientConnectorError as aio_error:

		print(f'\n\033[38;5;196m{aio_error}\033[0m')


	except SystemExit:

		sys.exit(0)



	
if __name__ == '__main__':
	main()
