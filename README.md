# Coffee Shop Full Stack

## Full Stack Nano - IAM Final Project

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. But they need help setting up their menu experience.

You have been called on to demonstrate your newly learned skills to create a full stack drink menu application. The application must:

1. Display graphics representing the ratios of ingredients in each drink.
2. Allow public users to view drink names and graphics.
3. Allow the shop baristas to see the recipe information.
4. Allow the shop managers to create new drinks and edit existing drinks.


### configuration in auth0

1. tenant created named sywongiam
2. application created named coffee 
3. 2 users are created in User Management -> Users
   sywong10@yahoo.com    barista role
   sywong109@gmail.com   manager role
4. barisa role includes permission get:drinks-detail
5. manager role includes permissions delete:drinks, get:drinks, get:drinks-detail, patch:drinks, post:drinks

##  below are two JWT tokens with permissions needed for barista and manager to manage coffee shop.
##

JWT for barista and manager

barista JWT:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZEcm9MaTFHM3ZOQzZLNllQRlhkMiJ9.eyJpc3MiOiJodHRwczovL3N5d29uZ2lhbS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI3NTAyYzgwOWJiMGQwMDY4ZTUwNTkzIiwiYXVkIjoiY29mZmVlYXBpIiwiaWF0IjoxNjUzNzAxOTMwLCJleHAiOjE2NTM3MDkxMzAsImF6cCI6IkNIVll3OTlWSmREZVFST2g2WWNoQ0padmFsQlBhZU1HIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.Hi-rqNcvqW5JsiGm8zy26gqLUjX4gcLlM1BrnOw7WN9Vk8JcVmVRYqJ1VHr_WSvGoGrF4FQY9cHD1geumYKz4076BqdMAQdT_Fgk-vS83ZqqvrKtz8jbD-ZTCyPDJJ8iy2vdeY07C6xS8BjjBhUFHJhNdtPS0pGzpxO9k5DajruHdCJOjnbN5oFQBHxbTBc1jWCab1VyLCPXEs6-Nn7xwdozfVRrIX7jVNtRkh78D6nYgyd0CZywIbC8Jm9uOUSzzdPmXw-ikbrLiF9sSEV18Z4KSoSDLRGUD3bUvYgWGY31IRIg61LvkI5vmk1AwYjjRx4a07dT4c6VCs2wq17mRQ

manager JWT:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZEcm9MaTFHM3ZOQzZLNllQRlhkMiJ9.eyJpc3MiOiJodHRwczovL3N5d29uZ2lhbS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI3NjI5MzM0Y2JmYTAwMDZlNmY1ZjNlIiwiYXVkIjoiY29mZmVlYXBpIiwiaWF0IjoxNjUzNzAyNTQ5LCJleHAiOjE2NTM3MDk3NDksImF6cCI6IkNIVll3OTlWSmREZVFST2g2WWNoQ0padmFsQlBhZU1HIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.Pn51jLVEA8gVVBjmDuY3T38he0HsGkNyq6WSGBL62MpLYg7ZB3VNU-FSFm8awNib0eiKfJajn2HADbH-CK90SgvgxQQcUf5a17ZNrCeruiE1vkvAfYf0xwRdmh11kVtjweNL29hfSzyelXlW7TFB7pg9cpjC94WIgMAQ7Oe_ranzgJTdKBBwSC5xpDO5HrW5_tBfawtluvAys_Q0DnXki6r42uJoxSEQLbC1ZLFBw4q24Zs5x6K09UcGmTZPwMaDsxioEcbuE-YfUgJogU6TtZK9fsyiYW0Z0KHcl3L_Mxm1jYJnoObnGD5Z6QwrkgwQEE0LkLJwq4ikhr3QQdANBQ


### Backend configuration and start

1. in backend/src/auth/auth.py file, contains auth0 domain, algorithms and api_audience in application in auth0 

AUTH0_DOMAIN = 'sywongiam.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'coffeeapi'

2. in auth.py file also contains functions to validate JWT token.  These functions are from Identity and Access Management class. 
3. create virtual env main folder
4. source venv/bin/activate
5. cd backend
6. pip install -r requirements.txt
7. cd src
8. export FLASK_APP=api.py
9. flask run --reload


### Frontend
1. download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).
2. download and install ionic cli [Ionic Framework Docs](https://ionicframework.com/docs/installation/cli).
3. $ cd frontend
4. $ npm install
5. application and auth0 variables are setup in start_code/frontend/src/environments/environments.ts  
6. $ ionic serve 
7. once ionic server is running, coffee images should be present in the drink-menu page
    http://localhost:8100/tabs/drink-menu
8. coffee recipes can be added, updated and deleted via interacting with rest endpoints using Postman.
9. login to frontend page by clicking on "User" - Login
10. once Login, the page will show existing recipes in database.


###  postman
###
1. install postman
2. Import the postman collection `./backend/udacity-fsnd-udaspicelatte.postman_collection.json`
3. Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs). 
4. Run the collection and correct any errors.

