# PyREST
Below you'll find instructions for 
1. Using Postman to test this project
2. Running the project from Docker
3. Running the project from a Terminal (command-line)
4. Running the project in Docker


## Postman
This repo uses Postman environments. It allows the API tests to be the same by just selecting an Environment to populate variables which change. (For example, the API URL will likely change with new deployments.)

### Environment files
- Localhost.postman_environment.json

### API Collection files
These files use environment variables defined in the files above
- Python Flask Demo.postman_collection.json

There are 3 simple endpoints in the App which differ only by the HTTP Request Method
-  GET
-  POST
-  PUT


## Running from a terminal
Running the demo from the commandline is two steps
- activate virtual environment
- run the flask app

Specific OS Instructions:
### windows
```
pipenv install -r requirements.txt
.venv\Scripts\activate
python -m flask run
```

### linux
```
pipenv install -r requirements.txt
source .venv\Scripts\activate
python -m flask run
```

Success looks something like this:
```
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

## Running in Docker
You'll need to have Docker installed.

```
docker build -t pyrestdemo .
docker run -d -p 5000:5000 pyrestdemo
```
