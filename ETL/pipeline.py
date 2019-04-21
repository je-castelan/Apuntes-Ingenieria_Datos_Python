import logging
logging.basicConfig(level=logging.INFO)
import subprocess

logger = logging.getLogger(__name__)

news_sites_uids=['eluniversal','elpais']

def main():
    _extract()
    _transform()
    _load()

def _extract():
    logger.info("Starting extract process")
    for news_site_uid in news_sites_uids:
        subprocess.run(['python','main.py',news_site_uid], cwd='../Web_Scrapper')
        subprocess.run(['find','.','-name','{}*'.format(news_site_uid),
                        '-exec', 'mv', '{}', '../Data_Wrangling/{}.csv'.format(news_site_uid),
                        ';'], cwd='../Web_Scrapper')

def _transform():
    logger.info("Starting transform process")
    for news_site_uid in news_sites_uids:
        subprocess.run(['python','newspaper_receipe.py','{}.csv'.format(news_site_uid)], cwd='../Data_Wrangling')
        subprocess.run(['find','.','-name','{}*cleaned*'.format(news_site_uid),
                        '-exec', 'mv', '{}', '../Load_Database/{}.csv'.format(news_site_uid),
                        ';'], cwd='../Data_Wrangling')
        subprocess.run(['find','.','-name','{}*'.format(news_site_uid),
                        '-exec', 'rm', '{}',';'], cwd='../Data_Wrangling')

def _load():
    logger.info("Starting loading process")
    for news_site_uid in news_sites_uids:
        subprocess.run(['python','main.py','{}.csv'.format(news_site_uid)], cwd='../Load_Database')
        subprocess.run(['find','.','-name','{}*'.format(news_site_uid),
                        '-exec', 'rm', '{}',';'], cwd='../Load_Database')


if __name__ == '__main__':
    main()
