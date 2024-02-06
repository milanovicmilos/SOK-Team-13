from setuptools import setup, find_packages

setup(
    name="visualiser_app",
    version="0.1",
    packages=find_packages(),
    # requiring Django later than 2.1
    install_requires=['Django>=2.1'],
    # Installing package data related to package
    # https://docs.python.org/3/distutils/setupscript.html#installing-package-data
    # data_files specify additional files that are not closely related to the
    # source code of the package.
    # https://docs.python.org/3/distutils/setupscript.html#installing-additional-files
    package_data={'visualiser_app': ['static/*.css', 'static/*.js', 'static/*.html', 'templates/*.html']},
    zip_safe=False
)