# jcc-app
A web app for the Janelia Charity Club

## How to use this repo

This web app makes use of the python flask web framework. Please make sure you have Python 3 installed on your system.

First of all, clone the repo to your local computer. In a command line, type

`git clone git@github.com:WomensCodingCircle/jcc-app.git`

### Build a dev environment using virtualenv

Navigate to the folder jcc-app, then type

`virtualenv --no-site-packages env`

`source env/bin/activate`

`pip install --upgrade pip`

`pip install -r requirements.txt`

If you get an error with the itsdangerous package, type

`pip install git+https://github.com/pallets/itsdangerous.git@master\##egg\=itsdangerous`

and just install the requirements textfile again. If the installation runs
successfully, you need to run a database migration. Set the FLASK_APP environment variable with

`export FLASK_APP=app/__init__.py`

Then run the database migration with

`flask db upgrade`

If that worked out, you should be able to start the application with

`python run.py`

Now just open the URL which is printed out after 'Running on..' in a browser
and you'll see your Flask app there!

#### Migrate database after changes to the model

If you changed the data model of the application, you need to run the database migration again. If you haven't done so already,
set the FLASK_APP environment variable

`export FLASK_APP=app/__init__.py`

Create a migration:

`flask db migrate`

Apply the migration:

`flask db upgrade`

### Update the application on our VM

Log into the VM and find the app under

`/var/www/projects/jcc-app`

Get the latest version of the app from Github:

`git fetch`

`git rebase origin/master`

Reload the service for the app:

`sudo systemctl restart jcc-app`