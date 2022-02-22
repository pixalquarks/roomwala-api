# ROOMWALA-API  

A RESTful API build on top of Python's [FASTAPI](https://fastapi.tiangolo.com/) framework.

## HOW TO RUN THE PROJECT LOCALLY
Make sure you have git and python(preferably 3.9) installed locally.

### GETTING A LOCAL COPY OF THE REPOSITORY
Start by cloning the master branch onto your local machine
```
git clone https://github.com/pixalquarks/roomwala-api.git
```
Or you can use your prefered method to get a copy of the repository locally.


### GETTING ALL THE DEPENDENCIES
Open the cloned repository in your terminal and create a virtual enviroment.
If you don't know how to create one, simply refer to [this](https://www.geeksforgeeks.org/python-virtual-environment).
Or you can follow this.
```
pip install virtualenv
python -m venv
.\venv\Scripts\activate
```
Now that you can created a virtual enviroment and activated it, you'll have to install all the dependencies.
```
pip install -r requirements.txt
```

### DATABASE INSTALLATION
Now we need a database. SQL database to be precise.
In my case I'm using a MySQL database, but feel free to use your favourite SQL database and things should work pretty much the same.
If you choose to stick with MySQL then follow along.
I'm using Xampp to host my database which you can download from [here](https://www.apachefriends.org/index.html).
And then simply follow the installation guide and you're good to go.
Then open the xampp control panel and run the sql server and that's it.

### SETTING UP ENVIROMENT VARAIBLES
Open the .env.txt file in a text editor and setup the enviroment varaibles accordingly. Refer to [this](./Environment.md) to better unserstand how to setup enviroment variables.
Now rename it to .env

### CREATING DATABASE
This project use [Alembic](https://alembic.sqlalchemy.org/en/latest) as the database migration tool.
To create the database and required tables
```
alembic upgrade head
```

### RUNNING THE SERVER
To run the server, simply enter
```
uvicorn app.main:app
```
This will run the server on your localhost:8000
You can now test the api on postman or you can simply navigate to localhost:8000/docs to get a better, interactive and documented view of all the available routes.

