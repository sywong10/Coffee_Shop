# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
   - in API Settings:
     - Enable RBAC
     - Enable Add Permissions in the Access Token
5. Create new API permissions:
   - `get:drinks`
   - `get:drinks-detail`
   - `post:drinks`
   - `patch:drinks`
   - `delete:drinks`
6. Create new roles for:
   - Barista
     - can `get:drinks-detail`
   - Manager
     - can perform all actions
7. Test your endpoints with [Postman](https://getpostman.com).
   - Register 2 users - assign the Barista role to one and Manager role to the other.
   - Sign into each account and make note of the JWT.
   - Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
   - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
   - Run the collection and correct any errors.
   - Export the collection overwriting the one we've included so that we have your proper JWTs during review!


## start up backend

source venv/bin/activate
cd starter_code/backend/src
export FLASK_APP=api.py
flask run --reload


##  below are two JWT tokens with permissions needed for barista and manager to manage coffee shop.
##

JWT for barista and manager

barista JWT:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZEcm9MaTFHM3ZOQzZLNllQRlhkMiJ9.eyJpc3MiOiJodHRwczovL3N5d29uZ2lhbS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI3NTAyYzgwOWJiMGQwMDY4ZTUwNTkzIiwiYXVkIjoiY29mZmVlYXBpIiwiaWF0IjoxNjUzNTIyNDUxLCJleHAiOjE2NTM1Mjk2NTEsImF6cCI6IkNIVll3OTlWSmREZVFST2g2WWNoQ0padmFsQlBhZU1HIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.XoGMlJk0uxOwTqSFXzscmFShKbUcs-QJdKNZ5l8eCsZtQm0AJ3FdzCCF8ni2_DVfXhZslEg7vcQLrg9ADBkoHLYtS_A2XQz_Db_2Gxq-S01US0pAL3lCh5E8p74222I5NN2G4hmduVkTCL6f3yQ646ZRx2FMcReWFpkk5nrhBf3a1R2SqrKC7oGXDbRNEl3UDORJ5Ldwj9VNMjZ3LAAjxV5OI0MBHw-bB0dTSPJ34ivIJKPtgauhS0GR0Spcz_HcQvl2I8FqWWDTiQuSmD8RhcqJoc1P0UgCeWpm-gY2vbZNP7FLSTPyJ6oD-oZxxONsRWRCGl-YEwLuh5_XycqxdA

manager JWT:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZEcm9MaTFHM3ZOQzZLNllQRlhkMiJ9.eyJpc3MiOiJodHRwczovL3N5d29uZ2lhbS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI3NjI5MzM0Y2JmYTAwMDZlNmY1ZjNlIiwiYXVkIjoiY29mZmVlYXBpIiwiaWF0IjoxNjUzNTI1NjE2LCJleHAiOjE2NTM1MzI4MTYsImF6cCI6IkNIVll3OTlWSmREZVFST2g2WWNoQ0padmFsQlBhZU1HIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.QmQqh7cnwo3wyHZ6Rr-I0c5CFvrS6FlcZLqlv95B2R8gb8pYVClvxNiSMAW7qHO9UWv-QQEVGmZnuyppksb8gXdaWTQaGYr7mHNTAMCDyXpmI2hcKuN_bgB9d8sjsEj5-v2mMhiyI--Op9tuhUjmG5pWMY_QhO6JW328djYndKvZsViNO8qXDECnJlKSFmWQ_pr8JTAD_lEFDPDVAUvdsrTI23XVcVWtC5wSWLn8MOXyoO21skFpZ7mAIyVPJroiZdrYU2xRYcSoCqNvUJRB15U3rXOsu7566Hr8qxTo2K0JREd0j_DfbRzO1PuS1AUV-QmQuEobH1_r6f4zr8Z6XA


### Implement The Server

There are `@TODO` comments throughout the `./backend/src`. We recommend tackling the files in order and from top to bottom:

1. `./src/auth/auth.py`
2. `./src/api.py`

### In ./src/auth/auth.py file

- contains auth0 domain, algorithms and api_audience in application in auth0 

AUTH0_DOMAIN = 'sywongiam.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'coffeeapi'

- auth.py file also contains functions to validate JWT token.  These functions are from
Identity and Access Management class.


###  In api.py file, it contains different endpoints

Endpoints

GET '/drinks'
- fetch drink list
- this endpoint is a public endpoint and does not require permission
- return an object with drink.short() data and status code
  {
      "drinks": [
          {
              "id": 1,
              "recipe": [
                  {
                      "color": "blue",
                      "name": "water",
                      "parts": 1
                  }
              ],
              "title": "water"
          }
      ],
      "success": true
  }


GET '/drinks-detail'
- fetch long drink list
- this endpoint requires "get:drinks-detail" permission
- return an object with drink.long() data and status code
- {
    "drinks": [
        {
            "id": 1,
            "recipe": [
                {
                    "color": "blue",
                    "name": "water",
                    "parts": 1
                }
            ],
            "title": "water"
        }
    ],
    "success": true
}




POST '/drinks'
- add a new drink and its recipe
- this endpoint requires 'post:drinks' permission
- return an object of newly added drink and its recipe and status code 
- {
    "drinks": {
        "id": 2,
        "recipe": {
            "color": "blue",
            "name": "Water",
            "parts": 1
        },
        "title": "Water3"
    },
    "success": true
}



PATCH '/drinks/<int:id>'
- update an existing drink in database with corresponding id 
- this enpoint requires 'patch:drinks' permission
- this endpoint returns object of updated drink, its drink.long() data and status code

    {
        "drinks": {
            "id": 4,
            "recipe": null,
            "title": "Water4"
        },
        "success": true
    }

  


DELETE '/drinks/<int:id>'
- deletes existing drink with intended id in database 
- this endpoint requires 'delete:drinks' permission
- this endpoint returns object that contains deleted id and status

    {
        "delete": 3,
        "success": true
    }





