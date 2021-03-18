'''
! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !

I specifically decided to write this primitive function, 
since the regular expression is not able to handle LARGE links.

! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !

'''
import re
import requests
from urllib.parse import urlparse
from datetime import datetime

def Exist_https(Base_URL,url):
	'''
			RFC 3986 Uniform Resource Identifier (URI): Generic Syntax
	
	2.2. Reserved characters:

	reserved    = gen-delims / sub-delims
	gen-delims  = ":" / "/" / "?" / "#" / "[" / "]" / "@"
	sub-delims  = "!" / "$" / "&" / "'" / "(" / ")" / "*" / "+" / "," / ";" / "="

	2.3. Unreversed characters:

	unreserved  = ALPHA / DIGIT / "-" / "." / "_" / "~"

	↓ Links containing acceptable characters in the links for the site map.
	'''
	normal_characters=['/',':','.','-','_','`',]# ? &  =

	if url and not url.isspace():

		if Base_URL not in url and url[0]=='/':
			
			url=Base_URL+url[1:]

			if url[-1]!='/' and '.html' not in url:

				url=url+'/'


		if Base_URL in url:

			i=-1

			list_url=list(url)

			for letter in url:
				
				i+=1

				if not letter.isalpha() and not letter.isdigit():

					if letter not in normal_characters:
						
						return False

					# normal_characters[:3]= ['/',':','.']
					truth = [letter for i in normal_characters[:3] if letter==i]

					""" 
					'==3' because list(range(4,7))=[4,5,6], 'https://'[6]='http://'[6],
					[str(i==index) for index in list(range(4,7))] ?= ['True','True','False'], ['False','False','True']....."""
					index= True if len([ True for index in list(range(4,7)) if i!=index])==3 else False

					if i+1!=len(url):

						if letter == url[i+1] and truth and index:

							return False

					if letter==':' and i!=5 and i!=4:

						return False

			if not  re.search(r'/$',url) and \
			not re.search('(\.(\w+)){1}$',url):

				url=url + '/'

				return url

			if re.search('(\.(\w+)){1}$',url) and '.html' in url \
			or re.search('(\.(\w+)){1}$',url) and '.php' in url:

				return url

			elif re.search('(\.(\w+)){1}$',url) and \
			'.html' not in url and '.php'  not in url:

				return False

			return url

		else:
			
			return False



'''

The function is written to analyze references 
to the presence of valid document extensions.

''' #List,Succes_List
def Document_ext(Base_URL,url,Header_date,len_pages_rank,):

	'''

	url=https://example.com/page1/doc.pdf, 
	re.search( pattern, url ).group(0) = '.pdf' 

	'''
	if url and not url.isspace():

		if Base_URL not in url and url[0]=='/':
			
			url=Base_URL+url[1:]

		if Base_URL in url:

			pattern=re.compile('(\.(\w+)){1}$')
			
			if re.search(pattern,url):

				res=re.search(pattern,url).group(0)

				extensions=(lambda b: b+[i.upper() for i in b])(

					['.pdf','.docs', '.excel', '.xml']

					)

				truth = True if True in [True for i in extensions if res==i] else False

				if truth:

					return url


