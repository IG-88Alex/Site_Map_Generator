from elapsedtimer import ElapsedTimer
from urllib.parse import urlparse
import warnings
import asyncio
import aiohttp
import sys, os
from pathlib import Path
import importlib.util

module_spec = importlib.util.spec_from_file_location(
'Importing', str(Path(__file__).parent)+'/Importing.py'
	)
obj_module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(obj_module)
Import=obj_module.Import

def main():
	'''
	The @Import decorator allows you to pass a 
	dictionary with modules to the "modules" parameter 
	of the "def main(modules)" function'''
	@Import
	def Main(modules):

		warnings.filterwarnings("ignore", category=RuntimeWarning)

		'''
		Before you can !run a module! using its !specification!, 
		you must create a reference to it in the form of a variable.'''
		Search=modules['Search'].Search
		Graph_parse=modules['Graph'].Graph_parse
		Input=modules['Input'].Input
		Results=modules['Results'].Results
		Welcome=modules['Welcome'].Welcome
		
		'''
		This function(Welcome) imports the greeting - program logo, 
		and also includes support for the ANSI standard for output 
		in the running Windows/Linux console.'''
		Welcome()

		'''
		Used for user input, links, and specific parameters.'''
		Dict_values=Input()

		# URL for our web-crawler.
		URL=Dict_values['url']
		Path_directory=None

		if 'Path' in Dict_values:
			Path_directory=Dict_values['Path']

		obj1=Search(URL,Path_directory)
		obj1.Lis_foun_lin.append((obj1.Base_URL,'get'))

		# The main branch of the program.
		async def run_coroutines():

			nonlocal obj1

			tasks=[]

			work_queue = asyncio.Queue()

			for link in obj1.Lis_foun_lin:

				await work_queue.put(link)

				task = asyncio.ensure_future(

					obj1.searching_links(work_queue)
				)

				tasks.append(task)

				for i in tasks:

					await i
				
		try:
			et=ElapsedTimer()
			
			et.start()
			loop_2=asyncio.get_event_loop()
			loop_2.run_until_complete(run_coroutines())
			et.stop()

			obj1.Create_Sitemap()
			obj1.Map.Site_map_close()
			counter=obj1.get_counter()
			Results(counter, et.elapsed, obj1.Netloc, obj1.Map.Path_File_XML)
			graph=Graph_parse(obj1.Netloc, obj1.All_links, Dict_values)
			
		except KeyboardInterrupt:
			et.stop()
			obj1.Create_Sitemap()
			obj1.Map.Site_map_close()
			print('\n\n\033[38;5;196mStop execution, exit the program.\033[0m')
			counter=obj1.get_counter()
			Results(counter,et.elapsed,obj1.Netloc,obj1.Map.Path_File_XML)		
			graph=Graph_parse(obj1.Netloc,obj1.All_links,Dict_values)
			sys.exit(0)

		except aiohttp.client_exceptions.ClientPayloadError as error:
			print('\n\n\033[31mThe program was interrupted by an error.\033[0m')
			print(f'\n\n\033[38;5;{error}\033[0m')
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
