from abc import ABC, abstractmethod


class DataSource(ABC):
    def __init__(self, *args, **kwargs):
        # Ovde možete inicijalizovati zajedničke promenljive ili parametre
        pass

    @abstractmethod
    def parse_data(self, data):
        """
        Metoda za parsiranje podataka i formiranje grafa.

        Parameters:
        - data: Podaci iz izvora, kao što su JSON, XML, CSV, itd.

        Returns:
        - Graph: Struktura podataka koja predstavlja graf.
        """
        pass

    @abstractmethod
    def configure(self, *args, **kwargs):
        """
        Metoda za konfiguraciju izvora podataka.

        Parameters:
        - args: Dodatni argumenti potrebni za konfiguraciju.
        - kwargs: Dodatni ključ-vrednost argumenti potrebni za konfiguraciju.
        """
        pass

    @abstractmethod
    def get_required_parameters(self):
        """
        Metoda koja vraća listu obaveznih ulaznih parametara za određeni izvor podataka.

        Returns:
        - List[str]: Lista obaveznih ulaznih parametara.
        """
        pass
