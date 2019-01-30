import argparse
import logging
"""Importacion de libreria de logging a nivel INFO"""
logging.basicConfig(level=logging.INFO)

import news_page_objects as news
from common import config


logger = logging.getLogger(__name__)

def _news_scraper(news_site_uid):
	""""Modulo que genera el scrapper de la pagina seleccionada"""
	host = config()['news_sites'][news_site_uid]['url']
	logging.info('Beggining scrapper for {}'.format(host))
	homepage = news.HomePage(news_site_uid, host)

	for link in homepage.articule_links:
		print(link) 

if __name__ == '__main__':
	"""Funcion principal"""
	parser = argparse.ArgumentParser()
	news_site_choices = list(config()['news_sites'].keys())
	parser.add_argument(
		'news_site',
		help='Site that you want to scrape',
		type=str,
		choices=news_site_choices
		)

	args = parser.parse_args()
	_news_scraper(args.news_site)
