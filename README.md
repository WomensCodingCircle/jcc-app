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
successfully, you should be able to start the application with

`python src/home.py`

Now just open the URL which is printed out after 'Running on..' in a browser
and you'll see your Flask app there!
