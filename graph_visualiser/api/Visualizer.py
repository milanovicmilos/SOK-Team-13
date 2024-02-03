from abc import ABC, abstractmethod

class Visualizer(ABC):
    def __init__(self, graph):
        """
        Konstruktor apstraktne klase za vizualizaciju grafa.

        Parameters:
        - graph (dict): Grafički model koji se koristi za generisanje vizualizacije.
        """
        self.graph = graph

    @abstractmethod
    def generate_html(self):
        """
        Apstraktna metoda koja generiše HTML reprezentaciju grafa.

        Returns:
        - str: HTML string koji predstavlja vizualizaciju grafa.
        """
        pass
