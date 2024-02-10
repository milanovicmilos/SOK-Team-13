from setuptools import setup, find_packages

setup(
    name='graph_visualiser',
    version='0.1',
    packages=find_packages(),
    # namespace_packages=['graph_visualiser', 'graph_visualiser.data_source_plugin'],
    install_requires=[
        'beautifulsoup4==4.9.3',
        'requests==2.25.1'
    ],
    entry_points={
        'console_scripts': [
            'graph_visualiser=graph_visualiser.main:main'
        ]
    }
)
