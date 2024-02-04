from itertools import islice
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


class WikiDataGetter:
    def __init__(self, url):
        self.url = url

    def set_url(self, url):
        self.url = url

    def get_soup(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            return BeautifulSoup(response.content, 'html.parser')
        else:
            print(f'Error: {response.status_code}')
            return None

    def get_body_content_div(self):
        soup = self.get_soup()
        if soup:
            return soup.find('div', {'id': 'bodyContent'})
        return None

    def get_node_html_data(self):
        body_content_div = self.get_body_content_div()

        if body_content_div:
            links = set(islice(
                (urljoin(self.url, link.get('href')) for link in body_content_div.find_all('a', href=True) if
                 '/wiki' in link.get('href') and not link.get('href').endswith(('.png', '.jpg', '.jpeg', '.svg'))),
                10))

            return body_content_div.prettify(), links
        else:
            print("Div with id 'bodyContent' not found.")
            return None, None

    def get_node_json_data(self):
        body_content_div = self.get_body_content_div()

        if body_content_div:
            links = set(islice(
                (urljoin(self.url, link.get('href')) for link in body_content_div.find_all('a', href=True) if
                 '/wiki' in link.get('href') and not link.get('href').endswith(('.png', '.jpg', '.jpeg', '.svg'))),
                10))

            html_content, links = body_content_div.prettify(), links
            data = {
                "html_content": html_content,
                "links": links
            }

            json_data = {
                "id": self.url,
                "data": data["html_content"],
                "links": data["links"]
            }

            return json_data
        else:
            print("Div with id 'bodyContent' not found.")
            return None
