@echo off

REM This script is used to clean unnecessary generated files/folders.

call :remove_eggs "D3Core"
call :remove_eggs "UcitavanjeKod"
call :remove_eggs "graph_visualiser/data_source_plugin"
call :remove_eggs "graph_visualiser/block_visualiser"
call :remove_eggs "graph_visualiser/data_source_plugin/data_source_plugin_html"
call :remove_eggs "graph_visualiser/data_source_plugin/data_source_plugin_json"

REM remove db
cd "django_project" || exit
del *.sqlite3
cd ..

goto :eof

:remove_eggs
REM The directory path is sent as the first argument
cd %1 || exit
rmdir /s /q build
del /s /q *.egg-info
rmdir /s /q dist
cd ..
goto :eof
