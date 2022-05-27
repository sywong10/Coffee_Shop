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
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZEcm9MaTFHM3ZOQzZLNllQRlhkMiJ9.eyJpc3MiOiJodHRwczovL3N5d29uZ2lhbS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI3NTAyYzgwOWJiMGQwMDY4ZTUwNTkzIiwiYXVkIjoiY29mZmVlYXBpIiwiaWF0IjoxNjUzNjQ4Nzc1LCJleHAiOjE2NTM2NTU5NzUsImF6cCI6IkNIVll3OTlWSmREZVFST2g2WWNoQ0padmFsQlBhZU1HIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.GoMNK8KLK6NwtiK0zB8HLUkdli_lxYNQxU9OFmVVtUd6sAeSnePoS3wEA0AqPfJFm1AVxVIEHyJd16L73O40EQCJp6-bQKLFp80Im1bTWIBITTXHbGMbpGzXXsFQuUGxdyycRT_c5JIEZHlUreF-bV1G5zscm0aMLMut3VBiDyFLY5GJCw5RiZtbEPQ3R-8aOdnAprCQuG3hP6pQ_k8aDpxvAUo5G_mvuKRJ9Byoot4VA-oYtrJg7XRQCljwlhMeZdl3F9y1GECxRLTuhElROHkm30HnUh9tItyUijUi603z_U5fM1qKQRYirekKl3TrcmhWNjs2jPQd40SLYjgSIw

manager JWT:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZEcm9MaTFHM3ZOQzZLNllQRlhkMiJ9.eyJpc3MiOiJodHRwczovL3N5d29uZ2lhbS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI3NTAyYzgwOWJiMGQwMDY4ZTUwNTkzIiwiYXVkIjoiY29mZmVlYXBpIiwiaWF0IjoxNjUzNjQ4Nzc1LCJleHAiOjE2NTM2NTU5NzUsImF6cCI6IkNIVll3OTlWSmREZVFST2g2WWNoQ0padmFsQlBhZU1HIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.GoMNK8KLK6NwtiK0zB8HLUkdli_lxYNQxU9OFmVVtUd6sAeSnePoS3wEA0AqPfJFm1AVxVIEHyJd16L73O40EQCJp6-bQKLFp80Im1bTWIBITTXHbGMbpGzXXsFQuUGxdyycRT_c5JIEZHlUreF-bV1G5zscm0aMLMut3VBiDyFLY5GJCw5RiZtbEPQ3R-8aOdnAprCQuG3hP6pQ_k8aDpxvAUo5G_mvuKRJ9Byoot4VA-oYtrJg7XRQCljwlhMeZdl3F9y1GECxRLTuhElROHkm30HnUh9tItyUijUi603z_U5fM1qKQRYirekKl3TrcmhWNjs2jPQd40SLYjgSIw


### Implement The Server

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



#####

Test your endpoints with [Postman](https://getpostman.com).
   
1. Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
2. Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
Run the collection and correct any errors.
3. use the new collection file to test udacity-fsnd-udaspicelatte.postman_collection-new.json

