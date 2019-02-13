import bs4
import requests

from common import config

class NewsPage:
	"""Clase de una página de una fuente general de noticias"""

	def __init__(self, news_site_uid, url):
		"""Constructor donde se consulta a la URL de una noticia"""
		self._config = config()['news_sites'][news_site_uid]
		self._queries = self._config['queries']
		self._html = None
		self._visit(url)

	def _select(self, query_string):
		"""Función privada para obtener el contenido deseado con el select"""
		return self._html.select(query_string)

	def _visit(self, url):
		"""Función para obtener el contenido y hacer el parseo"""
		response = requests.get(url)
		response.raise_for_status()
		self._html = bs4.BeautifulSoup(response.text, 'html.parser')


class HomePage(NewsPage):
	"""Clase del análisis de la página inicial."""
	def __init__(self, news_site_uid, url):
		"""Constructor"""
		super().__init__(news_site_uid, url)

	@property
	def articule_links(self):
		"""Obtención de los artículos de la página principal"""
		link_list = []
		for link in self._select(self._queries['homepage_articule_links']):
			if link and link.has_attr('href'):
				link_list.append(link)
		return set(link['href'] for link in link_list)

class ArticlePage(NewsPage):
	"""Clase del análisis de una URL de noticia"""
	def __init__(self, news_site_uid, url):
		"""Constructor"""
		super().__init__(news_site_uid, url)

	@property
	def body(self):
		result = self._select(self._queries['article_body'])
		return result[0].text if len(result) else ''

	@property
	def title(self):
		result = self._select(self._queries['article_title'])
		return result[0].text if len(result) else ''
