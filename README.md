# Overview
This Django project is designed to manage tasks and tags. It provides an admin interface to create, update, and delete tasks and tags.

## Prerequisites

Before running the project, ensure that you have the following prerequisites installed on your system:

+ Python (version 3.6 or higher)
+ Django (version 3.2 or higher)

## Installation
1. Clone the repository or download the project source code.

2. Open a terminal or command prompt and navigate to the project's root directory.

3. Create a virtual environment (optional but recommended):
```shell
python -m venv env
```
4. Activate the virtual environment:
+ For Windows:
```shell
env\Scripts\activate
```
+ For Unix/Linux:
```shell
source env/bin/activate
```
5.Install project dependencies:
```shell
pip install -r requirements.txt
```
## Configuration
1.Open the settings.py file located in the your_project/your_project directory.

2.Update the database configuration if needed. By default, the project uses the SQLite database, which is suitable for development purposes.

3.Optionally, you can set up an email backend to enable email notifications for tasks. Update the EMAIL_BACKEND, EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, and EMAIL_USE_TLS settings accordingly.

## Database Setup
1. Apply database migrations:
```shell
python manage.py migrate
```

2. (Optional) Create a superuser account to access the admin interface:
```shell
python manage.py createsuperuser
```
## Running the Project
1. Start the Django development server:
```shell
python manage.py runserver
```

2. Open a web browser and access the local development server at http://localhost:8000/.

3. To access the admin interface, append /admin to the URL (e.g., http://localhost:8000/admin). Log in using the superuser credentials created earlier.

## Usage
In the admin interface, you can create, update, and delete tasks and tags.
Tasks have fields such as title, description, tags, created date, due date, and status.
Tags can be associated with multiple tasks.
The changelist view allows you to view and filter tasks based on status and due date.
Use the search field to search for tasks based on title and description.
