from setuptools import setup, find_packages


setup(
    name='data_source_plugin_html',
    version='0.1',
    packages=find_packages(),
    # namespace_packages=['graph_visualiser.data_source_plugin_html'],
    install_requires=[
        'beautifulsoup4==4.9.3',
        'requests==2.25.1'
    ],
    entry_points={
        'graph_visualiser.data_source': [
            'html=data_source_plugin_html:DataSourceHTML'
        ]
    }
)
