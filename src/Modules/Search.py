import ssl
import shutil
import codecs
import asyncio
import aiohttp
import certifi
import platform
import urllib.request
import importlib.util
import networkx as Nx
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse
from bs4 import BeautifulSoup as BS
import os, sys, requests,  re , time, queue
from urllib.parse import unquote, unquote_plus





class Search:

	'''
	Importing Get_File_Map'''
	path_module_1=str(Path(__file__).parent)+'/Import_Module.py'

	module_spec_1 = importlib.util.spec_from_file_location(
			        
			        'Import_Module', path_module_1
			    )

	obj_module_1 = importlib.util.module_from_spec(module_spec_1)

	module_spec_1.loader.exec_module(obj_module_1)

	Import=obj_module_1.Import

	modules=Import()


	Exist_https=modules['Exist_https'].Exist_https

	Document_ext=modules['Exist_https'].Document_ext

	Get_File_Map=modules['Get_File_Map'].Get_File_Map

	Log_info=modules['Log_info'].Log_info


	'''
	Counter for counting links.'''
	__counter=1
	

	def __init__(self,URL,Path_directory=None):

		'''
		Python Certificate provided by Mozilla.'''
		self.sslcontext = ssl.create_default_context(cafile=certifi.where())

		'''
		This List of found links'''
		self.Lis_foun_lin=[]

		# This list is intended for storing valid links.
		self.Succes_link=[]

		'''
		The URL that we pass to the scraper.'''
		self.URL=URL

		'''
		Parse a URL into a 6 components:
		<scheme>://<netloc>/<path>;<params>?<query> <fragment>'''
		self.Scheme=urlparse(URL).scheme

		self.Netloc=urlparse(URL).netloc

		self.Base_URL= str(

		'{uri.scheme}://{uri.netloc}/'.format( uri=urlparse(URL) )

		)

		'''
		Keywords derived from headings 
		that carry information about 
		the time and date the page 
		was formatted.'''
		self.Header_date=(lambda b: b + [i.upper() for i in b])(

			['etag','date','last-modified']

			)

		'''
	    The rank of the page will depend 
	    on the number of pages that lead 
	    to it.'''
		self.len_pages_rank={

	    		   1:'0.80',2:'0.80',
	               3:'0.64',4:'0.64',
	               5:'0.54',6:'0.54',
	               7:'0.41',8:'0.41',
	               9:'0.35'

	               }

		'''
	    The dictionary contains lists, 
	    thanks to which it sorts links 
	    according to their ranks.'''
		self.Contain_rank={

					'1.00':[],
					'0.80':[],
					'0.64':[],
					'0.54':[],
					'0.41':[],
					'0.35':[]

					}

		'''
		Let's create a site map object and a title, a map header.'''
		self.Map=Search.Get_File_Map( self.Netloc, Path_directory )

		# multiplier for b='\b'
		self.mult=0

	'''
	The main function of finding new links.'''
	async def searching_links(self,tupl):

		async with aiohttp.ClientSession(headers={'Connection': 'keep-alive'}) as session:

			tupl = await tupl.get()

			url=tupl[0]

			type_of_request=tupl[1]

			requesters={
						'get':session.get ,
						'head':session.head ,
						}

			requester=requesters[type_of_request]

			async with requester(url,ssl=self.sslcontext) as response:

				await self.html_analysis(url,type_of_request,response)


	async def html_analysis(self,url,type_url,response):

		if Search.__counter < 45000:

			'''
			List of pages selected from the link.
			The generator allows you not only to create a 
			list of pages, but also to remove empty None lines from this list.
			
			https://www.example.com/page1/page2/page3(/)... => ['page1', 'page2', 'page3']'''
			pages=urlparse(url).path.strip('/').split('/')

			self.Last_mod=datetime.now().__format__("%a, %d %b %Y %H:%M:%S GMT")
			#=datetime.now().isoformat()[:-7]+'+00:00'			

			for date in self.Header_date:

				if date in response.headers:

					self.Last_mod = response.headers[date]


			if response.status==200 and url not in self.Succes_link and type_url=='get' \
			or url not in self.Succes_link and type_url=='head':

				# HTML-code, server response to the get-request.
				self.Text = await response.text()

				if url != self.Base_URL and url != self.Base_URL[:-1] and url not in self.Succes_link:

					if pages:
						# The priority of this link, its rank..
						self.Priority=self.len_pages_rank[int(len(pages))]

					self.Contain_rank[self.Priority].append( (url, self.Last_mod, self.Priority) )

					self.Succes_link.append(url)

					Search.__counter+=1

					Len=len(str(Search.__counter))

					# self.mult - multiplier
					if Len==1:
						self.mult=self.mult*1

					if Len > len(str(Search.__counter - 1)):
						self.mult=self.mult+1

					Search.Log_info(Search.__counter, self.mult, url)

				# Checks if the main base link is not in the list.
				if len(self.Lis_foun_lin) == 1 and self.Lis_foun_lin[0] == (self.Base_URL,'get'):

					self.Contain_rank['1.00'].append( (url, self.Last_mod, '1.00') )

					Search.Log_info(Search.__counter, self.mult, self.Base_URL)

				'''
				For each found link found by BeautifulSoup, do the following....'''
				for link in [i['href'] for i in BS(self.Text,'lxml').find_all('a',href=True)]:

					link=unquote(unquote(link))
					
					doc=Search.Document_ext(

						self.Base_URL, link,
						self.Header_date,
						self.len_pages_rank,

						)# self.Succes_doc_link.append((url,Last_mod,Priority))

					if doc and (doc,'head') not in self.Lis_foun_lin:

						Search.__counter+=1

						Len=len( str(Search.__counter) )

						# self.mult - multiplier
						if Len==1:
							self.mult=self.mult*1

						if Len > len(str(Search.__counter - 1)):
							self.mult=self.mult+1

						self.Lis_foun_lin.append((doc,'head'))
					
					
					'''
					2.The first condition is to search for a link based on a given pattern. 
					http(s)://...(.)example.com/.....'''
					url = Search.Exist_https(self.Base_URL,link)

					if url and not doc:

						if (url,'get') not in self.Lis_foun_lin:

							self.Lis_foun_lin.append((url,'get'))


			elif Search.__counter > 45000:

				self.Create_Sitemap()

				self.Map.Site_map_close()

				sys.exit(0)


	# The Create_Sitemap method creates a site map.
	def Create_Sitemap(self):

		'''
		Generates a single list based on the lists of the dictionary self.Contain_rank{}'''
		self.All_links=[n for inner in [self.Contain_rank[i] for i in self.Contain_rank] for n in inner]

		for i in self.All_links:

			self.Map.Gen_site_map(i[0],i[1],i[2])


	def get_counter(self):

		return Search.__counter





























'''
Function for testing the module Search.py'''
async def main():
	try:

		if 'Windows' in str(platform.platform()):

			os.system('cls')
			import ctypes
			kernel32 = ctypes.windll.kernel32
			kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

		# (Linux/GNU)
		else:

			os.system('clear')

		URL = 'https://yandex.ru/'
		Path_directory = None
		obj1 = Search(URL, Path_directory)
		obj1.Lis_foun_lin.append(obj1.Base_URL)

		tasks = []

		work_queue = asyncio.Queue()

		for link in obj1.Lis_foun_lin:

			await work_queue.put(link)

			task = asyncio.ensure_future(

				obj1.searching_links(work_queue)

			)

			tasks.append(task)

			for i in tasks:

				await i


	except KeyboardInterrupt:

		sys.exit(0)


if __name__ == '__main__':
	loop_2 = asyncio.get_event_loop()

	loop_2.run_until_complete(main())
