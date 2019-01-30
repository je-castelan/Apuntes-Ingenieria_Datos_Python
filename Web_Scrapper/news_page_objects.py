import bs4
import requests
from common import config

class HomePage:
	"""Clase del objeto HTML consultado y analizado"""
	def __init__(self, news_site_uid, url):
		"""Constructor donde se consulta a la URL"""
		self._config = config()['news_sites'][news_site_uid]
		self._queries = self._config['queries']
		self._html = None	
		self._visit(url)

	@property
	def articule_links(self):
		link_list = []
		for link in self._select(self._queries['homepage_articule_links']):
			if link and link.has_attr('href'):
				link_list.append(link)
		return set(link['href'] for link in link_list)

	def _select(self, query_string):
		return self._html.select(query_string)

	def _visit(self, url):
		"""Función para obtener el contenido y hacer el parseo"""
		response = requests.get(url)
		response.raise_for_status()
		self._html = bs4.BeautifulSoup(response.text, 'html.parser')
