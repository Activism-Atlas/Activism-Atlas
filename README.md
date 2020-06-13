# Activism-Atlas

## Table of Contents
* [Technologies](#technologies)
* [Setup](#setup)

## Technologies
* Postgresql
* Python version: 3.7.3
* Django version: 2.2.13
...

## Setup

From hereafter, the main repository directory will just be described as "main directory".

1. Install the following:
    * Python
    * pip
    * pyenv, pyenv-virtualenv
        * After installation, make sure you've added the following to the end of your `.zshrc` or `.bashrc`:
        ```
        if which pyenv > /dev/null; then eval"$(pyenv init -)"; fi
        if which pyenv-virtualenv-init > /dev/null; then eval"$(pyenv virtualenv-init -)"; fi
        ```
    * PostgreSQL - Please make sure the server works after installation. [How to check if server works](https://tableplus.com/blog/2018/10/how-to-start-stop-restart-postgresql-server.html)
    * npm...

2. Install the correct Python version using pyenv:
    * In your terminal, run `pyenv install 3.7.3`

3. Setup your virtualenv:
    * Make sure you're in the main directory in your terminal.
    * Run the following command to create the virtualenv with correct Python version:
        * `pyenv virtualenv 3.7.3 <name of virtualenv>`
            * E.g., `pyenv virtualenv 3.7.3 activism-atlas`
    * Run the following to set the virtualenv to the current directory:
        * `pyenv rehash`
        * `pyenv local <name of virtualenv>`
            * E.g., `pyenv local activism-atlas`
    * Check that the virtualenv has been set by running:
        * `pyenv version`
            * Should show something like `activism-atlas (set by ...`

4. Install dependencies:
    * Make sure you're in the main directory in your terminal.
    * Run `pip install -r requirements.txt`

5. Create your Postgresql database:
    * In your terminal (doesn't have to be main directory), [start the Postgresql service](https://tableplus.com/blog/2018/10/how-to-start-stop-restart-postgresql-server.html)
        * Your terminal prompt should change to something like: `<username>=#`
    * Run the following lines:
        * `CREATE DATABASE postgres;`
            * Make sure the DB has been created by running `\list`. The `postgres` name should show up.
        * `CREATE USER postgres;`
        * `GRANT ALL PRIVILEGES ON DATABASE postgres TO postgres;`
        * Exit the server shell.

6. Setup Django credentials:
    * Make sure you're in the main directory in your terminal.
    * Run the following command to generate a new secret key:
        * `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
    * The in "atlas" folder within the main directory, there is a `.env_example`. Using the key printed out in the step above, follow the directions in the `.env_example` file.

7. RUN IT!
    * Make sure you're in the main directory in your terminal.
    * Run `python manage.py runserver`
    * Head over to [http://localhost:8000](http://localhost:8000)
    * You should see a Django-created page.
    * Ctrl+c in your terminal to exit.

8. Run migrations:
    * Make sure you're in the main directory in your terminal.
    * There are initial models (tables) that come with Django and need to be created.
    * Run `python manage.py makemigrations`
        * This is a needed step WHENEVER you create/edit models.
    * Run `python manage.py migrate`
        * Also a needed step WHENEVER you create/edit models. Or else the database won't update.

9. Create a Django admin superuser:
    * Make sure you're in the main directory in your terminal.
    * Run `python manage.py createsuperuser`
    * Enter the credentials as prompted.
    * This step is necessary to access Django admin: [http://localhost:8000/admin](http://localhost:8000/admin).
    * Django admin is where you'll be able to see/interact with the database in the browser.
    * Nothing really there besides out-of-the-box Django stuff in the beginning.

#### For front-enders:
There is a folder called "frontend" in the main directory. This is your playground!
You need to have the Django app running (i.e., `python manage.py runserver`) if you want access to the APIs that the backend team is building out. The based URL is `localhost:8000/api`. Will explain more as we progress.


## License
[MIT](https://choosealicense.com/licenses/mit/)