import re

from bs4 import BeautifulSoup

import urlparse
class HtmlParser(object):
    def parse(self, new_url, html_content):
        if new_url is None or html_content is None:
            return

        soup = BeautifulSoup(html_content,'html.parser',from_encoding='utf8')

        new_urls = self._get_new_urls(new_url, soup)
        new_data = self._get_new_data(new_url, soup)

        return new_urls, new_data

    def _get_new_urls(self, new_url, soup):
        new_urls = set()
        links = soup.find_all("a", href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_part_url = link["href"]
            new_full_url = urlparse.urljoin(new_url, new_part_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, new_url, soup):
        res_data = {}
        res_data['url'] = new_url
        title_node = soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        return res_data