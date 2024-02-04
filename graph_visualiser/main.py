from graph_visualiser.data_source_plugin.wiki_data_getter import WikiDataGetter

if __name__ == "__main__":
    wiki_data_getter = WikiDataGetter('https://en.wikipedia.org/wiki/Formula_One')

    html_content, links = wiki_data_getter.get_html_data()
    print(html_content)
    # print(len(html_content['links']))
    print(links)

