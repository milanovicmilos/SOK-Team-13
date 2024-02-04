from itertools import islice
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


class WikiDataGetter:
    """
    Class for getting data from Wikipedia.
    """
    def __init__(self, url):
        self.url = url

    def set_url(self, url):
        """
        Method for setting the URL of the data source.
        :param url:
        :return:
        """
        self.url = url

    def get_soup(self) -> BeautifulSoup or None:
        """
        Method for getting the soup from the data source.
        :return:
        """
        response = requests.get(self.url)

        if response.status_code == 200:
            return BeautifulSoup(response.content, 'html.parser')
        else:
            print(f'Error: {response.status_code}')
            return None

    def get_body_content_div(self) -> BeautifulSoup or None:
        """
        Method for getting the body content div from the data source.
        :return:
        """
        soup = self.get_soup()
        if soup:
            return soup.find('div', {'id': 'bodyContent'})
        return None

    def get_node_html_data(self) -> str or None:
        """
        Method for getting the HTML content of the node.
        :return:
        """
        body_content_div = self.get_body_content_div()

        if body_content_div:
            links = set(islice(
                (urljoin(self.url, link.get('href')) for link in body_content_div.find_all('a', href=True) if
                 '/wiki' in link.get('href') and not link.get('href').endswith(('.png', '.jpg', '.jpeg', '.svg'))),
                5))

            return body_content_div.prettify(), links
        else:
            print("Div with id 'bodyContent' not found.")
            return None, None

    def get_node_json_data(self) -> dict or None:
        """
        Method for getting the JSON data of the node.
        :return:
        """
        body_content_div = self.get_body_content_div()

        if body_content_div:
            links = set(islice(
                (urljoin(self.url, link.get('href')) for link in body_content_div.find_all('a', href=True) if
                 '/wiki' in link.get('href') and not link.get('href').endswith(('.png', '.jpg', '.jpeg', '.svg'))),
                5))

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
