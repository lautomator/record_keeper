##Record Keeper

Here are a few Django-powered apps that track inventory and keep notes.
They are:

* Publications: books
* Reader: blog
* About (a static page)

###Local Setup
To get this going:
* Install virtualenv and install the requirements:

`virtualenv env`
`source env/bin/activate`
`pip install -r requirements.txt`

* Run the database migrations
python manage.py migrate

* Create a super user
`python manage.py createsuperuser`

* Run the Django server:
`python manage.py runserver`

###Troubleshooting
* Be sure all of the virtualenv requirements are set.
* Verify the virtual environment is running
