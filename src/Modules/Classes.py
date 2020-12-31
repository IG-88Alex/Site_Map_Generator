import networkx as Nx
import numpy.random as rnd

import matplotlib.pyplot as Plt

import asyncio
import aiohttp


import codecs
import platform
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import unquote, unquote_plus
import os, sys, requests, datetime , time , re , time, queue


class Search:

  counter = 0

  def __init__(self,URL):

    try:

      self.URL=URL

      self.context = ssl.SSLContext(ssl.PROTOCOL_TLS)#######################
      self.context.verify_mode = ssl.CERT_REQUIRED##########################

      self.Rank_0=[]

      self.Rank_1=[]

      self.Rank_2=[]

      self.Rank_3=[]

      self.Rank_4=[]

      self.Rank_5=[]

      self.Fundament=[]

      self.Additional=[]


      self.Dict_rank={'1.00':self.Rank_0,'0.80':self.Rank_1,'0.64':self.Rank_2,'0.54':self.Rank_3,'0.41':self.Rank_4,'0.35':self.Rank_5}

      self.Header_date=['Etag','Date','Last-Modified','last-modified']

      
      self.Scheme=urlparse(self.URL).scheme

      self.Netloc=urlparse(self.URL).netloc

      self.Base_URL= str('{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(self.URL)))

      #-----------------------------------------------------------------------------+
      self.Format_Read_Upper  = ['DOCX','DOC','PDF','RTF','ZIP','TXT']             #|
      self.Format_Read_Lower  = [form.lower() for form in self.Format_Read_Upper]  #|
                                                                                   #|
      self.Format_Read_All = self.Format_Read_Upper + self.Format_Read_Lower       #|
      #-----------------------------------------------------------------------------+


      #-----------------------------------------------------------------------------+
      self.Format_Image_Upper = ['GIF','JPEG','PNG','WEBP','JPG']                  #|
      self.Format_Image_Lower = [form.lower() for form in self.Format_Image_Upper] #|
                                                                                   #|
      self.Format_Image_All = self.Format_Image_Upper + self.Format_Image_Lower    #|
      #-----------------------------------------------------------------------------+


      self.All_Format = self.Format_Image_All + self.Format_Read_All

      self.Simphols = ['#','&','?','=']

      self.Simphols_Format= self.Simphols+self.All_Format


      self.Headers={
          "Host":self.Netloc,
          'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',      
          'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',    
          'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',                                 
          'Accept-Encoding':'gzip, deflate, br',
          'Referer':'https://www.google.com/',
          'DNT':'1',
          'Connection':'keep-alive',
          'Cookie':'',
          'Upgrade-Insecure-Requests':'1',
          'TE':'Trailers'}

      

      if requests.get(url=self.Base_URL).status_code == 200:
        print(f'\n\033[38;5;46mSuccessful server response  <Response [200]>.\033[0m\n')

        self.Response=True

      if requests.get(url=self.Base_URL).status_code == 403:
        print(f'\n\033[38;5;196mThe server recognized the parser <Response [403]> !!!.\033[0m')

        self.Response=False



    except ConnectionError as error:
      print(f'\n\033[31mConnection_Error: {error}.\033[0m')




  async def searching_links(self,url,headers=None):

    

    async with aiohttp.ClientSession(headers={'Connection': 'keep-alive'}) as session:


      url = await url.get(ssl=self.context)

      


      async with session.get(url,allow_redirects=False) as response:

        if response.status == 200:

          

          self.pages = []

          if url != '' and url[-1] != '/' and urlparse(url).path != '/':


            self.pages = urlparse(url).path[1:].split('/')

           


          elif url !='' and url[-1] == '/' and urlparse(url).path != '/':


            self.pages=urlparse(url).path[1:-1].split('/')

            

           #------------------------------Get__headers__date.
          for date in self.Header_date:

            if date in response.headers:

              self.Last_mod = response.headers[date]

          #--------------------------------------------------------------------------Link__ranking.

          if self.Base_URL not in  [i[0] for i in self.Dict_rank['1.00']]:

            #print([i[0] for i in self.Dict_rank['1.00']])

            self.Dict_rank['1.00'].append((self.Base_URL,self.Last_mod,'1.00'))


          if len(self.pages) == 1 or len(self.pages) == 2:

            Page_Rank = '0.80'

            if url not in [i[0] for i in self.Dict_rank['0.80']]:

              #print([i[0] for i in self.Dict_rank['0.80']])

              self.Dict_rank['0.80'].append((url,self.Last_mod,Page_Rank))



          if len(self.pages) == 3 or len(self.pages) == 4:

            Page_Rank = '0.64'

            if url not in [i[0] for i in self.Dict_rank['0.64']]:

              self.Dict_rank['0.64'].append((url,self.Last_mod,Page_Rank))



          if len(self.pages) == 5 or len(self.pages) == 6:

            Page_Rank = '0.54'

            if url not in [i[0] for i in self.Dict_rank['0.54']]:

              self.Dict_rank['0.54'].append((url,self.Last_mod,Page_Rank))


          if len(self.pages) ==  7 or len(self.pages) == 8:

            Page_Rank = '0.41'

            if url not in [i[0] for i in self.Dict_rank['0.41']]:

              self.Dict_rank['0.41'].append((url,self.Last_mod,Page_Rank))


          if len(self.pages) == 9 or len(self.pages) > 9:

            Page_Rank = '0.35'

            if url not in [i[0] for i in self.Dict_rank['0.35']]:

              self.Dict_rank['0.35'].append((url,self.Last_mod,Page_Rank))


#------------------------------------------------------------Search__for__links.-----------------------------------------------------------------------------------


          Text = await response.content.read()

          for tag in (BeautifulSoup(Text,'lxml').find_all('a',href=True)):

            #--------R_E_Q_U_I_R_E_M_E_N_T_1____Main_links_absolute_path
            if (unquote(tag['href']) != self.Base_URL[:-1]) \
            and tag['href'] not in self.Fundament \
            and urlparse(unquote(tag['href'])).scheme == self.Scheme \
            and urlparse(unquote(tag['href'])).netloc == self.Netloc:

              self.Succes = None

              for elem in self.Simphols_Format:

                if elem in unquote(tag['href']):

                  self.Succes = True



              if self.Succes == None and 'class' in tag.attrs and 'date' not in tag['class'][0]:

                Search.counter += 1

                self.Fundament.append(unquote(tag['href']))

                print(f"{Search.counter}\033[38;5;200m>    \033[38;5;46m{unquote(tag['href'])}\033[0m")

              if self.Succes == None and 'class' not in tag.attrs:

                Search.counter += 1

                self.Fundament.append(unquote(tag['href']))

                print(f"{Search.counter}\033[38;5;200m>    \033[38;5;46m{unquote(tag['href'])}\033[0m")

    

            
            #--------------------------------------------------------------------------------------------------------R_E_Q_U_I_R_E_M_E_N_T_2____Main_links_relative_path
            if bool(urlparse(unquote(tag['href'])).path) == True and unquote(tag['href'][0]) =='/' and ':' not in unquote(tag['href'])\
            and unquote(self.Base_URL+tag['href'][1:]) not in self.Fundament and urlparse(unquote(tag['href'])).netloc != self.Netloc:
              
              self.Succes = None

              for elem in self.Simphols_Format:

                if elem in unquote(self.Base_URL + tag['href'][1:]):

                  self.Succes = True


              if self.Succes == None and 'class' in tag.attrs:

                if len(tag['class']) > 1:

                  if 'date' not in tag['class'][0]:

                    Search.counter += 1

                    self.Fundament.append(unquote(self.Base_URL + tag['href'][1:]))

                    print(f"{Search.counter}\033[38;5;200m>    \033[38;5;46m{unquote(self.Base_URL + tag['href'][1:])}\033[0m")

              if self.Succes == None and 'class' not in tag.attrs:

                Search.counter += 1

                self.Fundament.append(unquote(self.Base_URL + tag['href'][1:]))

                print(f"{Search.counter}\033[38;5;200m>    \033[38;5;46m{unquote(self.Base_URL + tag['href'][1:])}\033[0m")
                




            #-----------------------------------------------------------R_E_Q_U_I_R_E_M_E_N_T_3____Additional_Reference
            if urlparse(unquote(tag['href'])).netloc != self.Netloc:

              self.Succes = None
              
              for form in self.All_Format:

                if form in unquote(tag['href']):

                  self.Succes = True

              if self.Succes == None and urlparse(unquote( tag['href'])).scheme == self.Scheme:

                Search.counter += 1

                self.Additional.append(unquote(tag['href'].rstrip()))

                print(f"{Search.counter}\033[38;5;200m>    \033[38;5;51m{unquote(tag['href']).rstrip()}\033[0m")



      self.len_Additional=len(self.Additional)




#----------------------------------------------------------The__generation__of__the__main__file__of__the__site__map.---------------------------------------------------

class Get_File_Map:


  def __init__(self,Base_URL, Netloc, Path = None):

    self.Path = Path

    if 'www' in Netloc:

      pattern=re.compile("[https,http]://www.(\\w+).")

      pattern=pattern.findall(Base_URL)[0] 

      self.name='/' + pattern + '_sitemap_1.xml'


    if 'www' not in Netloc:

      pattern=re.compile("[https,http]://(\\w+).")

      pattern=pattern.findall(Base_URL)[0]

      self.name='/' + pattern + '_sitemap_1.xml'


    if 'Windows' in str(platform.platform()):

      PWD = str(os.getcwd()).replace('\\', '/')

    else:            #(Linux/GNU)
      
      PWD = str(os.getcwd()).replace('/','\\')###########


    if self.Path == None: 

      self.Path_Folder = (PWD + "/Site_Maps/" + str(pattern[0]).upper() + str(pattern[1:]))

    elif self.Path!= None and self.Path[-1] == '/':

      self.Path_Folder = self.Path + "Site_Maps/" + str(pattern[0]).upper() + str(pattern[1:])

    elif self.Path != None and self.Path[-1] != '/':

      self.Path_Folder = self.Path + "/Site_Maps/" + str(pattern[0]).upper() + str(pattern[1:])


    if  not(os.path.exists(self.Path_Folder)):

      os.makedirs(self.Path_Folder)


    self.Path_file_xml = self.Path_Folder + self.name


    self.File_xml = codecs.open(str(self.Path_file_xml),'w',"utf_8_sig")


    self.File_xml.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" \
      xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9  http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">')

    self.File_xml.close()

    self.File_xml = codecs.open(str(self.Path_file_xml),'a',"utf_8_sig")

    if 'Windows' in str(platform.platform()):
    
      self.Path_file_xml = self.Path_file_xml.replace('/','\\')

    if 'Linux' in str(platform.platform()):

      self.Path_file_xml = self.Path_file_xml.replace('\\','/')




  def Gen_site_map(self,URL,Last_mod,Priority):

    Date = datetime.datetime.strptime(Last_mod, "%a, %d %b %Y %H:%M:%S GMT")

    Last_mod = f'{Date.replace().isoformat()}"+00:00"'


    #----------------------------------------------------Let's__write__to__the__file.
    tree_xml =f"\n    <url>\
    \n\n    <loc>{URL}</loc>\
    \n\n    <lastmod>{Last_mod}</lastmod>     \
    \n\n    <priority>{Priority}</priority>\
    \n\n    </url>"
      
    self.File_xml.write(tree_xml)


  def Site_map_close(self):

    self.File_xml.write('\n</urlset>')

    self.File_xml.close()

    



#--------------------------------------Generating_a_graph_based_on_the_created_list
class Graph_parse:

  list_colors = ['blue','red']

  list_node_sizes = [400,50]

  list_pages = []



  def construct_gruph(self,Netloc,listing):

    self.graph = Nx.Graph()

    

    for url in listing:


        if url != '' and url[-1] != '/' and urlparse(url).path != '/': #___First___link__analysis__algorithm.

          self.graph.add_node(Netloc) # Main__page__from__the__link , urlparse((https://www.example.com/)).netloc = www.example.com.

          list_path_node=urlparse(url).path[1:].split('/')[0] # Second__page__from__the__link, method((https://www.example.com/page1/page2))[0] => ['page1'].

          self.graph.add_node(list_path_node) # Create__node.

          self.graph.add_edge(Netloc,list_path_node, graph=self.graph)# Connect__the__created__vertices__of__the__graph. netloc---page1 (www.example.com---page1)

          B=urlparse(url).path[1:].split('/') # method((https://www.example.com/page1/page2))[0] => ['page1','page2','page3'].


          for num in range(len(B)): # Let's connect new vertices of the graph. netloc---page1---page2---page3 (www.example.com---page1---page2---page3)

            if num > 0 and B[num] != '':

              self.graph.add_edge(B[num-1],B[num],graph=self.graph)


        elif url !='' and url[-1] == '/' and urlparse(url).path != '/':# The second__link__analysis__algorithm.
            
          self.graph.add_node(Netloc) 

          list_path_node=urlparse(url).path[1:-1].split('/')[0]

          self.graph.add_node(list_path_node)

          self.graph.add_edge(Netloc,list_path_node, graph=self.graph)

          B=urlparse(url).path[1:-1].split('/')



          for num in range(len(B)):

            if num > 0 and B[num] != '':

              self.graph.add_edge(B[num-1],B[num],graph=self.graph)

                  

    list_red = list(['red' for i in self.graph]) # Let__the__color__of__all__nodes__of__the__graph__be__red.

    list_red[0] = 'cyan' # Let__the__first__node(netloc)__be__a__cyan__color.

    list_sizes = list([150 for i in self.graph])

    list_sizes[0] = 3000


    Nx.draw(self.graph,node_size = list_sizes, node_color = list_red, with_labels = True,font_weight="bold")


    Plt.show()

    return

