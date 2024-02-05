@echo off

REM This script is used to build all necessary Python components
REM and run a Django website.

call :lay_egs "./D3Core"
call :lay_egs "./graph_visualiser/data_source_plugin/data_source_plugin_json"
call :lay_egs "./graph_visualiser/data_source_plugin/data_source_plugin_html"

call :run_server "django_project"
goto :eof

:lay_egs
REM The directory path is sent as the first argument
pip install %1
goto :eof

:run_server
REM The Django website path is sent as the first argument
cd %1
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
goto :eof
