<a href="http://fvcproductions.com"><img src="https://avatars1.githubusercontent.com/u/4284691?v=3&s=200" title="FVCproductions" alt="FVCproductions"></a>

<!-- [![FVCproductions](https://avatars1.githubusercontent.com/u/4284691?v=3&s=200)](http://fvcproductions.com) -->


# Todoapp

> Basic MVC flow. From the view the user can insert input, and submit to a post route (/todo/create). That goes to the post request listener on the controller side. The controller will then manipulate our model, and grab the latest model from our database to become the new view.


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
