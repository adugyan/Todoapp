<a href="http://fvcproductions.com"><img src="https://avatars1.githubusercontent.com/u/4284691?v=3&s=200" title="FVCproductions" alt="FVCproductions"></a>

<!-- [![FVCproductions](https://avatars1.githubusercontent.com/u/4284691?v=3&s=200)](http://fvcproductions.com) -->


Todoapp
---

### Introduction

A Todo application that will allow users to submit items to a list. There are various lists, for organizational purposes, and once an item is created it can be checked to denote it has been completed and each item will also come with a delete button to clear the list.

### Overview

This app is functional but will still be added to. I plan to have a form to create custom lists as well as including CSS to improve the look of the project.

### Tech Stack

The tech stack I used included:

* **SQLAlchemy ORM** as the ORM library of choice
* **PostgreSQL** as the database of choice
* **Python3** and **Flask** as my server language and server framework
* **Flask-Migrate** for creating and running schema migrations
* **HTML** for the website's frontend

### Main Files: Project Structure

  ```sh
  ├── README.md
  ├── app.py *** the main driver of the app. Includes SQLAlchemy models.
                    "python app.py" to run after installing dependences
  ├── error.log
  ├── requirements.txt *** The dependencies we need to install with "pip3 install -r requirements.txt"
  ├── migrations
  │   ├── 3e805f616c55_.py
  │   ├── 08979bcf4318_.py
  │   ├── da2f29fca445_.py
  │   └── f94e60ef5d2d_.py
  └── templates
      ├── index.html
  ```

  Overall:
  * Models are located in `app.py`.
  * Controllers are also located in `app.py`.
  * The web frontend is located in `templates/`.


  Instructions
  -----
  1. First, [install Flask](http://flask.pocoo.org/docs/1.0/installation/#install-flask) if you haven't already.

    
    $ cd ~
    $ sudo pip3 install Flask
    

  2. Run the development server:
    
    
    $ export FLASK_APP=myapp
    
    $ export FLASK_ENV=development # enables debug mode
    
    $ python3 app.py
    

  3. Navigate to Home page [http://localhost:5000](http://localhost:5000)





- version 1.0
> 7/8/2020
- Included an Ajax fetch method so that input from the user is immediately appended. Page refreshment is no longer needed
- included error handling with try-except-handling pattern
>7/9/2020
Included database migration with Flask-Migrate
  1. Set up folders to store migrations(as versions of the database)
  2. Ran initial migration to create tables and replace the use of db.create_all()
  3. Migrate on changes to our data models
    - Make changes to the SQLAlchemy models
    - Allow Flask-Migrate to auto-generate a migration script based on the changes
    - Fine-tune the migration scripts
    - Run the migration, aka “upgrade” the database schema by a “version”
>7/10/2020 Included update functionality
1. Added checkboxes to the view when new items are added to the list
2. When a user clicks a checkbox it will send out an update request
>7/11/2020
1. Added delete functionality
>7/14/2020
1. Added a new parent table 'todolists'  as well as a foreign key relationship
2. Added new migration files for the added database schema
3. Added a second list named urgent and the option for the user to switch between preferred lists
to organize items
4. Changed page layout
