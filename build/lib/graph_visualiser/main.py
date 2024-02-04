import pkg_resources


def load_plugins(url, group):
    plugins = []

    list_of_entry_points = list(pkg_resources.iter_entry_points(group=group))
    print(list_of_entry_points)

    for ep in pkg_resources.iter_entry_points(group=group):
        o = ep.load()
        parser = o(url)
        plugins.append(parser)

    return plugins


def main():
    try:
        plugins = load_plugins("https://en.wikipedia.org/wiki/Formula_1", "graph_visualiser.data_source")
        if not plugins:
            print("No plugins found")
            return
        for plugin in plugins:
            print(plugin)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Formula_1"
    main()
