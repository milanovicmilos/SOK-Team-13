from graph_visualiser.api.data_source import DataSource


class DataSourceHTML(DataSource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def parse_data(self, data):
        """
        Method for parsing HTML data and forming a graph.

        Parameters:
        - data: HTML data from the source.

        Returns:
        - Graph: Data structure representing a graph.
        """
        # Implement the logic for parsing HTML data here
        pass

    def configure(self, *args, **kwargs):
        """
        Method for configuring the HTML data source.

        Parameters:
        - args: Additional arguments needed for configuration.
        - kwargs: Additional key-value arguments needed for configuration.
        """
        # Implement the logic for configuring the data source here
        pass

    def get_required_parameters(self):
        """
        Method that returns a list of required input parameters for the HTML data source.

        Returns:
        - List[str]: List of required input parameters.
        """
        # Implement the logic for getting the required parameters here
        pass
