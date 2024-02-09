from setuptools import setup, find_packages


setup(
    name='simple_visualiser',
    version='0.1',
    packages=find_packages(),
    # namespace_packages=['plugin_implementation'],
    install_requires=[
        'beautifulsoup4==4.9.3',
        'requests==2.25.1',
        'jinja2==3.1.3'
    ],
    entry_points={
        'graph_visualiser.visualizer': [
            'simple_visualiser = simple_vis.simple_visualizer:SimpleVisualiser'
        ]
    }
)