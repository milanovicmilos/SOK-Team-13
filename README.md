# SOK-Team-13
Ex tensible P latform for S tructure V isualization and N avigation
Project Overview
This Django project consists of two data source plugins and two graph visualizer plugins. The data source plugins are named data_source_plugin_json and data_source_plugin_html, while the graph visualizer plugins are block_visualiser and simple_visualiser. The project utilizes the jinja2 template engine for graph visualization and incorporates web scraping using BeautifulSoup for data retrieval from Wikipedia.

Project Initialization
Prerequisites
Python (>=3.10)
Virtual environment (Optional but recommended)
Initial Setup
Clone the project repository:


git clone https://github.com/SOK-Team-13/django_project.git
cd django_project
Create a virtual environment (optional but recommended):

python -m venv venv
Activate the virtual environment:

On Windows:

venv\Scripts\activate
On Linux/Mac:

source venv/bin/activate
Install project dependencies:

pip install -r requirements.txt
Run the initialization script:

run.bat
Running the Django Application
Navigate to the project directory:

cd django_project
Run the Django migrations:

python manage.py makemigrations
python manage.py migrate
Start the Django development server:

python manage.py runserver
Open your web browser and go to http://127.0.0.1:8000/ to access the Django application.

Used Libraries
Django: A high-level Python web framework for rapid development.
Jinja2: A template engine for Python, used for graph visualization.
BeautifulSoup: A library for pulling data out of HTML and XML files, utilized for web scraping from Wikipedia.
Requests: A popular HTTP library for making requests to external resources.
Project Structure
D3Core: Core library for data visualization.
graph_visualiser/data_source_plugin/data_source_plugin_json: JSON data source plugin.
graph_visualiser/data_source_plugin/data_source_plugin_html: HTML data source plugin.
graph_visualiser/block_visualiser: Block visualizer plugin.
graph_visualiser/simple_visualiser: Simple visualizer plugin.
django_project: Django application directory.
Additional Notes
The run.bat script automates the installation of Python components and runs the Django website. Ensure that the paths in the script are correct for your environment.

If using virtual environments, activate it before running any scripts or Django commands.

Ensure that the required dependencies are installed by running pip install -r requirements.txt.

Customize the Django project according to your needs, and refer to the Django documentation for further guidance: Django Documentation.

