import re
import networkx as Nx
import matplotlib.pyplot as Plt
from urllib.parse import urlparse


# Generating_a_graph_based_on_the_created_list
class Graph_parse:

  list_colors=['blue','red']

  list_node_sizes=[400,50]

  list_pages=[]

  def __init__(self,Netloc,listing,Dict):

    listing=[i[0] for i in listing][1:]

    if '-g' in Dict:

      self.graph=Nx.Graph()

      self.graph.add_node(Netloc)

      for url in listing:

          pages=urlparse(url).path.strip('/').split('/')

          if pages:

            page_one=pages[0]

            self.graph.add_node(page_one)

            self.graph.add_edge(Netloc,page_one, graph=self.graph)

            for num in range(len(pages)):

              if num > 0 and pages[num] != '':

                self.graph.add_edge(

                  pages[num-1],

                  pages[num],

                  graph=self.graph

                  )
                    
      '''
      Let the color of all nodes of the graph be red.'''
      list_red=list(['red' for i in self.graph])

      '''
      Let the first node(self.Netloc) be a cyan color.'''
      list_red[0]='cyan'

      list_sizes=list([150 for i in self.graph])

      list_sizes[0]=3000

      Nx.draw(

        self.graph,
        node_size=list_sizes,
        node_color=list_red,
        with_labels=True,
        font_weight="bold"

        )

      Plt.show()