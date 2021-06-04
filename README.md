Auction - platform to support streamers in their e-commerce journey
---

### Installation & Requirements

git and pip3 is assumed to be installed

    pip3 install pipenv
    pipenv install
    
### Create the database and user

PostgreSQL is assumed to be installed

If you have a Postgres user already created run `createdb dbname` to create a new database.

If not, type this commands in terminal to create a user, database and provide needed privileges:

    createuser projectuser
    createdb dbname
    psql -c "alter user projectuser with encrypted password 'password';"
    psql -c "grant all privileges on database dbname to projectuser;"

### Getting Started & How to Run

copy & rename the .env.example file to .env in the same dir and populate it with your data

then run

    pipenv shell
    ./manage.py runserver
    
    
   ### Setting up linters and fixers. 

Flake8 is a linter. Typing flake8 example.py in terminal will show mistakes, unused imports and etc. Works only on Python code, default settings.

Black is a fixer. Typing black example.py in terminal will automatically fix code. Works only on Python code. We are using default settings.

Optional:
Also you can set up Black in PyCharm, so it will edit code automatically. Here is a guide:

1.Make sure you have the File Watchers plugin installed.

2.Go to Preferences or Settings -> Tools -> File Watchers and click + to add a new watcher/custom template:

3.Name: Black

4.File type: Python

5.Scope: Project Files

6.Program: <Here you should enter path. You can find it by typing in terminal: "which Black" >

7.Arguments: $FilePath$

8.Output paths to refresh: $FilePath$

9.Working directory: $ProjectFileDir$
