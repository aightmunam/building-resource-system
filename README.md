# building-resource-system

### Database Design

The database design diagram is as follows:

![Database design](https://github.com/aightmunam/building-resource-system/blob/master/database-design.png?raw=true)

### Project Setup


1. Clone this repo
```
git clone https://github.com/aightmunam/building-resource-system.git
```
2. Create a virtualenv and activate it
```
virtualenv venv
source venv/bin/activate
```
3. Make sure you have Postgres installed. If not, download it from [here](https://www.postgresql.org/download/) and install it.

4. Install all python requirements
```
pip install -r requirements.txt
```
5. Create your Postgres database and user to be used with this project. You will need DB name, DB user with access to this DB, 
and the password. 
```
psql // This will open the Postgres shell

psql> CREATE DATABASE <db_name>;
psql> CREATE USER <db_user> WITH PASSWORD '<db_password>';
psql> GRANT ALL PRIVILEGES ON DATABASE <db_name> TO <db_user>;
```
Once all three have been made, we need to export the following variables into our environment as:
```
DB_NAME=<db_name>
DB_USER=<db_user>
DB_PASSWORD=<db_password>
```
You can either export them by doing `export DB_NAME=<db_name>` in the terminal or you can create a `.env` file in 
the root directory of this project containing the above code.

6. We need to generate and add a variable `SECRET_KEY` to our environment that will act as the project's secret key.
```
python -c "import secrets; print(secrets.token_urlsafe())" 
```
This command will generate a key, now simply export it into the environment or add it to the `.env` file.
```
SECRET_KEY= # Add generated key here
```
7. Now, we need to run the database migrations and run the django server
```
python3 manage.py migrate
python3 manage.py runserver
```

