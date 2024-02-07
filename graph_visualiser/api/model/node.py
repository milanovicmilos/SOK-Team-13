from html import unescape
from typing import Any
import re

from bs4 import BeautifulSoup


class Node:

    def __init__(self, node_id: str, data: Any):
        self._node_id = node_id
        self._data = data
        self._parsed_data = self.parse_node_data()

    @property
    def node_id(self) -> str:
        return self._node_id

    @property
    def data(self) -> Any:
        return self._data

    @property
    def parsed_data(self) -> {}:
        return self._parsed_data

    def get_data(self):
        return self._data

    def parse_node_data(self):
        matches = {}
        counter = 0

        # Use BeautifulSoup to parse the HTML
        soup = BeautifulSoup(self._data, 'html.parser')

        # Find all th elements with class infobox-label
        infobox_label_elements = soup.find_all('th', class_='infobox-label')

        for infobox_label_element in infobox_label_elements:
            if counter > 5:
                break
            label_text = infobox_label_element.get_text(strip=True)

            # Find the parent tr element
            tr_element = infobox_label_element.find_parent("tr")
            print(tr_element)
            # Find the next sibling td with the class infobox-data
            infobox_data_element = tr_element.find_next_sibling("tr").find("td", class_="infobox-data")
            print(infobox_data_element)

            if infobox_data_element:
                counter += 1

                # Extract the text content from the infobox-data element
                data_text = unescape(infobox_data_element.get_text(separator=' ', strip=True))
                print(data_text)
                # Check if there is an <a> tag inside infobox-data
                a_tag = infobox_data_element.find("a")
                if a_tag:
                    # If <a> tag is present, extract its text content
                    a_text = unescape(a_tag.get_text(separator=' ', strip=True))
                    matches[label_text] = a_text
                else:
                    # If no <a> tag, use the text content of infobox-data
                    matches[label_text] = data_text

        matches['id'] = self.url_to_valid_name()

        return matches

    def url_to_valid_name(self):
        regex = re.compile(r'[^\/]*(?:\/([^\/#]+))?(?:#([^#]+))?$')
        match = regex.match(self._node_id)

        if match:
            last_segment, fragment = match.groups()
            return fragment if fragment else last_segment

        # If there's no match, return the original URL
        return self._node_id
