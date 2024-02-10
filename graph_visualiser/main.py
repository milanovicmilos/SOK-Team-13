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

        print("Available plugins:")
        for i, plugin in enumerate(plugins, start=1):
            print(f"{i}. {plugin}")

        while True:
            user_input = input("Choose a plugin number (or 'q' to quit): ")

            if user_input.lower() == 'q':
                print("Exiting program.")
                break

            try:
                plugin_number = int(user_input)
                if 1 <= plugin_number <= len(plugins):
                    selected_plugin = plugins[plugin_number - 1]
                    print(f"You selected: {selected_plugin}")
                    graph = selected_plugin.get_graph()
                    print("Graph created successfully.")
                    print(graph)
                else:
                    print("Invalid plugin number. Please choose a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number or 'q' to quit.")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Formula_1"
    main()
