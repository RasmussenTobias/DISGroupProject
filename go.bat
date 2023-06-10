@echo off

REM Call the Python file and capture the output
for /f "tokens=1* delims==" %%a in ('python connectionAuth.py') do (
    if "%%a"=="username" set username=%%b
    if "%%a"=="database" set database=%%b
    if "%%a"=="host" set host=%%b
    if "%%a"=="port" set port=%%b
)

REM Run SQL file using psql
psql -h %host% -p %port% -U %username% -d %database% -f "sql_schema.sql"