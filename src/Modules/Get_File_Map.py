import re, os, codecs, datetime, platform
from tldextract import extract

class Get_File_Map:

  def __init__(self,Netloc,Path_directory=None):

    '''
    Domain name (or second level domain.).

    [ tldextract.extract() ] methodd 
    allows you to find the name 
    of a resource, and separates 
    it from prefixes and suffixes.'''
    sld_name=extract(Netloc).domain

    #The name of the site, a second level domain.
    self.name='/' + sld_name + '_sitemap.xml'
    
    #Current work directory  
    Cur_work_dir = str(os.getcwd()).replace('/','\\')

    if Path_directory == None:

      self.Path_Folder = (

      Cur_work_dir + "/Site_Maps/" + sld_name.replace(sld_name[0],sld_name[0].upper(),1)

        )

    else:

      self.Path_Folder = (

      Path_directory+"/Site_Maps/"+sld_name.replace(sld_name[0],sld_name[0].upper(),1)

        )

    '''
    Check whether a folder with this name exists, 
    if it does not exist, then you need to create this folder.'''
    if  not(os.path.exists(self.Path_Folder)):

      os.makedirs(self.Path_Folder)

    #Path, location of the XML-file.
    self.Path_File_XML = self.Path_Folder + self.name

    #Clear the file, write a new header - 'w'.
    with codecs.open(str(self.Path_File_XML),'w',"utf_8_sig") as self.File_XML:

      self.File_XML.write(

        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" \
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" \
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9  \
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">'

        )

      self.File_XML.close()

    '''
    Depending on the operating system, 
    replace the slash with a backslash, 
    for variable self.Path_file_xml.'''
    if 'Windows' in str(platform.platform()):
    
      self.Path_File_XML = self.Path_File_XML.replace('/','\\')

    if 'Linux' in str(platform.platform()):

      self.Path_File_XML = self.Path_File_XML.replace('\\','/')


  def Gen_site_map(self,URL,Last_mod,Priority):

    Date = datetime.datetime.strptime(Last_mod, "%a, %d %b %Y %H:%M:%S GMT")

    Last_mod = f'{Date.replace().isoformat()}+00:00'

    #Let's write to the file.
    tree_xml =f"\n    <url>\
    \n\n    <loc>{URL}</loc>\
    \n\n    <lastmod>{Last_mod}</lastmod>     \
    \n\n    <priority>{Priority}</priority>\
    \n\n    </url>"
      
    with codecs.open(str(self.Path_File_XML),'a',"utf_8_sig") as self.File_XML:

      self.File_XML.write(tree_xml)

      self.File_XML.close()


  def Site_map_close(self):

    with codecs.open(str(self.Path_File_XML),'a',"utf_8_sig") as self.File_XML:

      self.File_XML.write('\n</urlset>')

      self.File_XML.close()