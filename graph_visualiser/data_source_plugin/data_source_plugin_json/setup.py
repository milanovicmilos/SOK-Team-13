from setuptools import setup, find_packages

setup(
    name='data_source_plugin_json',
    version='0.1',
    packages=find_packages(),
    namespace_packages=['plugin_implementation'],
    install_requires=[
        'beautifulsoup4==4.9.3',
        'requests==2.25.1'
    ],
    entry_points={
        'graph_visualiser.data_source': [
            'json=plugin_implementation.data_source_plugin_json_implementation:DataSourceJSON'
        ]
    }
)
