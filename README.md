=====================================================
Dojo Dev Camp - Django/Angular E-commerce Application
=====================================================

This project is broken into branches that help to define
new functional pieces.  It is based on the e-commerce
application in Coding For Entrepreneurs

Cloning the Repository to GitHub
--------------------------------
- Create an empty repository at GitHub (let's call it test)
- Open up your terminal
- Run the following commands

```
cd /tmp # make sure this is a directory that exists
git clone --bare git@github.com:rooeydaniel/angular_django_ecommerce.git
cd angular_django_ecommerce.git
git push --mirror git@github.com:test.git # this will be different for you
cd ..
rm -rf angular_django_ecommerce.git
```

Branch v1
---------
This shows the initial structure for a Django application that uses
best practices derived from the instructor's own coding experience
and lessons from Two Scoops of Django.  An explanation of each branch's
directory structure will be explained as follows (with each corresponding
explanation only including the changes made from the previous branch(es).

apps/
    public/
    project/
        confs/
            urls.py                     - Handles our route for the Django admin, static files, and our base.html file
            wsgi.py                     - Used by Heroku to handle collecting static files, etc.
        requirements/
            base.txt                    - Common PIP dependencies between dev, prod and test environments
            dev.txt                     - Any dev (local) dependencies that shouldn't be in any other environment
            prod.txt                    - Ditto
            test.txt                    - Ditto
        settings/
            dev.py                      - Handles settings local to that environment, should be a copy of local_settings.py.example
            base.py                     - Django settings that are used everywhere, anything overwritten should happen in your local settings file
    static/
        assets/
            common/                     - Will house assets common to all apps
                lib/                    - this houses the front-end dependencies installed by Bower
                                        * Note: .bowerrc defines where these dependencies get installed
            public/                     - Will house assets specific to the public app
        templates/
            base.html                   - Base template for the entire application
    .bowerrc                            - Tells Bower where to install the front-end dependencies
    .gitignore                          - Anything listed in here will not get committed to your Git repository
    bower.json                          - Used by Bower, it defines the front-end packages you want in your project
    manage.py                           - Django's management script
    package.json                        - Used by Node's NPM - will install Bower, is run by Heroku automatically
    Procfile                            - Used by Heroku to determine what process to run when app is deployed
    README.md                           - The current file
    requirements.txt                    - Should be set to the appropriate environment - will get run automatically in Heroku

### Steps to run this branch locally
1. Create a virtual environment
2. Install required PIP packages in your project directory

```
$ pip install -r project/requirements/dev.txt  # Please read note below if you use OS X Mavericks
```

* Note: As of March 27, 2014, the command above will fail on OS X Mavericks, following is the command you want to run:
* http://stackoverflow.com/questions/22313407/clang-error-unknown-argument-mno-fused-madd-python-package-installation-fa

* Note: To uninstall all PIP packages - pip freeze | xargs pip uninstall -y

```
ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future pip install -r project/requirements/dev.txt
```

3. Install NPM and Bower packages  in your project directory

```
$ npm install
```

4. Run initial database sync

```
$ python manage.py syncdb  # Create a super user
```

5. Start up the Django internal server in your project directory

```
$ python manage.py runserver --settings=project.settings.dev
```

6. Open up your browser to http://localhost:8000 and you should see a generic home page

Branch v2
---------
This branch will introduce User Authentication through Django, along with User Account Creation.
Here are the new additions:

1. We modified base.html and added some Django template blocks.  The main components were the login link, logout link,
and My Account links.

2. We modified the main urls.py file to include a new urls.py from our public app.

3. We added a new urls.py file to our public app to handle the new home and login links.

4. We added a new views.py file to our public app to handle the new home and login views.

5. We created a new templates folder with login.html and home.html files in our public app.

6. We added some custom styles to app.css to help with the login form and follows the starter template from Bootstrap.

7. We modified the login view to handle both the rendering of the login page and the authentication of a user.  Once
authenticated, you should see your Full Name with a link for logout and My Account.

8. We added the create_user view to handle the new user form and posting of new user information.

9. We added the edit_user view to handle my account details and posting of new user information.

### Steps to run this branch locally
1. Activate your virtual environment and checkout the v2 branch

```
$ cd ~/path/to/project
$ . ~/.virtualenvs/angular_django_ecommerce/bin/activate
$ git checkout v2
```

2. Install required PIP packages in your project directory

```
$ pip install -r project/requirements/dev.txt  # Please read note below if you use OS X Mavericks
```

* Note: As of March 27, 2014, the command above will fail on OS X Mavericks, following is the command you want to run:
* http://stackoverflow.com/questions/22313407/clang-error-unknown-argument-mno-fused-madd-python-package-installation-fa

* Note: To uninstall all PIP packages - pip freeze | xargs pip uninstall -y

```
ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future pip install -r project/requirements/dev.txt
```

3. Install NPM and Bower packages  in your project directory

```
$ npm install
```

4. Start up the Django internal server in your project directory

```
$ python manage.py runserver --settings=project.settings.dev
```

5. Open up your browser to http://localhost:8000 and you should see a generic home page

Deploying to Heroku (WIP - does NOT work yet)
---------------------------------------------
These instructions should work across all branches

1. Create a new heroku account at heroku.com (if you don't already have one)
2. Install the heroku toolbelt on your machine
3. Inside a terminal/command prompt, change to your project directory and log into heroku

```
$ cd /path/to/project
$ heroku login
$ heroku plugins:install https://github.com/naaman/heroku-vim # Allows us to use heroku vim to edit files remotely
```

4. Create a new heroku dyno/project/app

```
$ heroku create cc-ecommerce --buildpack=https://github.com/rooeydaniel/heroku-buildpack-django.git
```

4. Add your SECRET_KEY to your heroku environment

```
$ heroku config:set SECRET_KEY=  # Makes sure you actually set a secret key
$ heroku config:get SECRET_KEY  # this will be a sanity check that it actually was set
```

5. Push your branch to Heroku (or master)

```
$ git push heroku [BRANCH_NAME]  # e.g. v1
$ heroku open # run this once the previous command finishes, it may take a minute
$ heroku logs --tail  # this allows you to watch the logs out at Heroku to see if anything goes way wrong
$ heroku ps:scale web=1
```