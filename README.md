## Task management app 

This is a very simple task management app built using django, html and css.

### Approach

Class-based views for django view functions are used in order to make the code more scalable, readable and reusable.
The class implements the get and post methods in order to dispatch and handle http requests, but it can also have other methods.

There is a utils.py file that contains some logic in order to make the views leaner.

### Database

SQLite is the best choices for the current load and security of the project. The database on the deployed app is separated from the code repository.


### Frontend

As a native backend developer, the frontend code is very simple yet intuitive.
Next to the tasks in progress and in to do, there are two buttons: a tick and a play sign respectively. These buttons are used to move the task to the next status (e.g. to do -> in progress or in progress -> done)
The done tasks can be eliminated by clicking on the lens button and then on the trash.

### Next steps

The app can be improved with better design and also new features, here are some of the new ones that might be added

 - add subtask model
 - implement django messages
 - implement task archiving
 - implement reverse flow on tasks (e.g. in progress -> to do or done -> in progress)
 - add a weight to the tasks

### Run this project

To run this project on your machine follow the following steps:
 - make sure you have python >= 3.10 installed
 - clone the repository and checkout to the development branch
 - create a virtual environment with the following command -> python -m venv venv
 - activate virtual env -> venv/Scripts/activate (on windows) or source venv/bin/activate (on linux)
 - install project dependencies -> pip freeze -r requirements.txt
 - apply migrations to db -> python manage.py migrate
 - run the server on localhost -> python manage.py runserver

and you are ready to go
