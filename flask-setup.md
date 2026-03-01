https://flask.palletsprojects.com/en/stable/quickstart/ 

1. create project folder/working directory
2. vscode: CTRL + P > ">" > "Python: Create Environment"
3. dirs setup:  
    > .venv
    v project_name
        app.py
        requirements.txt
        documentation.md
        ...
4. cd outside project dir
5. ".\.venv\Scripts\Activate"
6. cd project dir
7. "pip install flask"
8. "pip freeze > requirements.txt"
9. script app.py 
10. TO RUN
        "flask --app app run"     OR  "flask run" IF .py file is named wsgi/app.py
    DEBUG mode
        "flask --app app run --debug"

db - PostgreSQL