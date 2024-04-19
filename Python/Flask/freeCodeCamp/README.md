# freeCodeCamp - Learn Flask for Python

## How To Run
1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command:
```
$ .\env\Scripts\activate
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

5. Finally start the web server:
```
$ (env) python app.py
```

This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```

## Notes:
- Make sure you have the following installed
    - Globally:
        - Python
        - virtualenv (`pip3 install virtualenv`)
    - Within enviroment:
        - Flask and SQLalchemy (`pip3 install flask flask-sqlalchemy`)
- To set up enviroment run ```virtualenv env`
- To activate the enviroment run `source env/bin/active`
- To create the database, open the in terminal python (using `python3`) then run the following lines 
```python
from app import db, app
app.app_context().push()
db.create_all()
exit()
```
- To run the app `python3 app.py`
- Deploying to heroku:
    - Download Heroku CLI (command line interface)
    ``` 
    $ heroku login
    $ pip3 install gunicorn
    ```
    - Create a file called `Procfile` and add the following `web:guincorn app:<app-filename>`
    ```
    $ pip3 freeze > requirements.txt
    ```
    - Create git repository, add and commits files
    ```
    $ heroku create application-name
    $ git push heroku master
    ```
