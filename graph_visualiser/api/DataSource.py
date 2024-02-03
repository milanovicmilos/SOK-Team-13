from abc import ABC, abstractmethod


class DataSource(ABC):
    def __init__(self, *args, **kwargs):
        # Here you can initialize common variables or parameters
        pass

    @abstractmethod
    def parse_data(self, data):
        """
        Method for parsing data and forming a graph.

        Parameters:
        - data: Data from the source, such as JSON, XML, CSV, etc.

        Returns:
        - Graph: Data structure representing a graph.
        """
        pass

    @abstractmethod
    def configure(self, *args, **kwargs):
        """
        Method for configuring the data source.

        Parameters:
        - args: Additional arguments needed for configuration.
        - kwargs: Additional key-value arguments needed for configuration.
        """
        pass

    @abstractmethod
    def get_required_parameters(self):
        """
        Method that returns a list of required input parameters for a specific data source.

        Returns:
        - List[str]: List of required input parameters.
        """
        pass
