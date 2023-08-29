## Django Project Startup Basics

- Create A folder navigate there open cmd and write "virtualenv env" (make sure you have virtualenv installed before installation command pip install virtualenv,check version command virtualenv --version)
- Type "source ./env/Scripts/activate" to activate the virtual environment
- Type "django-admin startproject main" to create a project
- Navigate to main folder by cd main and create a app by "django-admin startapp home"
- Type "python manage.py runserver" to start the server
- If we want to install a prowe have to go to the root folder by "cd .." and install the project

## Django Project Structure

- Firstly our main focus will be projects "urls.py" and "views.py" (if this not exists we have to create it)
- In "urls.py" we have to define a route and a function which will send response to that route
- We can inlclude a entire application's urls via main adding the application in "settings.py" Apps list
- To send html files in response we have to create a "template" folder on any app of our project and we can send all apps html file from there
- We can also create a "common" folder in our projects root to use common html in our website
- We can calculate our data in python and send it to html file but we can also calculate our data in html file django template filter. We can folllow this link [Learn Django Filters](https://www.geeksforgeeks.org/django-template-filters/) and [Learn Django Tags](https://www.geeksforgeeks.org/django-template-tags/?ref=lbp)
- We can create a common html file on root folders template and then we can extend it on other html files
- In our application folder we can create our custom filters and use it . The folder name should be "templatetags"
- We can create our custom template with the combination custom filters
