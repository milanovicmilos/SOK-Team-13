@echo off

REM This script is used to build all necessary Python components
REM and run a Django website.

call :lay_egs "./D3Core"
call :lay_egs "./graph_visualiser/data_source_plugin/data_source_plugin_json"
call :lay_egs "./graph_visualiser/data_source_plugin/data_source_plugin_html"
call :lay_egs "./graph_visualiser/block_visualiser"

call :run_server "django_project"
goto :eof

:lay_egs
REM The directory path is sent as the first argument
"C:\Users\Milos\.virtualenvs\SOK-Team-13\Scripts\python.exe" -m pip install %1
goto :eof

:run_server
REM The Django website path is sent as the first argument
cd %1
"C:\Users\Milos\.virtualenvs\SOK-Team-13\Scripts\python.exe" manage.py makemigrations
"C:\Users\Milos\.virtualenvs\SOK-Team-13\Scripts\python.exe" manage.py migrate
"C:\Users\Milos\.virtualenvs\SOK-Team-13\Scripts\python.exe" manage.py runserver
goto :eof