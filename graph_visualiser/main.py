from graph_visualiser.data_source_plugin.data_source_plugin_html.data_source_plugin_html import DataSourceHTML
from graph_visualiser.data_source_plugin.wiki_data_getter import WikiDataGetter

if __name__ == "__main__":
    plugin = DataSourceHTML("https://en.wikipedia.org/wiki/Formula_1")
    graph = plugin.get_graph()
    print(graph.nodes)
